from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello World!</h1>'

# Dynamic route to make app respond with personalized message.
@app.route('/user/<name>')
def user(name):
	return f'<h3>Hello { name } !!'