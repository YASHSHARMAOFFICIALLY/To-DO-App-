from flask import render_template,Blueprint,request,redirect,flash,url_for,session
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_required,current_user
from app import db
from app.model import users
auth_bp = Blueprint('auth',__name__)
@auth_bp.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        existing_user = users.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exist")
            return redirect(url_for("auth.register"))
        new_users =users(username=username,password=generate_password_hash(password))
        db.session.add(new_users)
        db.session.commit()
        flash("registration sucessfull! please Login","sucess")
        return redirect(url_for("auth.register"))
    return render_template("register.html")
@auth_bp.route('/login',methods = ["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = users.query.filter_by(username=username).first()
        if user and check_password_hash(user.password,password):
            login_user(user)
            flash("Logged in sucessfully!","sucess")
            return redirect(url_for("tasks.view_tasks"))
        else:
            flash("Inavlid password or username","danger")
    return render_template("login.html")
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out sucessfully')
    return redirect(url_for("auth.login"))