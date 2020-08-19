from flask import Flask, render_template

app = Flask(__name__)

# rendering template

@app.route('/')
def index():
	return render_template('index.html')

# Dynamic route to make app respond with personalized message.
@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)