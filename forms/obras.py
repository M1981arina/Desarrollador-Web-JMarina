from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange, Optional


class ObraForm(FlaskForm):
    nombre = StringField(
        "Nombre de la obra",
        validators=[
            DataRequired(message="El nombre de la obra es obligatorio."),
            Length(min=2, max=100, message="El nombre debe tener entre 2 y 100 caracteres."),
        ],
    )
    tipo = SelectField(
        "Tipo de obra",
        choices=[
            ("", "Seleccione un tipo..."),
            ("Vial", "Vial"),
            ("Parque", "Parque"),
            ("Educación", "Educación"),
            ("Salud", "Salud"),
            ("Turismo", "Turismo"),
            ("Servicios", "Servicios básicos"),
        ],
        validators=[DataRequired(message="El tipo de obra es obligatorio.")],
    )
    descripcion = TextAreaField(
        "Descripción detallada",
        validators=[
            DataRequired(message="La descripción es obligatoria."),
            Length(min=10, max=500, message="La descripción debe tener entre 10 y 500 caracteres."),
        ],
    )
    ubicacion = StringField(
        "Ubicación",
        validators=[Optional(), Length(max=150, message="La ubicación no puede superar 150 caracteres.")],
    )
    presupuesto = FloatField(
        "Presupuesto aproximado",
        validators=[Optional(), NumberRange(min=0, message="El presupuesto no puede ser negativo.")],
    )
    submit = SubmitField("Registrar obra")
