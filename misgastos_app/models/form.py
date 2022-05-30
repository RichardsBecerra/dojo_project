from select import select
from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, IntegerField, TextAreaField, SubmitField

class ioForm (FlaskForm):
    mio = SelectField('Gasto o Ingreso', choices=[(0, 'Gasto'), (1, 'Ingreso')])
    mov_cid = SelectField('Categoria', choices=[])
    mov_iid = SelectField('Item', choices=[])
    mdate = DateField('Fecha')
    mamount = IntegerField('Monto')
    mov_tpid = SelectField('Forma de pago', choices=[])
    mcomment = TextAreaField('Comentario')