from selene import have, command
from selene.support.shared import browser
from qaguru_pageobjects.model import resource


class RegistrationPage:
    def __init__(self):
        self.state = browser.element('#state')
        pass

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
                have.size_greater_than_or_equal(3)
            )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_student_email(self, value):
        browser.element('#userEmail-wrapper #userEmail').type(value)
        return self

    class SelectStudentGender:
        @staticmethod
        def male():
            return browser.element('[name="gender"][value="Male"]+label').click()

    def fill_student_phone_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    class SelectHobbies:
        @staticmethod
        def reading():
            return browser.element('#hobbiesWrapper').all('.custom-control-label').element_by(have.text(
                'Reading')).click()

    def upload_student_photo(self, picture_name):
        browser.element('#uploadPicture').set_value(resource.path(picture_name))
        return self

    def fill_student_current_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
        return self

    def fill_state(self, name):
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(name)).click()
        return self

    def fill_city(self, name):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(name)).click()
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def should_have_registered(self, full_name, email, gender, phone_number, date_of_birth, subjects, hobbies,
                               picture, current_address, state_and_city):
        browser.element('[id=example-modal-sizes-title-lg]').should(
            have.text('Thanks for submitting the form')
        )

        browser.element('.table').all('td').even.should(
            have.texts(
                full_name,
                email,
                gender,
                phone_number,
                date_of_birth,
                subjects,
                hobbies,
                picture,
                current_address,
                state_and_city
            )
        )
        return self
