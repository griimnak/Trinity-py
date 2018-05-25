from . import tpl
from trinity.router import Response

def View(request):
    return Response(
        tpl.render("test/test.html", get_query=request.params[0])
    )
