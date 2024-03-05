from flask import Flask, make_response, request
import datetime

app = Flask(__name__)

# 设置cookies
@app.route("/set_ck")
def set_ck():
    response = make_response("设置cookie成功")

    # cookie 报错在客户端
    # response.set_cookie("name", "abc", max_age=10)

    expires_time = datetime.datetime.now()  + datetime.timedelta(seconds=60)
    response.set_cookie("name", "abc", expires=expires_time)
    response.set_cookie("age", "18", expires=expires_time)
    response.set_cookie("sex", 'man', expires=expires_time)
    return response

@app.route("/get_ck")
def get_ck():
    cookies = request.cookies
    print(cookies)

    print(cookies.to_dict())
    return cookies

@app.route("/del_ck")
def del_ck():
    response = make_response("删除cookie")
    # response.delete_cookie("name")
    for k,_ in  request.cookies.to_dict().items():
        response.delete_cookie(k)
    return  response

if __name__ == "__main__":
    app.run(debug=True)