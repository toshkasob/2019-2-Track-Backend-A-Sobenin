def handler(environ, start_response):
    data = b'Hello, my dear friend!'
    headers = [('Content-Type', 'text/plain')]
    #           ('Content-Length', str(len(data)))
    start_response('200 OK', headers)
    return [data]