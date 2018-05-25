

class Response(object):
    """
    Creates response object, binding headers, status and body.
    """
    def __init__(self, body, status="200 OK"):
        self.status = status
        self.body = str(body) or ""
        self.headers = {
            "Content-Type": "text/html",
            "Content-Length": str(len(self.body)),
            "X-Powered-By": "Trinity-py-tr4.5"
        }

    @property
    def wsgi_headers(self):
        return [(k, v) for k, v in self.headers.items()]
