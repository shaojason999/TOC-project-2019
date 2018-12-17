from bottle import route, run

@route('/')
@route('/message')
def hello():
    return "Hello World!"

@route('/message1')
def hello():
    return "Hello World!!"

run(host='localhost', port=8080, debug=True)
