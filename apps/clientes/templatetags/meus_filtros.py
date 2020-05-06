from django import template

register = template.Library()

# Essa função serve para que seja possível manipular um input através da inserção de uma nova classe
@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})