from behave import given, step


@given("navegamos a la aplicacion de testleaf")
def step_impl(context):
    context.driver.get("http://testleaf.herokuapp.com/home.html")

@step("damos click en el modulo edicion")
def step_impl(context):
    context.home_page.click_modulo_edicion()
