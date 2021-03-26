from django import template

register = template.Library()


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})

@register.filter(name='can_delete')
def can_delete(user, session):    
    return user == session.owner

@register.filter(name='is_member')
def is_member(user, session): 
    return len(session.riders.filter(pk=user.id)) > 0