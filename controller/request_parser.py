__author__ = 'harsh'
import json
from flask import Response, make_response
from controller.bugzilla_search import BugzillAPI
from controller.bitbucket_issues import BitBucketAPI
from controller.direct import DirectUrl, DebSummit, UbuntuEvents
from controller.git import GithubByRepo, GithubByUsername
from controller.udd import UddByEmail
from controller.rss import AtomAPI, RssAPI
from controller.helper import CalendarBuilder, FlaskError, SaveSession
from controller.db.dbobj import StoreSession


# noinspection PyBroadException
class AddEntry(object):

    def __init__(self, request) -> None:
        self.github_by_repo = []
        self.github_by_user = []
        self.bitbucket = []
        self.bugzilla = []
        self.direct = None
        self.rss = None
        self.atom = None
        self.ubuntu_events = False
        self.deb_summit = True
        self.udd = []
        self.gsoc = []
        self.items = []
        self.do_save = False
        """
        FIXME : dual entry problem
        Fixed in #2 :)
        """
        self.request = request
        self.parse()

    def get_resp(self) -> Response:
        try:
            if self.do_save:
                session_id = SaveSession(github_by_repo=self.github_by_repo,
                                         github_by_user=self.github_by_user,
                                         bitbucket=self.bitbucket,
                                         bugzilla=self.bugzilla,
                                         direct=self.direct,
                                         ubuntu_events=self.ubuntu_events,
                                         deb_summit=self.deb_summit,
                                         udd=self.udd,
                                         rss=self.rss,
                                         atom=self.atom).save()

                return Response(response=json.dumps({'Success': True, 'Session_id': session_id}), status=200,
                                content_type='application/json',
                                mimetype="application/json")

            else:
                self.build_resp()
                r = CalendarBuilder(self.items)
                resp = r.main()
                response = make_response(resp)
                response.headers["Content-Disposition"] = "attachment; filename=calendar.ics"
                return response

        except Exception as e:
            print(e)
            return Response(response=json.dumps(FlaskError().get_error()), status=500, content_type='application/json',
                            mimetype="application/json")

    def parse(self) -> bool:
        try:
            self.github_by_repo = self.request.get("github_by_repo", False)
            self.github_by_user = self.request.get("github_by_user", False)
            self.bitbucket = self.request.get("bitbucket", False)
            self.bugzilla = self.request.get("bugzilla", False)
            self.direct = self.request.get("direct", False)
            self.rss = self.request.get("rss", False)
            self.atom = self.request.get("atom", False)

            """
            Dirty Fix for blank remote iCal URL
            """
            if not self.direct:
                self.direct = False
            if not self.rss:
                self.rss = False
            if not self.atom:
                self.atom = False

            self.ubuntu_events = self.request.get("ubuntu_events", False)
            self.deb_summit = self.request.get("deb_summit", False)
            self.udd = self.request.get("udd", False)
            self.do_save = self.request.get("do_save", False)
            return True
        except Exception as e:
            print(e)
            return False

    def build_resp(self) -> None:
        if self.github_by_repo:
            self.items.append(GithubByRepo(repos=self.github_by_repo).main())
        if self.github_by_user:
            self.items.append(GithubByUsername(users=self.github_by_user).main())
        if self.bitbucket:
            self.items.append(BitBucketAPI(repos=self.bitbucket).main())
        if self.bugzilla:
            self.items.append(BugzillAPI(keywords=self.bugzilla).main())
        if self.direct:
            self.items.append(DirectUrl(url=self.direct).main())
        if self.ubuntu_events:
            self.items.append(UbuntuEvents().main())
        if self.deb_summit:
            self.items.append(DebSummit().main())
        if self.udd:
            self.items.append(UddByEmail(emails=self.udd).main())
        if self.rss:
            self.items.append(RssAPI(url=self.rss).main())
        if self.atom:
            self.items.append(AtomAPI(url=self.atom).main())


class GetEntry(object):
    def __init__(self, session_id):
        s = StoreSession()
        if s.exists(session_id):
            try:
                resp = s.get(key=session_id)
                resp['session_id'] = session_id
                self.response = Response(response=json.dumps(resp), status=200,
                                         content_type='application/json',
                                         mimetype="application/json")

            except Exception as e:
                print(e)
                self.response = Response(response=json.dumps(FlaskError().get_error()), status=500,
                                         content_type='application/json',
                                         mimetype="application/json")

        else:
            self.response = Response(response=json.dumps(FlaskError("Specified session_id was not found.").get_error()),
                                     status=404,
                                     content_type='application/json',
                                     mimetype="application/json")

    def get_resp(self) -> Response:
        return self.response


class GetDownload(object):
    data = {}
    items = []

    def __init__(self, session_id):
        self.session_id = session_id

    def get_resp(self) -> Response:
        s = StoreSession()
        if s.exists(self.session_id):
            self.data = s.get(self.session_id)
            self.build_resp()
            resp = CalendarBuilder(self.items).main()
            response = make_response(resp)
            response.headers["Content-Disposition"] = "attachment; filename=calendar.ics"
            return response

        else:
            return Response(response=FlaskError("Specified session_id was not found.").get_error(), status=404,
                            content_type='application/json',
                            mimetype="application/json")

    def build_resp(self) -> None:
        if self.data.get('github_by_repo', False):
            self.items.append(GithubByRepo(repos=self.data.get('github_by_repo')).main())

        if self.data.get('github_by_user', False):
            self.items.append(GithubByUsername(users=self.data.get('github_by_user')).main())

        if self.data.get('bitbucket', False):
            self.items.append(BitBucketAPI(repos=self.data.get('bitbucket')).main())

        if self.data.get('bugzilla', False):
            self.items.append(BugzillAPI(keywords=self.data.get('bugzilla')).main())

        if self.data.get('direct', False):
            self.items.append(DirectUrl(url=self.data.get('direct')).main())

        if self.data.get('ubuntu_events', False):
            self.items.append(UbuntuEvents().main())

        if self.data.get('deb_summit', False):
            self.items.append(DebSummit().main())

        if self.data.get('udd', False):
            self.items.append(UddByEmail(emails=self.data.get('udd')).main())
        if self.data.get('rss', False):
            self.items.append(RssAPI(url=self.data.get('rss')).main())
        if self.data.get('atom', False):
            self.items.append(AtomAPI(url=self.data.get('atom')).main())
