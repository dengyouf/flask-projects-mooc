from flask import  Flask, Blueprint

app = Flask(__name__)

user_bp = Blueprint("usr_bp", __name__, url_prefix="/user")

@user_bp.route('/add')
def add():
    return "add user"

@user_bp.route('/update')
def update():
    return "update user"

@user_bp.route('/delete')
def delete():
    return "delete user"

app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(debug=True)