from flask import Flask,render_template,session

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'adbcenkle'
@app.route("/tmpl2")
def tmpl():
    # session 传值
    session["username"] = "John"

    content = {
        "show": False,
        "show_name": False,
        "name": "ben",
        "books": {
            "no1": "python",
            "no2": "java",
            "no3": "golang"
        },
        "number": [10,20,30,40]
    }
    return render_template("tmpl2.html", **content)

if __name__=="__main__":
    app.run(debug=True)