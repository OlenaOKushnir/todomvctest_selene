import atexit

import pytest
from selene.api import *
from subprocess import call

from pages import tasks

class TestTodoMVC(object):
    @classmethod
    def teardown(cls):
        browser.driver().execute_script("localStorage.clear()")

    @classmethod
    def teardown_class(cls):
        def allure():
            call(['allure', 'generate report'])

        atexit.register(allure)

    @pytest.allure.CRITICAL
    def test_tasks_common_flow(self):
        tasks.visit()

        tasks.add("a")
        tasks.toggle("a")
        tasks.assert_tasks("a")

        tasks.filter_active()
        tasks.assert_no_tasks()

        tasks.add("b")
        tasks.assert_tasks("b")

        tasks.toggle_all()
        tasks.assert_no_tasks()

        tasks.filter_completed()
        tasks.assert_tasks("a", "b")

        tasks.toggle("a")
        tasks.assert_items_left(1)
        tasks.assert_tasks("b")

        tasks.clear_completed()
        tasks.assert_no_tasks()

        tasks.filter_all()
        tasks.assert_tasks("a")

        tasks.delete("a")
        tasks.assert_no_tasks()

    @pytest.allure.MINOR
    def test_edit_at_all(self):
        # given - create task

        tasks.visit()
        tasks.add("a")

        tasks.edit("a", "a edited")
        tasks.assert_tasks("a edited")
        tasks.assert_items_left(1)

    @pytest.allure.MINOR
    def test_cancel_edit_at_active(self):
        # given - create task
        tasks.visit()
        tasks.add("a")
        tasks.filter_active()

        tasks.cancel_edit("a", "a edited")
        tasks.assert_tasks("a")
        tasks.assert_items_left(1)
