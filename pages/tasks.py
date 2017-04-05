import allure
import pytest
from selene.api import *
from selene.bys import by_link_text

tasks = browser.all("#todo-list>li")


def visit():
    browser.visit('http://todomvc4tasj.herokuapp.com/')


@allure.step
def filter_active():
    browser.element(by_link_text("Active")).click()


@allure.step
def filter_completed():
    browser.element(by_link_text("Completed")).click()


@allure.step
def filter_all():
    browser.element(by_link_text("All")).click()


@allure.step
def add(*task_texts):
    for text in task_texts:
        browser.element("#new-todo").assure(be.enabled).set_value(text).press_enter()


@allure.step
def toggle(task_text):
    tasks.element_by(have.exact_text(task_text)).element(".toggle").click()


@allure.step
def assert_tasks(*task_texts):
    tasks.filtered_by(be.visible).should(have.exact_texts(*task_texts))


@allure.step
def assert_no_tasks():
    tasks.filtered_by(be.visible).assure(be.empty)


@allure.step
def toggle_all():
    browser.element("#toggle-all").click()


@allure.step
def assert_items_left(count):
    browser.element("#todo-count>strong").should(have.exact_text(str(count)))



@allure.step
def clear_completed():
    browser.element("#clear-completed").click()


@allure.step
def delete(task_text):
    tasks.element_by(have.exact_text(task_text)).hover().element(".destroy").click()


@allure.step
def start_editing(old_task_text, new_task_text):
    tasks.element_by(have.exact_text(old_task_text)).double_click()
    return tasks.element_by(have.css_class("editing")).element(".edit").set_value(new_task_text)


@allure.step
def edit(old_task_text, new_task_text):
    start_editing(old_task_text, new_task_text).press_enter()


@allure.step
def cancel_edit(old_task_text, new_task_text):
    start_editing(old_task_text, new_task_text).press_escape()
