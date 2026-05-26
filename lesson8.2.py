from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "Homepage"

@app.route("/about")
def about():
    home_url = url_for('home')
    return f"Return to <a href = '{home_url}'>Home</a>"

@app.route("/old")
def old():
    return redirect('/new')

@app.route("/new")
def new():
    return "Redirected"

@app.route("/profile/<username>")
def profile(username):
    return f"User: {username}"

@app.route("/link")
def link():
    return redirect(url_for('profile', username='Mark'))

if __name__ == '__main__':
    app.run(debug=True)