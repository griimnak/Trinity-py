from . import tpl
from trinity.router import Response

def View(request):
    s = "World!"
    return Response(tpl.render("home/main.html", test=s))
