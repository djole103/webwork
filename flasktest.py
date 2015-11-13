from flask import Flask, request, send_from_directory

app = Flask(__name__, static_url_path='')

#@app.route('/<path:path>')
#def send_js(path):
#    return send_from_directory('', path)

@app.route('/')
def root():
    return app.send_static_file('firstsite.html')

#@app.route('/')
#def hello_world():
#	return  "./firstsite.html" #"hello world"

if __name__ == "__main__":
	app.run()
