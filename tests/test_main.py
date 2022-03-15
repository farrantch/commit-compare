import pytest
from main import commit_compare

def test_farrantch_saaas_small(capfd):
    pat = None
    org = 'farrantch'
    repo = 'saaas'
    head = '1ed614fbd4600b4e736e4a36ada545a9bc95ca27'
    base = '7ffa15e06231da797a567fb93698b913a52e5222'
    commit_compare(pat=pat, org=org, repo=repo, head=head, base=base)
    out, err = capfd.readouterr()
    answer = "2018-08-25 00:27:44 - Chase Farrant - initial commit\n2018-08-25 00:28:29 - Chase Farrant - Create README.md\n"
    assert out == answer


def test_farrantch_saaas_large(capfd):
    pat = None
    org = 'farrantch'
    repo = 'saaas'
    head = '61eb66767e2b6197fb5b499d34fa1e17f834d1cc'
    base = '1ed614fbd4600b4e736e4a36ada545a9bc95ca27'
    commit_compare(pat=pat, org=org, repo=repo, head=head, base=base)
    out, err = capfd.readouterr()
    answer = """2018-08-25 00:28:29 - Chase Farrant - Create README.md
2018-08-25 00:47:30 - Chase Farrant - Update README.md
2018-08-25 01:34:09 - Chase Farrant - Update README.md
2018-08-25 01:34:41 - Chase Farrant - Update README.md
2018-11-21 15:16:22 - Chase Farrant - Update README.md
2019-04-18 23:22:26 - Chase Farrant - Update README.md\n"""
    assert out == answer


def test_invalid_head(capfd):
    pat = None
    org = 'farrantch'
    repo = 'saaas'
    head = '61eb66767e2b6197fb5b499d34fa1e17f834d1c'
    base = '1ed614fbd4600b4e736e4a36ada545a9bc95ca27'
    with pytest.raises(SystemExit) as e:
        commit_compare(pat=pat, org=org, repo=repo, head=head, base=base)
    assert e.type == SystemExit

def test_uncorrelated_commits(capfd):
    pat = None
    org = 'farrantch'
    repo = 'saaas'
    head = '1ed614fbd4600b4e736e4a36ada545a9bc95ca27'
    base = '61eb66767e2b6197fb5b499d34fa1e17f834d1c'
    with pytest.raises(SystemExit) as e:
        commit_compare(pat=pat, org=org, repo=repo, head=head, base=base)
    assert e.type == SystemExit

