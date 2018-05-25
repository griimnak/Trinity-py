from urllib.parse import parse_qs


class Request(object):
    """
    Creates a request object.
    """
    def __init__(self, environ):
        self.environ = environ
        self.path = environ["PATH_INFO"]
        self.method = environ['REQUEST_METHOD']
        self.headers = {k: v for k, v in environ.items() if k.startswith("HTTP_")}
        self.params = None
        self.GET = parse_qs(environ["QUERY_STRING"])
        self.POST = {}

        # Experimental
        if environ.get('HTTPS', 'off') in ('on', '1'):
            self.environ['wsgi.url_scheme'] = 'https'
        else:
            self.environ['wsgi.url_scheme'] = 'http'

        if self.method == "POST":
            try:
                content_length = int(environ.get("CONTENT_LENGTH", 0))
            except ValueError:
                content_length = 0

            query_string = environ["wsgi.input"].read(content_length)
            self.POST = parse_qs(query_string)
