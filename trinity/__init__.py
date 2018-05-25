import re

from trinity.template import to_regex
from trinity.router import Request

from app.views import not_found


class Trinity(object):
    """
    Main WSGI application. Sets routes and tpl_dir on init
    and dispatches Request object on __call__. Dispatcher
    then matches _req_url with _urls set by Trinity.
    """
    def __init__(self, routes=dict(), tpl_dir=""):
        self._routes = routes
        self._tpl_dir = tpl_dir

    def __call__(self, environ, start_response):
        response = self.dispatch(Request(environ))
        start_response(response.status, response.wsgi_headers)
        # Yield dispatcher response
        yield response.body.encode('UTF-8')

    def dispatch(self, request):
        _req_url = request.path
        for _url, View in self._routes.items():
            match = re.search(to_regex(_url), _req_url)
            if match is not None:
                # Send request params and return View
                request.params = match.groups()
                return View(request)
        # If match is None
        return not_found.View(request)
