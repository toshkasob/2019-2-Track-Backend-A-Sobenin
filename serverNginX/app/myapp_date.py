from datetime import date, time, datetime
def showDate(environ, start_response):
    data = str(datetime.today())
    headers = [('Content-Type', 'text/plain'),
               ('Content-Length', str(len(data)))]
    start_response('200 OK', headers)
    return [data]