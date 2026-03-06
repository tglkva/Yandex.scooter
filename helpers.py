from all_locators.faq_module import FaqModuleLocators
from all_locators.main_page import MainPageLocators
from all_locators.order_page import OrderPageLocators

def get_faq_pairs():

    pairs = [
    ("Вопрос 1", FaqModuleLocators.FAQ_QUESTION_BUTTON_1, FaqModuleLocators.FAQ_ANSWER_TEXT_1),
    ("Вопрос 2", FaqModuleLocators.FAQ_QUESTION_BUTTON_2, FaqModuleLocators.FAQ_ANSWER_TEXT_2),
    ("Вопрос 3", FaqModuleLocators.FAQ_QUESTION_BUTTON_3, FaqModuleLocators.FAQ_ANSWER_TEXT_3),
    ("Вопрос 4", FaqModuleLocators.FAQ_QUESTION_BUTTON_4, FaqModuleLocators.FAQ_ANSWER_TEXT_4),
    ("Вопрос 5", FaqModuleLocators.FAQ_QUESTION_BUTTON_5, FaqModuleLocators.FAQ_ANSWER_TEXT_5),
    ("Вопрос 6", FaqModuleLocators.FAQ_QUESTION_BUTTON_6, FaqModuleLocators.FAQ_ANSWER_TEXT_6),
    ("Вопрос 7", FaqModuleLocators.FAQ_QUESTION_BUTTON_7, FaqModuleLocators.FAQ_ANSWER_TEXT_7),
    ("Вопрос 8", FaqModuleLocators.FAQ_QUESTION_BUTTON_8, FaqModuleLocators.FAQ_ANSWER_TEXT_8)
    ]
    return pairs

test_data = [

    {
        "name": "Анастасия",
        "surname": "Иванова",
        "address": "улица Гастелло",
        "metro_station_name": "Сокольники",
        "metro_station_locator": OrderPageLocators.SOKOLNIKI_STATION,
        "phone_number": "89161234567",
        "date": "суббота, 14-е марта 2026 г.",
        "button_locator": MainPageLocators.ORDER_BUTTON_ABOVE,
        "button_name": "верхняя кнопка"
    },

    {
        "name": "Елизавета",
        "surname": "Куприна",
        "address": "Проспект Мира",
        "metro_station_name": "Проспект Мира",
        "metro_station_locator": OrderPageLocators.PROSPEKT_MIRA_STATION,
        "phone_number": "89267654321",
        "date": "среда, 25-е марта 2026 г.",
        "button_locator": MainPageLocators.ORDER_BUTTON_BELOW,
        "button_name": "нижняя кнопка"
    }
]

