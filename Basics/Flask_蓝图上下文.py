from flask  import  Flask,Blueprint,render_template

app = Flask(__name__)

user_bp = Blueprint("user_bp", "user", url_prefix="/user")

@user_bp.context_processor
def content_processor():
    return {"article": "Python is an easy way to"}
@user_bp.route("/article")
def get_article():
    # article = "Python is an easy way to"
    # return  render_template("user.html", article=article)
    # 有了蓝图上下文以后不传 article=article 也可以在html模版中使用
    return render_template("user.html")
@user_bp.route("/get")
def get_article_list():
    article = "Python is an easy way to"
    return render_template("article.html")
app.register_blueprint(user_bp)



if __name__ == "__main__":
    app.run(debug=True)
