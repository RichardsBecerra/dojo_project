from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, IntegerField, TextAreaField, HiddenField
from wtforms.validators import InputRequired

class ioForm (FlaskForm):
    mio = SelectField('Gasto o Ingreso', choices=[(0, 'Gasto'), (1, 'Ingreso')], validators=[InputRequired('Debe seleccionar Gasto o Ingreso')])
    mov_uid = HiddenField()
    mov_cid = SelectField('Categoria', choices=[], validators=[InputRequired('Debe seleccionar una Categoría')])
    mov_iid = SelectField('Item', choices=[], validators=[InputRequired('Debe seleccionar un Item')])
    mdate = DateField('Fecha', validators=[InputRequired('Debe seleccionar una Fecha')])
    mamount = IntegerField('Monto', validators=[InputRequired('Debe ingresar un Monto')])
    mov_tpid = SelectField('Forma de Pago', choices=[], validators=[InputRequired('Debe seleccionar una Forma de Pago')])
    mcomment = TextAreaField('Comentario')