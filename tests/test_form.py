from qaguru_pageobjects.model.pages.registration_page import RegistrationPage
import allure


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.select_student_gender = RegistrationPage.SelectStudentGender
    registration_page.select_hobbies = RegistrationPage.SelectHobbies
    with allure.step("Открыть страницу регистрации студента"):
        registration_page.open()

    '''
    WHEN
    '''
    with allure.step("Заполнить информацию о студенте"):
        registration_page.fill_first_name('Semen')
        registration_page.fill_last_name('Fedorov')
        registration_page.fill_student_email('fedorovedorov@gmail.com')
        registration_page.select_student_gender.male()
        registration_page.fill_student_phone_number('8811656731')
        registration_page.fill_date_of_birth('2023', 'November', '09')
        registration_page.fill_subjects('Maths')
        registration_page.select_hobbies.reading()
        registration_page.upload_student_photo('godot.png')
        registration_page.fill_student_current_address('st.Bakery, 10')
        registration_page.fill_state('Uttar Pradesh')
        registration_page.fill_city('Agra')
        registration_page.submit()
        registration_page.should_have_registered('Semen Fedorov', 'fedorovedorov@gmail.com',
                                                 'Male', '8811656731', '09 November,2023',
                                                 'Maths', 'Reading', 'godot.png',
                                                 'st.Bakery, 10', 'Uttar Pradesh Agra')
