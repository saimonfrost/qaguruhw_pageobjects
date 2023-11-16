import os

from selene import browser, have, be


def test_fill_all_form():
    browser.open('/')

    browser.element('#firstName').should(be.blank).type('Semen')
    browser.element('#lastName').should(be.blank).type('Fedorov')
    browser.element('#userEmail-wrapper #userEmail').should(be.blank).type('fedorovedorov@gmail.com')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').should(be.blank).type('8811656731')
    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__month-select"]').should(be.visible).element('option[value="10"]').click()
    browser.element('[class="react-datepicker__year-select"]').should(be.visible).element('option[value="2023"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--009"]').click()
    browser.element('#subjectsInput').should(be.blank).type('Ma').press_enter()
    browser.element('label[for=hobbies-checkbox-2]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('images/godot.png'))
    browser.element('#currentAddress').type('st.Pushkina, 10')
    browser.element('#state').click()
    browser.element('#react-select-3-input').should(be.blank).type('U').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').should(be.blank).type('A').press_enter()
    browser.element('#submit').click()

    browser.element('[class="table-responsive"]').all('td:nth-child(2)').should(
        have.texts('Semen Fedorov', 'fedorovedorov@gmail.com', 'Male', '8811656731', '09 November,2023',
                   'Maths', 'Reading', 'godot.png', 'st.Pushkina, 10', 'Uttar Pradesh Agra'))
