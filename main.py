import argparse
import logging
import sys
from github import Github

log = logging.getLogger()

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pat', type=str, help='Github personal-access-token.')
    parser.add_argument('--org', type=str, help='Github organization name (Required)', required=True)
    parser.add_argument('--repo', type=str, help='Github repository name (Required)', required=True)
    parser.add_argument('--head', type=str, help='Head commit id (Required)', required=True)
    parser.add_argument('--base', type=str, help='Base commit (Required)', required=True)
    return parser.parse_args()

def traverse_git_tree(next_sha, base, commits):
    item = next((x for x in commits if x.sha == next_sha), None)
    if item.sha == base:
        return [item]
    elif len(item.parents) > 0:
        for parent in item.parents:
            result = traverse_git_tree(parent.sha, base, commits)
            if result:
                temp = [item]
                temp.extend(result)
                return temp
    elif len(item.parents) == 0:
        log.error("Unable to find coorelation between the commits. Perhaps they are swapped?")
        return []
    elif item == None:
        log.error("Error. Unable to find commit.")
        return []

def display_results(commits):
    for c in commits:
        date = c.commit.author.date
        name = c.commit.author.name
        message = c.commit.message.split('\n')[0]
        print(f"{date} - {name} - {message}")
    return

def valid_commit_id(id, commits):
    return any(x for x in commits if x.sha == id)

def get_repo(pat, org, repo):
    g = Github(pat if pat else None)
    try:
        return g.get_repo(f"{org}/{repo}")
    except:
        log.error("Error. Unable to connect to repo.")
        sys.exit()

def commit_compare(pat, org, repo, head, base):
    repo = get_repo(pat=pat, org=org, repo=repo)
    commits = repo.get_commits()
    # Validation
    if not valid_commit_id(head, commits):
        log.error("Invalid HEAD commit id.")
        sys.exit()
    if not valid_commit_id(base, commits):
        log.error("Invalid BASE commit id.")
        sys.exit()
    relevant_commits = traverse_git_tree(head, base, commits)
    display_results(relevant_commits.__reversed__())
    return

if __name__ == "__main__":
    # Get/Set Arguments
    args = get_args()
    pat = args.pat
    org = args.org
    repo = args.repo
    head = args.head
    base = args.base
    # Process
    commit_compare(pat=pat, org=org, repo=repo, head=head, base=base)