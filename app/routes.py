from flask import Blueprint, render_template, redirect, url_for, flash, request
from .forms import TaskForm
from .services import TaskService
from .models import Task

tasks_bp = Blueprint('tasks', __name__, template_folder='templates')

@tasks_bp.route('/')
def list_tasks():
    tasks = TaskService.get_all_tasks()
    return render_template('tasks/list.html', tasks=tasks)

@tasks_bp.route('/task/new', methods=['GET', 'POST'])
def create_task():
    form = TaskForm()
    if form.validate_on_submit():
        TaskService.create_task(form.data)
        flash('Tarefa criada com sucesso!', 'success')
        return redirect(url_for('tasks.list_tasks'))
    return render_template('tasks/form.html', form=form, title='Nova Tarefa')

@tasks_bp.route('/task/<int:task_id>/edit', methods=['GET', 'POST'])
def edit_task(task_id):
    task = TaskService.get_task_by_id(task_id)
    if not task:
        flash('Tarefa não encontrada!', 'error')
        return redirect(url_for('tasks.list_tasks'))
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        TaskService.update_task(task, form.data)
        flash('Tarefa atualizada com sucesso!', 'success')
        return redirect(url_for('tasks.list_tasks'))
    return render_template('tasks/form.html', form=form, title='Editar Tarefa')

@tasks_bp.route('/task/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    task = TaskService.get_task_by_id(task_id)
    if not task:
        flash('Tarefa não encontrada!', 'error')
    else:
        TaskService.delete_task(task)
        flash('Tarefa excluída com sucesso!', 'success')
    return redirect(url_for('tasks.list_tasks'))

@tasks_bp.route('/task/<int:task_id>')
def task_detail(task_id):
    task = TaskService.get_task_by_id(task_id)
    if not task:
        flash('Tarefa não encontrada!', 'error')
        return redirect(url_for('tasks.list_tasks'))
    return render_template('tasks/detail.html', task=task)