from behave import *

import time

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    # time.sleep(1000)
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False