from faker import Faker

faker = Faker()

BASE_URL = "https://stellarburgers.education-services.ru"
API_URL = "https://stellarburgers.nomoreparties.site/api"

DEFAULT_PASSWORD = "Qwerty123!"


def generate_user_payload():
    return {
        "email": faker.email(),
        "password": DEFAULT_PASSWORD,
        "name": faker.first_name(),
    }
