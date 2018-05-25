from app.views import *
"""
Application routes.
urls = dict([
    (ROUTE_URL, VIEW_ENDPOINT),
    (ROUTE_URL, VIEW_ENDPOINT)
])
"""
urls = dict([
    ('/', home.View),
    ('/hello/{get_query}', test.View)
])


