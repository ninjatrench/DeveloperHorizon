import github
import icalendar
from conf import github_access_token, github_isPrivate

class Todo(object):
    conf = {}
    cache = {}

    def __init__(self):
        self.github_client = github.Github(github_access_token, user_agent='Debian-Dashboard')

    def make_uid(self, issue):
        return "%s-%s.issue.github.com" % (issue.number, issue.id)

    def make_title(self, repo_title, issue):
        return "%s #%s: %s" % (repo_title, issue.number, issue.title)

    def make_reporter(self, issue):
        return "%s@users.github.com" % issue.user.login

    def make_category(self, repo_title):
        return str(repo_title)

    def cache_manager(self, user):
        if user in self.cache:
            return self.cache.get(user)
        else:
            self.cache[user] = self.github_client.get_user(str(user)).email
            return self.cache_manager(user)

    def make_todo(self, issue, repo_title=None):
        if repo_title is None:
            repo_title = issue.repository.name

        try:
            todo = icalendar.Todo()
            todo['uid'] = self.make_uid(issue)
            todo['summary'] = self.make_title(repo_title, issue)
            todo['description'] = issue.body
            todo['url'] = issue.html_url
            todo['created'] = issue.created_at
            todo['last-modified'] = issue.updated_at
            todo['status'] = 'NEEDS-ACTION'
            todo['emailID'] = self.cache_manager(user=issue.user.login)
            todo['category'] = self.make_category(repo_title)
            todo['organizer'] = self.make_reporter(issue)
            return todo

        except Exception as e:
            print(e)
            return None


class GithubByUsername(Todo):
    Flag = True
    items = []

    def __init__(self, users):
        self.users = users
        super().__init__()

    def main(self):
        try:
            for i in self.users:
                user = self.github_client.get_user(i)
                for repos in user.get_repos():
                    print(repos.name)
                    self.fetch_issues(repo_name=str(i) + '/' + repos.name)

            return self.items

        except Exception as e:
            print(e)
            return "Some Error Occurred"

    def fetch_issues(self, repo_name):
        print(repo_name)
        repo_name_parts = repo_name.split('/')
        repo_title = repo_name_parts[1]
        repo = self.github_client.get_repo(repo_name)

        if self.Flag:
            for issue in repo.get_issues(state='open'):
                todo = self.make_todo(issue, repo_title)
                if todo:
                    self.items.append(todo)


class GithubByRepo(Todo):
    Flag = True
    items = []

    def __init__(self, repos):
        super().__init__()
        self.repos = repos
        self.main()

    def main(self):
        try:
            for i in self.repos:
                self.fetch_issues_by_repo(repo_name=i)

            return self.items

        except Exception as e:
            print(e)
            return "Some Error Occurred"

    def fetch_issues_by_repo(self, repo_name):
        print(repo_name)
        repo_name_parts = repo_name.split('/')
        repo_title = repo_name_parts[1]
        repo = self.github_client.get_repo(repo_name)

        if self.Flag:
            for issue in repo.get_issues(state='open'):
                todo = self.make_todo(issue, repo_title)
                if todo:
                    self.items.append(todo)


if __name__ == '__main__':
    pass