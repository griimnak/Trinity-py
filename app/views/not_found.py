from . import tpl
from trinity.router import Response

def View(request):
    return Response(
        tpl.render("not_found/main.html"),
        status="404 Not Found"
    )
