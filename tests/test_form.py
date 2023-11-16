import os

from selene import browser, have, be
import tests
from qaguru_pageobjects.model.pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.select_student_gender = RegistrationPage.SelectStudentGender
    registration_page.open()

    '''
    WHEN
    '''

    registration_page.fill_first_name('Semen')
    registration_page.fill_last_name('Fedorov')
    registration_page.fill_student_email('fedorovedorov@gmail.com')
    registration_page.select_student_gender.male()
    registration_page.fill_student_phone_number('8811656731')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys('November')
    browser.element('.react-datepicker__year-select').type('2023')
    browser.element('.react-datepicker__day--009').click()

    browser.element('#subjectsInput').should(be.blank).type('Maths').press_enter()
    browser.element('#hobbiesWrapper').all('.custom-control-label').element_by(have.text('Reading')).click()

    browser.element('#uploadPicture').send_keys(os.path.abspath(os.path.join(
        os.path.dirname(tests.__file__), 'images/godot.png')))

    browser.element('#currentAddress').type('st.Pushkina, 10')

    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('Uttar Pradesh')
    ).click()

    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('Agra')
    ).click()
    browser.element('#submit').click()

    '''
    THEN
    '''
    browser.element('[id=example-modal-sizes-title-lg]').should(
        have.text('Thanks for submitting the form')
    )

    browser.element('.table').all('td').even.should(
        have.texts(
            'Semen Fedorov',
            'fedorovedorov@gmail.com',
            'Male',
            '8811656731',
            '09 November,2023',
            'Maths',
            'Reading',
            'godot.png',
            'st.Pushkina, 10',
            'Uttar Pradesh Agra'
        )
    )
