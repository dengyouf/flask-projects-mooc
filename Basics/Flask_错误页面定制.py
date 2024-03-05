from flask import  Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return  "hello world"

@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return "页面不存在!<br>{}".format(error)

@app.errorhandler(500)
def internal_server_error(error):

    return "内部服务器错误<br>{}".format(error)

if __name__ == "__main__":
    app.run()