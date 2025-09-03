from flask import Flask,render_template,request,url_for,session,flash,redirect,Blueprint
from flask_login import login_required,current_user
from app import db
from app.model import Task
tasks_bp = Blueprint('tasks',__name__)
@tasks_bp.route('/')
@login_required
def view_tasks():
    tasks = Task.query.filter_by(user_id =current_user.id).all()
    return render_template('tasks.html',tasks = tasks)
@tasks_bp.route('/add',methods = ["POST"])
@login_required
def add_task():
    title = request.form.get('title')
    if title:
        new_task =Task(title = title,status = 'Pending',user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added sucessfully','sucess')
    return redirect(url_for('tasks.view_tasks'))
@tasks_bp.route('/toggle/<int:task_id>', methods=["POST"])
@login_required
def toggle_status(task_id):
    tasks = Task.query.get(task_id)
    if tasks:
        if tasks.status == "Pending":
            tasks.status = 'Working'
        elif tasks.status == 'Working':
            tasks.status = 'Done'
        else:
            tasks.status = 'Pending'
        db.session.commit()
    return redirect(url_for('tasks.view_tasks'))
@tasks_bp.route('/delete/<int:task_id>',methods = ["POST"])
@login_required
def delete_task(task_id):
    tasks = Task.query.get(task_id)
    if tasks and tasks.user_id == current_user.id:
        db.session.delete(tasks)
        db.session.commit()
        flash("Task deleted sucessfully","info")
    return redirect(url_for('tasks.view_tasks'))
@tasks_bp.route('/clear',methods =["POST"])
@login_required
def clear_tasks():
    Task.query.filter_by(user_id = current_user.id).delete()
    db.session.commit()
    flash("All Tasks Cleared Sucessfully!",'info')
    return(redirect(url_for("tasks.view_tasks")))
