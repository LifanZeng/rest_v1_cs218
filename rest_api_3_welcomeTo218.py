from bottle import Bottle, run, response, template
import time
import os
 
app = Bottle()
 
@app.route('/')
def hello():
	response.set_header('Vary', 'Accept')
	return '<h1>I am Lifan Zeng. Welcome to CS 218!</h1>'

@app.route('/now')
def time_server():
    	return time.ctime()

@app.route('/upper/<word>')
def upper_case_service(word):
	response.content_type = 'text/plain'
	return word.upper()

@app.route('/area/circle/<radius>')
def circle_area(radius):
	radius = float(radius)
	area = 3.14*radius*radius
	return f'<h1>The area is {area}</h1>'


file_template = '''\
<h1> List of files in <em> c-user-zengl-. </em> directory </h1>
<hr>
<ol>
  % for file in files:
    <li> <a href= "files/{{file}}"> {{file}} </a></li>
  % end
</ol>
'''
@app.route('/files')
def show_files():
	files = os.listdir(".")
	return template(file_template, files=files)


if __name__ == '__main__': 
    	run(app, host='localhost', port=8080)