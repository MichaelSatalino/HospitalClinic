from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,HiddenField, SubmitField, StringField, PasswordField, SelectField, ValidationError, BooleanField, DateField
from wtforms.validators import DataRequired, Optional
from app.customWidget import ButtonField

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


""" def buildSignupForm(data):
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
    return SignupForm() """

class SelectLoginForm(FlaskForm):
    label = StringField("Select Login Portal")
    choice_a = ButtonField("doctor")
    choice_b = ButtonField("nurse")

""" class SignupAccTypeForm(FlaskForm):
    account_type = SelectField('Account Type', choices=['doctor', 'nurse'], validators=[DataRequired()])
    submit = SubmitField('Continue') """

class PatientSearchForm(FlaskForm):
    first_name = StringField('First name')
    last_name = StringField('Last name')
    submit = SubmitField('Search')
    
class AppointmentSearchForm(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d', default=date.today())
    doc_name = StringField('Doctor')
    submit = SubmitField('Search')

class SelectDoctorAppointmentForm(FlaskForm):
    doctor_name = StringField('Doctor')
    submit = SubmitField('Continue')
    
class SelectPatientAppointmentForm(FlaskForm):
    patient_name = StringField('Patient')
    submit = SubmitField('Continue')

class CreateAppointmentForm(FlaskForm):
    doctor_name = StringField('Doctor')
    submit = SubmitField('Search')

class MedicationSearchForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Search')

class MedicationForm(FlaskForm):
    emp_id = StringField('Medication_ID', validators=[DataRequired()])
    name = StringField('Medication_Name', validators=[DataRequired()])
    department = StringField('Generic', validators=[DataRequired()])
    position = StringField('Dosage', validators=[DataRequired()])
    submit = SubmitField('submit')


def pharmSignupForm(data):
    if data=='doctor':
         class SignupForm(FlaskForm):
            emp_id = StringField('Doctor Employee ID', validators=[DataRequired()])
            name = StringField('Name', validators=[DataRequired()])
            department = StringField('Department', validators=[DataRequired()])
            position = StringField('Position', validators=[DataRequired()])
            password = PasswordField('Password', validators=[DataRequired()])
            date = StringField('Date_Prescribed', validators=[DataRequired()])
            diagnosis = StringField('Current_diagnosis_severity', validators=[DataRequired()])
            amnt = StringField('refills', validators=[DataRequired()])
            submit = SubmitField('Sign up')
    else:
        class SignupForm(FlaskForm):
            emp_id = StringField('Pharmacy_ID', validators=[DataRequired()])
            name = StringField('name', validators=[DataRequired()])
            department = StringField('address', validators=[DataRequired()])
            submit = SubmitField('submit')
    return SignupForm()

class AddPrescriptionForm(FlaskForm):
    pharmacy_name =SelectField('Pharmacy Name', choices=[],validators=[DataRequired()])
    pharmacy_address =SelectField('Pharmacy Address', choices=[],validators=[DataRequired()], validate_choice=False)    
    
    medication_name = StringField('Medication Name', validators=[DataRequired()])
    dosage = SelectField("Medication Dosage", choices=[], validators=[DataRequired()], validate_choice=False)
    refills = StringField('Refills', validators=[DataRequired()])
    medication_id=HiddenField()
    submit = SubmitField('Add')



class AppointmentTypeForm(FlaskForm):
    admission_type = StringField('Admission Type')
    exam_type = StringField('Exam Type')
    submit = SubmitField('Create')

def BuildEditAppointmentForm(stat):
    class EditAppointmentForm(FlaskForm):
        status = SelectField('Status', choices=['cancelled', 'not started', 'waiting','in progress', 'completed'], default=stat)
        submit = SubmitField('Save')
    return EditAppointmentForm()
