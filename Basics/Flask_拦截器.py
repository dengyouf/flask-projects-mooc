from flask import Flask, request,session

app = Flask(__name__)


app.config["SECRET_KEY"] = "dafafa"

@app.route("/login")
def login():
    session["is_login"] = True
    return "登陆"

@app.route("/update_user")
def update_user():
    return "update_user"

# 全局拦截器，会拦截所有请求，导致网站性能下降
@app.before_request
def before():
    # 获取用户请求的path， 根据url进行判断，那些拦截，那些放行
    url = request.path
    # 定义白名单
    pass_path = ["/", "/login", "/reg"]
    # 定义可通过的后缀名
    suffix = url.endswith("png") or url.endswith("jpg") or url.endswith("js") or url.endswith("css")
    if url in pass_path or suffix:
        pass
    else:
        if session.get('is_login') != True:
            return "请先登录~"

# 模块拦截器，蓝图拦截器
if __name__ == "__main__":
    app.run(debug=True)