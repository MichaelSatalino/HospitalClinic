from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, StringField, PasswordField, SelectField, ValidationError, BooleanField, DateField
from wtforms.validators import DataRequired, Optional

def buildLoginForm(data):
    if data=='doctor':
        class LoginForm(FlaskForm):
            emp_id = StringField('Doctor Employee ID', validators=[DataRequired()])
            password = PasswordField('Password', validators=[DataRequired()])
            submit = SubmitField('Log in')
    else:
        class LoginForm(FlaskForm):
            emp_id = StringField('Nurse Employee ID', validators=[DataRequired()])
            password = PasswordField('Password', validators=[DataRequired()])
            submit = SubmitField('Log in')
    return LoginForm()


def buildSignupForm(data):
    if data=='doctor':
        class SignupForm(FlaskForm):
            emp_id = StringField('Doctor Employee ID', validators=[DataRequired()])
            name = StringField('Name', validators=[DataRequired()])
            department = StringField('Department', validators=[DataRequired()])
            position = StringField('Position', validators=[DataRequired()])
            password = PasswordField('Password', validators=[DataRequired()])
            submit = SubmitField('Sign up')
    else:
        class SignupForm(FlaskForm):
            emp_id = StringField('Nurse Employee ID', validators=[DataRequired()])
            name = StringField('Name', validators=[DataRequired()])
            department = StringField('Department', validators=[DataRequired()])
            position = StringField('Position', validators=[DataRequired()])
            password = PasswordField('Password', validators=[DataRequired()])
            submit = SubmitField('Log in')
    return SignupForm()

class SelectLoginForm(FlaskForm):
    account_type = SelectField('Account Type', choices=['doctor', 'nurse'], validators=[DataRequired()])
    submit = SubmitField('Continue')

class SignupAccTypeForm(FlaskForm):
    account_type = SelectField('Account Type', choices=['doctor', 'nurse'], validators=[DataRequired()])
    submit = SubmitField('Continue')

class PatientSearchForm(FlaskForm):
    first_name = StringField('First name')
    last_name = StringField('Last name')
    submit = SubmitField('Search')

class CreateAppointmentDoctorForm(FlaskForm):
    doctor_name = StringField('Doctor')
    submit = SubmitField('Search')
