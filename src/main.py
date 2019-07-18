from github import Github
from arguments import Arguments
from crawler import GithubCrawler
from results import ScanResults
from reporting import Reporting
from git_issue_creator import GitIssueCreator


def main():
    print("== DevSecOps: ignore ==\nScan github repositories for misconfigured ignore files.\n")

    args = Arguments()
    if not args.load():
        exit(0)
    github = Github(args.github_token)
    crawler = GithubCrawler(github, args.organization)
    results = ScanResults()
    try:
        crawler.scan(results)
    except KeyboardInterrupt:
        print("\n\n*****************************\n[W] User aborted with CTRL-C.\n*****************************\n")
        pass
    Reporting(verbose=args.verbose).print(results)
    if args.create_git_issue:
        GitIssueCreator(github, verbose=args.verbose).create_issues(results)


if __name__ == "__main__":
    main()
