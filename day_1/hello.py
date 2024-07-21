from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye/<name>")       #(default) accepts any text without a slash  (String)
def string_world(name):
    return f"<p>Bye, {name}</p>"

@app.route("/number/<int:number>")  #accepts positive integers
def int_world(number):
    return f"<p>Here is the number {number}</p>"

@app.route("/float/<float:float_number>")  #accepts positive floating point values
def float_world(float_number):
    return f"<p>Here is the float number {float_number}</p>"



@app.route("/path/<path:subpath>")  #like string but also accepts slashes
def path_world(subpath):
    return f"<p>Here is the path {subpath}</p>"


if __name__ == "__main__":
    app.run(debug=True)