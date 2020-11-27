from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Regexp
from app.models import Employee


class CreateEmployeeForm(FlaskForm):
    name = StringField('Name',
                           validators=[Length(min=4, max=25,
                           message='Це поле має бути довжиною між 4 та 25 символів'),
                           DataRequired(message='Це поле обовязкове'), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Name must have only letters, numbers, dots or underscores')])
    surname = StringField('Surname',
                           validators=[Length(min=4, max=25,
                           message='Це поле має бути довжиною між 4 та 25 символів'),
                           DataRequired(message='Це поле обовязкове'), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Surname must have only letters, numbers, dots or underscores')])
    passport = StringField('Passport',
                           validators=[Length(min=8, max=8,
                           message='Це поле має бути довжиною 8 символів'),
                           DataRequired(message='Це поле обовязкове')])
    education = StringField('Education',
                           validators=[Length(max=100,
                                              message='Це поле має бути довжиною не більше 100 символів'),
                                       DataRequired(message='Це поле обовязкове')])
    salary = StringField('Salary',
                           validators=[Length(max=100,
                                              message='Це поле має бути довжиною не більше 100 символів'),
                                       DataRequired(message='Це поле обовязкове')])
    experience = StringField('experience',
                           validators=[Length(max=100,
                                              message='Це поле має бути довжиною не більше 100 символів'),
                                       DataRequired(message='Це поле обовязкове')])
