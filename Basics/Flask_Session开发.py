from flask import Flask, make_response, request, session
import datetime

app = Flask(__name__)

# 启用session
import os
app.config['SECRET_KEY'] =  os.urandom(24)

# 添加session
@app.route("/add_ss")
def add_ss():
    # 设置session， session 保存在服务端
    session['username'] = 'admin'
    session['nick_name'] = 'ben'

    return "添加session成功"

@app.route("/get_ss")
def get_ss():
    username = session.get("username")
    print(username)
    return "获取session成功"

@app.route("/del_ss")
def del_ss():
    session.clear()
    return "清除session成功"

if __name__ == "__main__":
    app.run(debug=True)