def test_python_bedevere(capfd):
    pat = None
    org = 'python'
    repo = 'bedevere'
    head = 'bbc8f7eb9f1bd2e6f65a6165ce166eb085c5997f'
    base = '188ae7db7864594bc723c1fd61d9718e6e692eba'
    commit_compare(pat=pat, org=org, repo=repo, head=head, base=base)
    out, err = capfd.readouterr()
    answer = """2017-03-31 23:04:47 - Brett Cannon - Initial commit
2017-03-31 23:13:52 - Brett Cannon - Update the license to be valid
2017-03-31 23:14:17 - Brett Cannon - Update the README
2017-03-31 23:19:13 - Brett Cannon - Initial code commit
2017-03-31 23:19:20 - Brett Cannon - Explain what the bot does
2017-04-01 20:26:37 - Brett Cannon - Consider a PR w/ a "trivial" label as passing
2017-04-02 18:55:30 - Brett Cannon - Set up Heroku
2017-04-02 18:59:41 - Brett Cannon - Handle a ping event
2017-04-02 19:07:05 - Brett Cannon - Add a test for the ping
2017-04-02 19:08:44 - Brett Cannon - Be less runtime-specific on Heroku
2017-04-02 19:11:18 - Brett Cannon - Fix a typo in the Procfile
2017-04-02 19:15:09 - Brett Cannon - Get the port from the environment
2017-04-02 19:18:29 - Brett Cannon - Pass in a port as an int
2017-04-02 19:35:07 - Brett Cannon - Change the SHA URL to be the test one
2017-04-02 21:25:07 - Brett Cannon - Fix the failure URL and message
2017-04-03 02:28:35 - Brett Cannon - Be looser in matching the issue number
2017-04-03 02:40:12 - Brett Cannon - Pull the statuses URL instead of calculating it
2017-04-03 03:00:07 - Brett Cannon - Add a Travis file
2017-04-07 18:17:24 - Brett Cannon - Assign copyright to the PSF
2017-04-07 18:23:43 - Brett Cannon - Add the Travis badge
2017-04-10 23:14:37 - Brett Cannon - Mention "trivial" label in failure message (#2)
2017-04-14 18:04:17 - Brett Cannon - Add code coverage (#7)
2017-04-14 18:05:29 - Brett Cannon - Add code coverage badge
2017-04-15 23:40:29 - Mariatta - Link to b.p.o when both issue number and trivial label are found (#5)
2017-04-16 20:55:20 - Brett Cannon - Skip coverage for unimportant code (#10)
2017-04-18 00:27:22 - Brett Cannon - Get tests to 100% coverage (#11)
2017-04-18 00:39:30 - Brett Cannon - Remove redundant test (#12)
2017-06-02 01:01:43 - Mariatta - Pin the versions in requirements-dev.txt (#16)
2017-06-03 19:12:46 - Brett Cannon - Use gidgethub's router (#17)
2017-06-04 20:09:43 - Brett Cannon - Use an LRU cache for gidgethub (#18)
2017-06-08 22:02:16 - Brett Cannon - Try to clarify where to put the issue number in the PR title
2017-06-16 19:51:54 - Brett Cannon - Automatically remove backport labels (#19)
2017-06-16 20:26:48 - Brett Cannon - Fix code to work with an event and not a pull request directly (#20)
2017-06-17 17:58:12 - Brett Cannon - Fix dispatching of the backport module (#21)
2017-06-17 18:02:24 - Brett Cannon - Add a period to the message that is left by the backport
2017-06-23 15:57:09 - Adam Leskis - Fix simple typo (#23)
2017-07-14 17:20:35 - Mariatta - Check for "skip issue" instead of a "trivial" label (#28)
2017-07-14 20:28:22 - Brett Cannon - Update the devguide URL (#29)
2017-07-14 21:28:24 - Brett Cannon - Use an async context manager (#30)
2017-07-21 20:02:36 - Brett Cannon - Drop periods from status description (#31)
2017-07-21 21:21:03 - Kushal Das - Add a link to b.p.o at the end of the message body (#24)
2017-07-21 22:25:25 - Brett Cannon - Fix the body replacement code (#32)
2017-07-25 16:26:16 - Brett Cannon - Specifically say admins can modify a PR (#35)
2017-08-11 19:13:49 - Brett Cannon - Set a stage label for a PR (#33)
2017-08-11 21:27:39 - Brett Cannon - Wire up the stage router (#36)
2017-08-11 23:07:58 - Brett Cannon - Handle "unlabeled" events when a label is deleted (#37)
2017-08-14 18:17:00 - Brett Cannon - Check for a news entry (#22)
2017-08-14 18:39:25 - Brett Cannon - Mention the "skip news" label (#40)
2017-08-14 19:36:22 - Brett Cannon - Handle "skip news" label changes appropriately (#41)
2017-08-14 20:54:58 - Brett Cannon - Update file matching (#43)
2017-08-14 21:10:04 - Brett Cannon - Take the 'next' directory into account (#44)
2017-08-14 21:54:47 - Brett Cannon - Touch up the change review notification (#45)
2017-08-15 21:09:52 - Brett Cannon - Shorten bpo issue # check failure description (#48)
2017-08-18 18:52:40 - Brett Cannon - Tweak the "changes requested" message (#51)
2017-08-18 22:13:28 - Brett Cannon - Don't leave another "changes requested" comment if already awaiting changes (#52)
2017-08-29 17:41:38 - Mariatta - Remove backport label when PR is edited. (GH-56)
2017-09-29 17:17:38 - Mariatta - Close PRs that try to merge a maintenance branch into master (#60)
2017-09-29 19:17:24 - Brett Cannon - Better failure messages for news entries (#62)
2017-09-29 21:49:03 - Brett Cannon - Completely ignore comment reviews from stage decisions (#63)
2017-10-04 17:33:15 - Mariatta - Remove any "awaiting.." labels when a PR is merged. (GH-58)
2017-10-06 22:17:49 - Brett Cannon - Print out the remaining GH quota after each successful call (#64)
2017-10-10 18:49:38 - Brett Cannon - Support a more muted trigger phrase for re-review (#66)
2017-10-12 18:27:00 - Brett Cannon - Copy labels from parent PR to backport PR(s) (#65)
2017-10-18 21:34:43 - Mariatta - pull_request_review state should be `commented` instead of `comment`. (GH-68)
2017-11-15 18:12:29 - Mariatta - Close PRs that try to merge a user's maintenance branch into master (GH-70)
2017-11-16 19:34:10 - Mariatta - Only close invalid PRs that match Python maintenance branch patterns. (GH-73)
2017-11-23 04:43:19 - Mariatta - Cleanup test_stage.py (GH-74)
2017-11-23 04:55:38 - Mariatta - Make the "Change requested" message brief when PR is authored by Core Dev (GH-75)
2017-11-28 21:48:40 - delirious-lettuce - Fix some spelling mistakes (#77)
2017-12-08 02:12:01 - Mariatta - Use Travis to test against 3.6-dev and 3.7-dev (GH-78)
2018-01-24 19:57:05 - pyup.io bot - create pyup.io config file (#80)
2018-01-24 20:02:49 - pyup.io bot - Initial Update (#81)
2018-01-24 20:11:39 - Mariatta - Fix issue where PR without any description has its title edited (GH-79)
2018-01-26 17:56:45 - Mariatta - Remind core dev to replace # into GH- in the commit message. (GH-82)
2018-01-26 21:00:31 - Mariatta - Actually import the follow_up module. (GH-83)
2018-01-26 21:09:58 - Mariatta - Post to the review_comment_url instead of comments_url (GH-84)
2018-01-26 21:21:14 - Mariatta - The correct url is review_comments_url (with an s) (GH-85)
2018-01-26 21:44:02 - Mariatta - It uses comments_url after all? (GH-86)
2018-01-26 21:54:28 - Mariatta - Use committer info instead of author. (GH-87)
2018-01-26 23:15:46 - Mariatta - Use the pull_request merged_by data as the committer. (GH-89)
2018-01-30 22:47:19 - Mariatta - Don't add "None" when PR body is empty. (#91)
2018-02-01 19:04:39 - pyup.io bot - Scheduled monthly dependency update for February (#92)
2018-02-02 13:32:51 - Mariatta - Set Heroku runtime environment to Python 3.6.4 (GH-93)
2018-02-21 03:11:59 - Mariatta - Dismiss review request from invalid PRs. (GH-96)
2018-03-13 20:54:43 - Andrew Svetlov - Adopt to aiohttp 3.0 (#101)
2018-04-02 18:22:46 - pyup.io bot - Scheduled monthly dependency update for April (#102)
2018-05-01 16:45:41 - pyup.io bot - Scheduled monthly dependency update for May (#104)
2018-05-16 20:41:32 - Brett Cannon - Be more tolerant of title formats (#105)
2018-06-01 21:12:29 - pyup.io bot - Scheduled monthly dependency update for June (#107)
2018-06-13 03:20:52 - Mariatta - Use Python 3.6.5 in Heroku (GH-110)
2018-06-29 20:44:08 - Mariatta - Use Python 3.6.6 runtime (GH-114)
2018-06-30 19:54:08 - Mariatta - Use Python 3.7.0 in Heroku (#115)
2018-07-02 04:45:54 - pyup.io bot - Scheduled monthly dependency update for July (#116)
2018-07-09 04:36:56 - Andrés Delfino - Improve the test cases of awaiting labels removal (#118)
2018-07-13 21:14:29 - Cheryl Sabella - Add type labels for docs and tests. (#108)
2018-07-14 01:41:18 - Mariatta - Check for news entry and bpo number when PR is reopened. (#119)
2018-07-14 01:50:02 - Mariatta - The delivery_id argument for gidgethub.sansio.event should be a `str`. (#120)
2018-07-21 03:44:39 - Mariatta - Post a status check for backport PR title. (#112)
2018-07-21 04:06:37 - Mariatta - Validate the PR title when PR was reopened. (#122)
2018-07-27 04:09:24 - Mayank Singhal - Automatically hyperlink `bpo-` text. (#121)
2018-07-27 21:25:40 - Mariatta - Update The Spanish Inquisition urls (#123)
2018-08-01 17:12:42 - pyup.io bot - Scheduled monthly dependency update for August (#126)
2018-08-04 14:58:59 - Mariatta - Only check for the maintenance branch `[X.Y]` prefix. (#125)
2018-08-24 18:32:55 - Mariatta - News status: Only post success status if news entry is at least 30 characters. (GH-128)
2018-09-04 16:52:51 - pyup.io bot - Scheduled monthly dependency update for September (#129)
2018-10-05 22:37:15 - Brett Cannon - Make a string raw (#132)
2018-10-13 04:45:00 - Sathwik Matsa - Fix link to bugs.python.org (#134)
2018-11-01 23:54:33 - pyup.io bot - Scheduled monthly dependency update for November (#140)
2018-11-07 18:53:13 - Mariatta - Invalid PRs: leave comment and add "invalid" label. (#138)
2018-12-01 22:21:39 - pyup.io bot - Scheduled monthly dependency update for December (#142)
2018-12-07 03:39:11 - Mariatta - Set Heroku runtime to 3.7.1 (#143)
2018-12-12 00:09:28 - Mariatta - Provide link to blurb-it (#145)
2018-12-14 19:16:56 - Lysandros Nikolaou - Fix broken link in README (#147)
2019-01-02 22:37:05 - pyup.io bot - Scheduled monthly dependency update for January (#150)
2019-02-01 17:57:48 - pyup.io bot - Scheduled monthly dependency update for February (#151)
2019-02-12 00:30:53 - Mariatta - The news status check will pass as long as the news file is not empty. (#152)
2019-02-16 03:14:08 - Mariatta - Use the xenial dist when testing Python 3.7 (#154)
2019-02-25 22:51:18 - Mariatta - Use Python 3.7.2 (#155)
2019-03-01 18:14:02 - pyup.io bot - Scheduled monthly dependency update for March (#156)
2019-03-21 20:18:38 - Lysandros Nikolaou - Apply 'awaiting core review' label to new core-dev PRs (#158)
2019-04-01 19:43:21 - pyup.io bot - Update pytest from 4.3.0 to 4.4.0 (#161)
2019-04-08 02:48:45 - Mariatta - Don't pass `maintainer_can_modify` when patching the PR. (#163)
2019-05-06 17:27:57 - pyup.io bot - Scheduled monthly dependency update for May (#166)
2019-05-06 17:30:04 - Lysandros Nikolaou - Linkify bpo mentions in commit comments (#160)
2019-05-30 17:05:52 - Mariatta - Add sentry (#170)
2019-05-30 17:26:08 - Mariatta - Remove test against 3.6 in .travis.yml (#171)
2019-05-31 22:37:40 - Gordon P. Hemsley - Avoid putting new bpo links inside of existing links (#167)
2019-06-05 04:23:00 - Mariatta - Update pip in travis.yml file (#173)
2019-06-21 23:14:56 - Mariatta - Automatically create "needs backport to" label when maintenance branch created. (#174)
2019-06-28 17:52:30 - pyup.io bot - Scheduled monthly dependency update for June (#172)
2019-07-02 16:43:51 - pyup.io bot - Scheduled monthly dependency update for July (#177)
2019-07-03 01:07:06 - Mariatta - Delete .pyup.yml (#178)
2019-07-03 17:19:29 - amaajemyfren - Fix bedevere's Youtube link  (#176)
2019-07-08 21:08:50 - dependabot-preview[bot] - Bump pytest from 5.0.0 to 5.0.1 (#180)
2019-07-18 18:29:57 - ssd71 - Add more details to the README (#181)
2019-08-02 22:47:36 - Giovanni Cappellotto - Fix PR state machine graph (#182)
2019-08-02 22:52:34 - Giovanni Cappellotto - Add a test case for a subsequent non-core dev review after a core dev review (#183)
2019-09-10 11:17:39 - Lysandros Nikolaou - Validate bpo issue numbers (#159)
2019-09-10 13:36:44 - Lysandros Nikolaou - Request review on GitHub when the PR needs change review (#168)
2019-09-18 17:52:07 - Brett Cannon - Use the latest Python version on Heroku
2019-09-23 22:40:19 - Brett Cannon - Explicitly require 'session' objects to be passed into set_status() (#193)
2019-09-24 21:05:16 - dependabot-preview[bot] - Bump pytest from 5.0.1 to 5.1.3 (#190)
2019-09-30 21:58:50 - dependabot-preview[bot] - Bump pytest from 5.1.3 to 5.2.0 (#194)
2019-10-07 18:52:18 - dependabot-preview[bot] - Bump pytest from 5.2.0 to 5.2.1 (#195)
2019-10-21 18:25:27 - Shibani Shankar Dash - Added verbose edge labels and new edge colour for triager actions (#197)
2019-10-21 21:30:50 - Mariatta - Use Python 3.7.5 runtime (#199)
2019-10-25 18:57:10 - dependabot-preview[bot] - Bump pytest from 5.2.1 to 5.2.2 (#202)
2019-10-28 18:16:38 - Henry Harutyunyan - Removing Monty Python joke refference links. (#203)
2019-11-15 17:40:31 - dependabot-preview[bot] - Bump pytest from 5.2.2 to 5.2.3 (#204)
2019-11-18 18:44:54 - dependabot-preview[bot] - Bump pytest from 5.2.3 to 5.2.4 (#205)
2019-12-16 19:41:49 - dependabot-preview[bot] - Bump pytest from 5.2.4 to 5.3.2 (#208)
2020-01-20 22:18:42 - dependabot-preview[bot] - Bump pytest from 5.3.2 to 5.3.3 (#212)
2020-01-21 22:33:30 - dependabot-preview[bot] - Bump pytest from 5.3.3 to 5.3.4 (#213)
2020-01-30 21:00:07 - dependabot-preview[bot] - Bump pytest from 5.3.4 to 5.3.5 (#214)
2020-02-28 19:57:44 - Lysandros Nikolaou - Remove asynctest dependency and filter out deprecation warnings (#211)
2020-03-16 21:29:20 - dependabot-preview[bot] - Bump pytest from 5.3.5 to 5.4.1 (#217)
2020-04-21 19:45:07 - dependabot-preview[bot] - Bump pytest-asyncio from 0.10.0 to 0.11.0 (#218)
2020-05-04 17:33:34 - dependabot-preview[bot] - Bump pytest-asyncio from 0.11.0 to 0.12.0 (#221)
2020-05-11 21:33:04 - dependabot-preview[bot] - Bump pytest from 5.4.1 to 5.4.2 (#222)
2020-05-15 20:54:06 - Mariatta - Re-request core review when there is a new commit to the approved PR (#220)
2020-05-19 17:52:32 - Mariatta - Use Python 3.8.3 runtime (#224)
2020-06-03 17:30:04 - dependabot-preview[bot] - Bump pytest from 5.4.2 to 5.4.3 (#225)
2020-06-19 17:10:13 - Mariatta - Delete requirements.in (#227)
2020-06-19 22:17:23 - dependabot-preview[bot] - Bump multidict from 4.5.2 to 4.7.6 (#228)
2020-06-19 22:17:47 - dependabot-preview[bot] - Bump yarl from 1.3.0 to 1.4.2 (#229)
2020-06-19 22:18:19 - dependabot-preview[bot] - Bump py from 1.8.0 to 1.8.2 (#230)
2020-06-19 22:18:46 - dependabot-preview[bot] - Bump six from 1.12.0 to 1.15.0 (#232)
2020-06-19 23:51:05 - dependabot-preview[bot] - Bump appdirs from 1.4.3 to 1.4.4 (#231)
2020-06-19 23:51:25 - dependabot-preview[bot] - Bump cachetools from 3.1.1 to 4.1.0 (#233)
2020-06-19 23:51:42 - dependabot-preview[bot] - Bump packaging from 19.0 to 20.4 (#234)
2020-06-19 23:52:02 - dependabot-preview[bot] - Bump sentry-sdk from 0.9.5 to 0.15.1 (#235)
2020-06-19 23:52:19 - dependabot-preview[bot] - Bump gidgethub from 3.1.0 to 4.1.1 (#236)
2020-06-19 23:52:36 - dependabot-preview[bot] - Bump pyparsing from 2.4.0 to 2.4.7 (#237)
2020-06-25 00:28:56 - dependabot-preview[bot] - Bump pytest-asyncio from 0.12.0 to 0.14.0 (#238)
2020-06-26 17:51:31 - dependabot-preview[bot] - Bump py from 1.8.2 to 1.9.0 (#239)
2020-06-29 20:20:17 - dependabot-preview[bot] - Bump cachetools from 4.1.0 to 4.1.1 (#240)
2020-07-07 18:47:58 - Mariatta - Add codecov.yml and pytest-cov dependency (#241)
2020-07-07 18:48:20 - dependabot-preview[bot] - Bump sentry-sdk from 0.15.1 to 0.16.0 (#242)
2020-07-14 21:34:16 - dependabot-preview[bot] - Bump sentry-sdk from 0.16.0 to 0.16.1 (#244)
2020-07-16 20:00:15 - dependabot-preview[bot] - Bump codecov from 2.1.7 to 2.1.8 (#245)
2020-07-23 19:04:56 - dependabot-preview[bot] - Bump sentry-sdk from 0.16.1 to 0.16.2 (#248)
2020-08-05 22:12:25 - dependabot-preview[bot] - Bump pytest from 5.4.3 to 6.0.1 (#251)
2020-08-05 22:12:40 - dependabot-preview[bot] - Bump yarl from 1.4.2 to 1.5.1 (#252)
2020-08-06 00:08:19 - dependabot-preview[bot] - Bump sentry-sdk from 0.16.2 to 0.16.3 (#253)
2020-08-11 23:40:01 - Mariatta - Bump the Python runtime environment to 3.8.5 (#255)
2020-08-14 16:54:19 - dependabot-preview[bot] - Bump sentry-sdk from 0.16.3 to 0.16.4 (#256)
2020-08-17 16:54:13 - dependabot-preview[bot] - Bump pytest-cov from 2.10.0 to 2.10.1 (#258)
2020-08-17 16:54:26 - dependabot-preview[bot] - Bump sentry-sdk from 0.16.4 to 0.16.5 (#257)
2020-08-24 19:14:12 - dependabot-preview[bot] - Bump codecov from 2.1.8 to 2.1.9 (#260)
2020-08-25 21:39:59 - dependabot-preview[bot] - Bump sentry-sdk from 0.16.5 to 0.17.0 (#261)
2020-08-31 19:05:07 - dependabot-preview[bot] - Bump sentry-sdk from 0.17.0 to 0.17.1 (#262)
2020-09-02 16:49:43 - dependabot-preview[bot] - Bump sentry-sdk from 0.17.1 to 0.17.2 (#263)
2020-09-03 19:08:22 - dependabot-preview[bot] - Bump sentry-sdk from 0.17.2 to 0.17.3 (#264)
2020-09-10 16:22:37 - dependabot-preview[bot] - Bump sentry-sdk from 0.17.3 to 0.17.4 (#267)
2020-09-14 18:38:04 - dependabot-preview[bot] - Bump pytest from 6.0.1 to 6.0.2 (#268)
2020-09-15 18:29:15 - dependabot-preview[bot] - Bump sentry-sdk from 0.17.4 to 0.17.5 (#270)
2020-09-16 18:11:54 - dependabot-preview[bot] - Bump sentry-sdk from 0.17.5 to 0.17.6 (#271)
2020-09-23 21:42:27 - dependabot-preview[bot] - Bump sentry-sdk from 0.17.6 to 0.17.7 (#272)
2020-09-24 17:14:50 - dependabot-preview[bot] - Bump sentry-sdk from 0.17.7 to 0.17.8 (#274)
2020-09-24 17:50:05 - dependabot-preview[bot] - Bump yarl from 1.5.1 to 1.6.0 (#273)
2020-09-28 21:00:49 - dependabot-preview[bot] - Bump pytest from 6.0.2 to 6.1.0 (#277)
2020-10-05 16:36:13 - dependabot-preview[bot] - Bump pytest from 6.1.0 to 6.1.1 (#279)
2020-10-13 19:28:02 - dependabot-preview[bot] - Bump codecov from 2.1.9 to 2.1.10 (#281)
2020-10-13 19:28:17 - dependabot-preview[bot] - Bump yarl from 1.6.0 to 1.6.2 (#283)
2020-10-13 19:41:34 - dependabot-preview[bot] - Bump aiohttp from 3.6.2 to 3.6.3 (#284)
2020-10-20 22:01:04 - dependabot-preview[bot] - Bump sentry-sdk from 0.17.8 to 0.19.1 (#286)
2020-10-26 18:43:50 - dependabot-preview[bot] - Bump aiohttp from 3.6.3 to 3.7.1 (#288)
2020-10-28 16:44:40 - dependabot-preview[bot] - Bump aiohttp from 3.7.1 to 3.7.2 (#289)
2020-10-29 16:46:57 - dependabot-preview[bot] - Bump pytest from 6.1.1 to 6.1.2 (#290)
2020-11-02 21:38:53 - Lysandros Nikolaou - Do not apply the 'awaiting merge' label on a closed PR (#292)
2020-11-03 17:49:54 - dependabot-preview[bot] - Bump sentry-sdk from 0.19.1 to 0.19.2 (#293)
2020-11-13 17:38:23 - dependabot-preview[bot] - Bump sentry-sdk from 0.19.2 to 0.19.3 (#294)
2020-11-16 21:30:10 - dependabot-preview[bot] - Bump multidict from 4.7.6 to 5.0.2 (#295)
2020-11-16 21:30:25 - dependabot-preview[bot] - Bump yarl from 1.6.2 to 1.6.3 (#296)
2020-11-19 18:11:49 - dependabot-preview[bot] - Bump aiohttp from 3.7.2 to 3.7.3 (#297)
2020-11-19 18:12:16 - dependabot-preview[bot] - Bump gidgethub from 4.1.1 to 4.2.0 (#298)
2020-11-20 17:45:12 - dependabot-preview[bot] - Bump sentry-sdk from 0.19.3 to 0.19.4 (#299)
2020-11-30 18:29:40 - dependabot-preview[bot] - Bump packaging from 20.4 to 20.7 (#300)
2020-12-04 06:36:18 - dependabot-preview[bot] - Bump multidict from 5.0.2 to 5.1.0 (#301)
2020-12-11 23:08:38 - dependabot-preview[bot] - Bump sentry-sdk from 0.19.4 to 0.19.5 (#304)
2020-12-11 23:08:55 - dependabot-preview[bot] - Bump cachetools from 4.1.1 to 4.2.0 (#303)
2020-12-11 23:37:31 - dependabot-preview[bot] - Bump chardet from 3.0.4 to 4.0.0 (#302)
2020-12-14 18:54:08 - Mariatta - Update to 3.8.6 runtime (#308)
2020-12-14 19:48:57 - dependabot-preview[bot] - Bump py from 1.9.0 to 1.10.0 (#306)
2020-12-14 22:40:39 - Mariatta - Add 3.9 to travis.yml and don't allow failure in 3.8 (#309)
2020-12-14 22:49:30 - Mariatta - Use Python 3.9.1 (#310)
2020-12-18 17:46:36 - dependabot-preview[bot] - Bump codecov from 2.1.10 to 2.1.11 (#313)
2021-01-19 17:23:29 - dependabot-preview[bot] - Bump pytest-cov from 2.10.1 to 2.11.0 (#315)
2021-01-21 18:22:47 - dependabot-preview[bot] - Bump pytest-cov from 2.11.0 to 2.11.1 (#316)
2021-01-26 00:24:37 - dependabot-preview[bot] - Bump cachetools from 4.2.0 to 4.2.1 (#317)
2021-02-02 00:00:43 - dependabot-preview[bot] - Bump packaging from 20.8 to 20.9 (#319)
2021-02-18 01:01:30 - dependabot-preview[bot] - Bump sentry-sdk from 0.19.5 to 0.20.2 (#322)
2021-02-19 18:38:16 - dependabot-preview[bot] - Bump sentry-sdk from 0.20.2 to 0.20.3 (#323)
2021-04-15 21:34:30 - dependabot[bot] - Bump aiohttp from 3.7.3 to 3.7.4 (#324)
2021-04-16 22:03:35 - dependabot-preview[bot] - Bump aiohttp from 3.7.4 to 3.7.4.post0 (#330)
2021-04-18 20:04:12 - dependabot-preview[bot] - Bump chardet from 3.0.4 to 4.0.0 (#311)
2021-04-18 20:04:36 - dependabot-preview[bot] - Bump sentry-sdk from 0.20.3 to 1.0.0 (#325)
2021-04-19 17:07:05 - Mariatta Wijaya - Add GitHub Actions to run tests (#329)
2021-04-19 21:45:18 - dependabot-preview[bot] - Bump pytest from 6.1.2 to 6.2.3 (#327)
2021-04-22 17:43:44 - dependabot-preview[bot] - Bump pytest-asyncio from 0.14.0 to 0.15.0 (#332)
2021-04-28 22:01:18 - dependabot-preview[bot] - Bump cachetools from 4.2.1 to 4.2.2 (#333)
2021-04-28 22:02:21 - Mariatta Wijaya - Remove travis.yml file (#335)
2021-04-29 00:08:30 - dependabot-preview[bot] - Bump gidgethub from 4.2.0 to 5.0.1 (#326)
2021-04-29 16:24:23 - dependabot-preview[bot] - Upgrade to GitHub-native Dependabot (#336)
2021-05-03 22:39:12 - Pablo Galindo - Account for the renaming of the 'master' branch to 'main' (#338)
2021-05-05 14:49:47 - dependabot[bot] - Bump pytest from 6.2.3 to 6.2.4 (#339)
2021-05-06 19:55:27 - dependabot[bot] - Bump six from 1.15.0 to 1.16.0 (#340)
2021-05-07 18:33:19 - dependabot[bot] - Bump sentry-sdk from 1.0.0 to 1.1.0 (#341)
2021-05-17 22:38:03 - dependabot[bot] - Bump pytest-cov from 2.11.1 to 2.12.0 (#342)
2021-05-19 16:56:11 - Mariatta Wijaya - Update the readme to reference CPython main branch. (#343)
2021-06-02 22:34:25 - dependabot[bot] - Bump pytest-cov from 2.12.0 to 2.12.1 (#345)
2021-07-13 20:58:35 - dependabot[bot] - Bump packaging from 20.9 to 21.0 (#346)
2021-07-13 21:00:49 - dependabot[bot] - Bump sentry-sdk from 1.1.0 to 1.3.0 (#348)
2021-07-28 20:02:59 - dependabot[bot] - Bump sentry-sdk from 1.3.0 to 1.3.1 (#349)
2021-08-04 20:21:15 - dependabot[bot] - Bump codecov from 2.1.11 to 2.1.12 (#350)
2021-08-31 20:30:44 - dependabot[bot] - Bump pytest from 6.2.4 to 6.2.5 (#351)
2021-09-24 19:01:31 - dependabot[bot] - Bump sentry-sdk from 1.3.1 to 1.4.1 (#353)
2021-09-28 18:51:00 - dependabot[bot] - Bump sentry-sdk from 1.4.1 to 1.4.2 (#354)
2021-09-30 22:13:38 - dependabot[bot] - Bump sentry-sdk from 1.4.2 to 1.4.3 (#356)
2021-09-30 22:13:48 - dependabot[bot] - Bump cachetools from 4.2.2 to 4.2.3 (#355)
2021-10-01 18:09:57 - dependabot[bot] - Bump cachetools from 4.2.3 to 4.2.4 (#357)
2021-10-04 18:18:47 - dependabot[bot] - Bump multidict from 5.1.0 to 5.2.0 (#358)
2021-10-04 18:19:05 - dependabot[bot] - Bump pytest-cov from 2.12.1 to 3.0.0 (#359)
2021-10-18 19:36:52 - dependabot[bot] - Bump yarl from 1.6.3 to 1.7.0 (#360)
2021-10-18 19:38:17 - dependabot[bot] - Bump pytest-asyncio from 0.15.1 to 0.16.0 (#364)
2021-10-18 19:42:17 - dependabot[bot] - Bump uritemplate from 3.0.1 to 4.1.1 (#363)
2021-10-25 16:59:03 - dependabot[bot] - Bump pyparsing from 2.4.7 to 3.0.1 (#365)
2021-10-28 18:56:15 - dependabot[bot] - Bump pyparsing from 3.0.1 to 3.0.3 (#366)
2021-11-02 18:38:55 - dependabot[bot] - Bump yarl from 1.7.0 to 1.7.2 (#370)
2021-11-05 22:39:11 - dependabot[bot] - Bump py from 1.10.0 to 1.11.0 (#372)
2021-11-18 20:38:55 - dependabot[bot] - Bump packaging from 21.0 to 21.3 (#377)
2021-11-19 20:05:58 - dependabot[bot] - Bump pyparsing from 3.0.3 to 3.0.6 (#376)
2022-01-27 18:09:54 - dependabot[bot] - Bump cachetools from 4.2.4 to 5.0.0 (#383)
2022-01-27 18:10:46 - dependabot[bot] - Bump pytest-asyncio from 0.16.0 to 0.17.2 (#388)
2022-01-27 18:12:27 - dependabot[bot] - Bump multidict from 5.2.0 to 6.0.2 (#396)
2022-01-27 18:12:53 - dependabot[bot] - Bump pyparsing from 3.0.6 to 3.0.7 (#392)
2022-01-27 18:13:49 - dependabot[bot] - Bump sentry-sdk from 1.4.3 to 1.5.4 (#397)
2022-01-27 18:31:04 - dependabot[bot] - Bump aiohttp from 3.7.4.post0 to 3.8.1 (#375)
2022-01-27 18:31:25 - dependabot[bot] - Bump gidgethub from 5.0.1 to 5.1.0 (#393)
2022-01-27 18:37:41 - dependabot[bot] - Bump pytest-aiohttp from 0.3.0 to 1.0.3 (#395)
2022-01-27 18:40:24 - Mariatta Wijaya - Test against Python 3.10 (#398)
2022-01-27 18:51:57 - Mariatta Wijaya - Deploy to Python 3.10 on Heroku (#400)
2022-02-11 18:38:42 - dependabot[bot] - Bump pytest from 6.2.5 to 7.0.0 (#401)
2022-02-11 19:14:46 - dependabot[bot] - Bump pytest-asyncio from 0.17.2 to 0.18.1 (#403)\n"""
    assert out == answer