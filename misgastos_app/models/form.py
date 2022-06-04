from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, IntegerField, TextAreaField, HiddenField
from wtforms.validators import InputRequired

class ioForm (FlaskForm):
    mid = HiddenField()
    mio = SelectField('Gasto o Ingreso', choices=[(0, 'Gasto'), (1, 'Ingreso')], coerce=int, validators=[InputRequired('Debe seleccionar Gasto o Ingreso')])
    mov_uid = HiddenField()
    mov_cid = SelectField('Categoria', choices=[], coerce=int, validators=[InputRequired('Debe seleccionar una Categoría')])
    mov_iid = SelectField('Item', choices=[], coerce=int, validators=[InputRequired('Debe seleccionar un Item')])
    mdate = DateField('Fecha', validators=[InputRequired('Debe seleccionar una Fecha')])
    mamount = IntegerField('Monto', validators=[InputRequired('Debe ingresar un Monto')])
    mov_tpid = SelectField('Forma de Pago', choices=[], coerce=int, validators=[InputRequired('Debe seleccionar una Forma de Pago')])
    mcomment = TextAreaField('Comentario')