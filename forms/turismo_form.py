from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class TurismoForm(FlaskForm):
    lugar = StringField("Lugar turístico", validators=[DataRequired(), Length(max=100)])
    tipo = StringField("Tipo de atractivo", validators=[DataRequired(), Length(max=80)])
    submit = SubmitField("Guardar")
