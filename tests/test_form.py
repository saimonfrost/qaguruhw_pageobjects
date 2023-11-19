from qaguru_pageobjects.model.pages.registration_page import RegistrationPage
from qaguru_pageobjects.data import users


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register(users.student)
    registration_page.should_have_registered(users.student)
