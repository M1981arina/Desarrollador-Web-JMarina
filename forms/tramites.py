from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class TramiteForm(FlaskForm):
    nombre = StringField(
        "Nombre completo",
        validators=[DataRequired(message="El nombre es obligatorio."), Length(min=2, max=100)],
    )
    email = StringField(
        "Correo electrónico",
        validators=[DataRequired(message="El correo es obligatorio."), Email(message="Ingrese un correo válido.")],
    )
    tipo = SelectField(
        "Trámite solicitado",
        choices=[
            ("", "Seleccione un trámite..."),
            ("Permiso de construcción", "Permiso de construcción"),
            ("Certificado municipal", "Certificado municipal"),
            ("Licencia comercial", "Licencia comercial"),
        ],
        validators=[DataRequired(message="Seleccione un trámite.")],
    )
    detalle = TextAreaField(
        "Detalle de la solicitud",
        validators=[DataRequired(message="El detalle es obligatorio."), Length(min=10, max=500)],
    )
    submit = SubmitField("Enviar solicitud")
