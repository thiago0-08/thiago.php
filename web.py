from bottle import route, run, template
from bib import metros_para_cm

@route('/hello/<name>')
def index(name):
    return template('<b> aaaaaaaaaaa {{a}}</b>!', a=name)


@route('/ex1/<m:float>')
def ex1_route(m):
    cm = metros_para_cm(m)
    cm = f'{cm:.2f}'
    return template('<h1> {{r}}cm<h1>', r=cm)






run(host='localhost', port=8081, reloader=True)

