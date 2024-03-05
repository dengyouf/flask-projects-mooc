from flask import Flask, render_template

app = Flask(__name__)

@app.route("/global_func")
def global_func():
    content = {
        "no1": 20,
        "no2": 30
    }
    return render_template("tmpl4.html", **content)

def global_func(a, b):
    return  a+b

# 注册全局函数，就可以在html中调用了
app.jinja_env.globals.update(my_func=global_func)


if __name__ == "__main__":
    app.run(debug=True)
