from flask import render_template, url_for, redirect, request
from app import app, db
from app.forms import CreateEmployeeForm
from app.models import Employee


@app.route('/', methods=['GET', 'POST'])
def employees():
    employees = Employee.query.all()
    return render_template("employees.html",
                           title='Employee',
                           employees=employees)


@app.route('/employee/new', methods=['GET', 'POST'])
def create_employee():
    form = CreateEmployeeForm()
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        passport = form.passport.data
        education = form.education.data
        salary = form.salary.data
        experience = form.experience.data
        employee = Employee(name=name, surname=surname, passport=passport, education=education, salary=salary, experience=experience)
        db.session.add(employee)
        db.session.commit()
        return redirect(url_for('employees'))
    return render_template("create-employee.html", title='Create Employee', form=form)


@app.route('/employees/<int:id>', methods=['GET', 'POST'])
def employee_details(id):
    employee = Employee.query.get(id)
    return render_template("employee_details.html",
                           title='Employee Details',
                           employee=employee)


@app.route('/employees/<int:id>/delete', methods=['GET', 'POST'])
def employee_delete(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for('employees'))


@app.route('/employees/<int:id>/edit', methods=['GET', 'POST'])
def employee_edit(id):
    employee = Employee.query.get(id)
    form = CreateEmployeeForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            employee.name = form.name.data
            employee.surname = form.surname.data
            employee.passport = form.passport.data
            employee.education = form.education.data
            employee.salary = form.salary.data
            employee.experience = form.experience.data
            db.session.commit()
            return redirect(url_for('employee_details', id=employee.id))
        else:
            return redirect(url_for('employees'))
    elif request.method == 'GET':
        form.name.data = employee.name
        form.surname.data = employee.surname
        form.passport.data = employee.passport
        form.education.data = employee.education
        form.salary.data = employee.salary
        form.experience.data = employee.experience
    return render_template('employee_edit.html', title='Employee Edit', form=form)
