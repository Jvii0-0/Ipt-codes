from flask import Flask, url_for, redirect

app = Flask(__name__)

# @app.errorhandler(404)
# def page_not_found(e):
#     return "Page not found!", 404

@app.errorhandler(ZeroDivisionError)
def divide_by_zero(e):
    return "Cannot devide by zero", 500

if __name__ == '__main__':
    app.run(debug=True)