from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class FacturaForm(FlaskForm):
    cliente = StringField('Cliente', validators=[DataRequired(message='El cliente es obligatorio.'), ])
    subtotal = FloatField('Subtotal', validators=[DataRequired(message='El subtotal es obligatorio.'), NumberRange(min=0.01, message='El subtotal debe ser mayor a 0.')])
    iva = FloatField('IVA', validators=[DataRequired(message='El IVA es obligatorio.'), NumberRange(min=0, message='El IVA no puede ser negativo.')])
    total = FloatField('Total', validators=[DataRequired(message='El total es obligatorio.'), NumberRange(min=0.01, message='El total debe ser mayor a 0.')])
    estado = SelectField('Estado', choices=[('Pagada', 'Pagada'), ('Pendiente', 'Pendiente'), ('Anulada', 'Anulada')], validators=[DataRequired(message='El estado es obligatorio.')])
    submit = SubmitField('Guardar')
