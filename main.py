import argparse
import logging
import sys
from github import Github

log = logging.getLogger()

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pat', type=str, help='Github personal-access-token required.')
    parser.add_argument('--org', type=str, help='Github organization name required.', required=True)
    parser.add_argument('--repo', type=str, help='Github repository name required.', required=True)
    parser.add_argument('--head', type=str, help='Head commit required.', required=True)
    parser.add_argument('--base', type=str, help='Base commit required.', required=True)
    return parser.parse_args()

def traverse_git_tree(next_sha, base, commits):
    item = next((x for x in commits if x.sha == next_sha), None)
    if item == None:
        print("Item not found")
        return []
    if item.sha == base:
        return [item]
    if len(item.parents) > 0:
        for parent in item.parents:
            result = traverse_git_tree(parent.sha, base, commits)
            if result:
                temp = [item]
                temp.extend(result)
                return temp
    return []

def display_results(commits):
    for c in commits:
        date = c.commit.author.date
        name = c.commit.author.name
        message = c.commit.message.split('\n')[0]
        print(f"{date} - {name} - {message}")
    return

def get_repo(pat, org, repo):
    g = Github(args.pat if args.pat else None)
    try:
        return g.get_repo(f"{args.org}/{args.repo}")
    except:
        log.error("Unabe to connect to repo.")
        sys.exit()

def commit_compare(pat, org, repo, head, base):
    repo = get_repo(pat=pat, org=org, repo=repo)
    commits = repo.get_commits()
    relevant_commits = traverse_git_tree(head, base, commits)
    display_results(relevant_commits.__reversed__())

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