from flask import Flask
app = Flask(__name__)

# @app.route("/")
# def home():
#     return "This is home page"

# @app.route("/about")
# def about():
#     return "This is about page"

# @app.route("/contact")
# def contact():
#     return "This is contact page"

# @app.route("/user/<username>")
# def user(username):
#     return f"User: {username}"

# @app.route("/post/<int:postid>")
# def post(postid):
#     return f"Post ID: {postid}"

# @app.route("/price/<float:value>")
# def price(value):
#     return f"Price: {value}"

# @app.route("/files/<path:filepath>")
# def files(filepath):
#     return f"Filepath: {filepath}"

@app.route("/")
@app.route("/home")
def home():
    return "This is home page"

if __name__ == '__main__':
    app.run(debug=True)