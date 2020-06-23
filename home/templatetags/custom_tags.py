from django import template
register = template.Library()

@register.simple_tag
def any_function(num1,num2):
    return num1+num2


@register.filter()
def check_permission(user, permission):
    test = user.user_permissions.all()
    if user.user_permissions.filter(codename = permission).exists():
        return True
    return False
