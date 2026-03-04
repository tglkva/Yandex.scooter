from selenium.webdriver.common.by import By


class FaqModuleLocators:

    FAQ_QUESTION_BUTTON_1 = (By.XPATH,"(//div[@id='accordion__heading-0'])") # Вопрос № 1 "Сколько это стоит? И как оплатить?"
    FAQ_QUESTION_BUTTON_2 = (By.XPATH,"(//div[@id='accordion__heading-1'])") # Вопрос № 2 "Хочу сразу несколько самокатов! Так можно?"
    FAQ_QUESTION_BUTTON_3 = (By.XPATH,"(//div[@id='accordion__heading-2'])") # Вопрос № 3 "Как рассчитывается время аренды?"
    FAQ_QUESTION_BUTTON_4 = (By.XPATH,"(//div[@id='accordion__heading-3'])") # Вопрос № 4 "Можно ли заказать самокат прямо на сегодня?"
    FAQ_QUESTION_BUTTON_5 = (By.XPATH,"(//div[@id='accordion__heading-4'])") # Вопрос № 5 "Можно ли продлить заказ или вернуть самокат раньше?"
    FAQ_QUESTION_BUTTON_6 = (By.XPATH,"(//div[@id='accordion__heading-5'])") # Вопрос № 6 "Вы привозите зарядку вместе с самокатом?"
    FAQ_QUESTION_BUTTON_7 = (By.XPATH,"(//div[@id='accordion__heading-6'])") # Вопрос № 7 "Можно ли отменить заказ?"
    FAQ_QUESTION_BUTTON_8 = (By.XPATH,"(//div[@id='accordion__heading-7'])") # Вопрос № 8 "Я жизу за МКАДом, привезёте?"

    FAQ_ANSWER_TEXT_1 = (By.XPATH, "//*[@id='accordion__panel-0']") # Ответ на вопрос № 1 
    FAQ_ANSWER_TEXT_2 = (By.XPATH, "//*[@id='accordion__panel-1']") # Ответ на вопрос № 2
    FAQ_ANSWER_TEXT_3 = (By.XPATH, "//*[@id='accordion__panel-2']") # Ответ на вопрос № 3
    FAQ_ANSWER_TEXT_4 = (By.XPATH, "//*[@id='accordion__panel-3']") # Ответ на вопрос № 4
    FAQ_ANSWER_TEXT_5 = (By.XPATH, "//*[@id='accordion__panel-4']") # Ответ на вопрос № 5
    FAQ_ANSWER_TEXT_6 = (By.XPATH, "//*[@id='accordion__panel-5']") # Ответ на вопрос № 6
    FAQ_ANSWER_TEXT_7 = (By.XPATH, "//*[@id='accordion__panel-6']") # Ответ на вопрос № 7
    FAQ_ANSWER_TEXT_8 = (By.XPATH, "//*[@id='accordion__panel-7']") # Ответ на вопрос № 8
