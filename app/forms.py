from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class TaskForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(min=1, max=100)])
    description = TextAreaField('Descrição', validators=[Length(max=500)])
    completed = BooleanField('Concluída')
    submit = SubmitField('Salvar')