from behave import step

@step('llenamos el campo correo con "{value}"')
def step_impl(context, value):
    context.edicion_page.llenamos_campo_correo(value)