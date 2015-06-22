from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def hello(request):
    return Response('Hello world!')


def hello_dyn(request):
    return Response('Hello %(name)s!' % request.matchdict)


def show_request(request):
    return Response('<html><body><pre>%s</pre></body></html>' % request.as_text())


if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello_world', '/')
    config.add_view(hello, route_name='hello_world')
    config.add_route('hello_world_dyn', '/hello/{name}')
    config.add_view(hello_dyn, route_name='hello_world_dyn')
    config.add_route('request', '/request')
    config.add_view(show_request, route_name='request')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
