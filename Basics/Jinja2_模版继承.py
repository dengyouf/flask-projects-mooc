from flask import Flask,render_template

app = Flask(__name__)

@app.route("/m")
def m():
    return render_template("m.html")


if __name__=="__main__":
    app.run(debug=True)