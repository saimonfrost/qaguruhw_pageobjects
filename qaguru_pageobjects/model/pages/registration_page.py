from selene import have
from selene.support.shared import browser
from qaguru_pageobjects.model import resource
from qaguru_pageobjects.data.users import User


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail-wrapper #userEmail')
        self.phone_number = browser.element('#userNumber')
        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.element('#hobbiesWrapper').all('.custom-control-label')
        self.upload_photo = browser.element('#uploadPicture')
        self.currentAddress = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.submit_button = browser.element('#submit')

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)

    def fill_last_name(self, value):
        self.last_name.type(value)

    def fill_email(self, value):
        self.email.type(value)

    def select_gender(self, value):
        browser.element(f'[name="gender"][value={value}]+label').click()
        return self

    def fill_phone_number(self, value):
        self.phone_number.type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
        return self

    def fill_subjects(self, value):
        self.subjects.type(value).press_enter()

    def select_hobbies(self, name):
        self.hobbies.element_by(have.text(name)).click()

    def upload_photos(self, picture_name):
        self.upload_photo.set_value(resource.path(picture_name))

    def fill_current_address(self, value):
        self.currentAddress.type(value)

    def fill_state(self, name):
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(name)).click()
        return self

    def fill_city(self, name):
        self.city.click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(name)).click()
        return self

    def register(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.select_gender(user.gender)
        self.fill_phone_number(user.phone_number)
        self.fill_date_of_birth(user.year_of_birth, user.month_of_birth, user.day_of_birth)
        self.fill_subjects(user.subjects)
        self.select_hobbies(user.hobbies)
        self.upload_photos(user.picture_name)
        self.fill_current_address(user.current_address)
        self.fill_state(user.state)
        self.fill_city(user.city)
        self.submit_button.click()

    def should_have_registered(self, user):
        browser.element('[id=example-modal-sizes-title-lg]').should(
            have.text('Thanks for submitting the form')
        )

        browser.element('.table').all('td').even.should(
            have.texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender,
                user.phone_number,
                f'{user.day_of_birth} {user.month_of_birth},{user.year_of_birth}',
                user.subjects,
                user.hobbies,
                user.picture_name,
                user.current_address,
                f'{user.state} {user.city}'
            )
        )
        return self
