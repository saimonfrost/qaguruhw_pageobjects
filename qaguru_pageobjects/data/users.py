import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    day_of_birth: str
    month_of_birth: str
    year_of_birth: str
    subjects: str
    hobbies: str
    picture_name: str
    current_address: str
    state: str
    city: str


student = User(first_name="Semen", last_name="Fedorov", email="fedorovedorov@gmail.com",
               gender="Male", phone_number="8811656731", day_of_birth="09", month_of_birth="November",
               year_of_birth="2023", subjects="Maths", hobbies="Reading", picture_name='godot.png',
               current_address="st.Bakery, 10", state="Uttar Pradesh", city="Agra")
