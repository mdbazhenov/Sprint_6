from selenium.webdriver.common.by import By

class CookieBar:
    ACCEPT_COOKIE = By.ID, "rcc-confirm-button"

class OrderButtonLocators:
    BUTTON_TO_ORDER_TOP = By.XPATH, ".//button[@class='Button_Button__ra12g']"
    BUTTON_TO_ORDER_CENTER = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"

class OrderFormLocators1:
    FIELD_NAME = By.XPATH, ".//input[@placeholder='* Имя']"
    FIELD_LAST_NAME = By.XPATH, ".//input[@placeholder='* Фамилия']"
    FIELD_ADDRESS = By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"
    FIELD_METRO = By.XPATH, ".//input[@placeholder='* Станция метро']"
    METRO_CHERKIZOVSKAYA = By.XPATH, ".//*[contains(text(), 'Черкизовская')]"
    METRO_SOKOLNIKI = By.XPATH, ".//*[contains(text(), 'Сокольники')]"
    FIELD_PHONE = By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"
    BUTTON_NEXT = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"

class OrderFormLocators2:
    TITLE_ABOUT_RENT = By.XPATH, ".//*[@class='Order_Header__BZXOb']"
    FIELD_DATA_ORDER = By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"
    CALENDAR_DATA_30 = By.XPATH, ".//*[@class='react-datepicker__day react-datepicker__day--030']"
    CALENDAR_DATA_31 = By.XPATH, ".//*[@class='react-datepicker__day react-datepicker__day--031']"
    FIELD_RENTAL_PERIOD = By.XPATH, ".//*[@class='Dropdown-placeholder']"
    RENT_1_DAY = By.XPATH, ".//*[contains(text(), 'сутки')]"
    RENT_3_DAYS = By.XPATH, ".//*[contains(text(), 'трое суток')]"
    CHECKBOX_BLACK_COLOR = By.XPATH, ".//*[contains(@id, 'black')]"
    CHECKBOX_GREY_COLOR = By.XPATH, ".//*[contains(@id, 'grey')]"
    FIELD_COMMENT_FOR_COURIER = By.XPATH, ".//input[@placeholder='Комментарий для курьера']"
    BUTTON_TO_ORDER_IN_FORM = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    DELIVERY_DATE_TOMORROW = By.XPATH, "//div[contains(@class, 'today')]/following-sibling::div[1]"

class OrderPopUpLocators:
    BUTTON_YES_ORDER = By.XPATH, ".//*[contains(text(), 'Да')]"
    POP_UP_WINDOW_SUCCESSFUL_ORDER = By.XPATH, ".//*[contains(text(), 'Заказ оформлен')]"
    BUTTON_VIEW_STATUS = By.XPATH, ".//*[contains(text(), 'Посмотреть статус')]"