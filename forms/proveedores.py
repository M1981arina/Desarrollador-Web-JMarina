from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class ProveedorForm(FlaskForm):
    nombre = StringField('Nombre del proveedor', validators=[DataRequired(message='El nombre es obligatorio.'), Length(min=2, max=100, message='El nombre debe tener entre 2 y 100 caracteres.')])
    contacto = StringField('Persona de contacto', validators=[DataRequired(message='El contacto es obligatorio.'), Length(min=2, max=100, message='El contacto debe tener entre 2 y 100 caracteres.')])
    email = StringField('Correo electrónico', validators=[DataRequired(message='El correo es obligatorio.'), Email(message='Ingrese un correo válido.')])
    telefono = StringField('Teléfono', validators=[DataRequired(message='El teléfono es obligatorio.'), Length(min=10, max=15, message='El teléfono debe tener entre 10 y 15 caracteres.')])
    submit = SubmitField('Guardar')
