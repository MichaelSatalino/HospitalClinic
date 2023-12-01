from wtforms import StringField
from wtforms.widgets import html_params
from markupsafe import Markup

class ButtonWidget(object):
    input_type = 'submit'

    html_params = staticmethod(html_params)

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id',field.id)
        kwargs.setdefault('type',self.input_type)
        kwargs.setdefault('value',field.name)
        if 'value' not in kwargs:
            kwargs['value'] = field._value()

        html= ('<button {params}>{label}</button>'.format(
            params=self.html_params(name=field.name, **kwargs),
            label=field.label.text
        ))
        return Markup(html)

class ButtonField(StringField):
    widget = ButtonWidget()