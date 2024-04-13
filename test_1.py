import logging
from conftest import testdata
from testpage import OperationHelper

def test_step1(browsser):
    logging.info("Test 1 Starting")
    testpage = OperationHelper(browsser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['passwd'])
    testpage.click_login_button()
    assert testpage.check_login_success(), "Login failed"
    testpage.create_post(testdata['title'], testdata['description'], testdata['content'])
    testpage.test_contact_us()
