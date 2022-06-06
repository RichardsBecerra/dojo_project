from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, IntegerField, TextAreaField, HiddenField, StringField
from wtforms.validators import InputRequired, Length

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

class ItemForm (FlaskForm):
    iid = HiddenField()
    iname = StringField('Nombre', validators=[InputRequired('Debe ingresar un Nombre'), Length(min=3, message='Nombre min 3 letras')])
    iio = HiddenField()
    itm_cid = HiddenField()
    itm_cname = HiddenField()
    itm_uid = HiddenField()