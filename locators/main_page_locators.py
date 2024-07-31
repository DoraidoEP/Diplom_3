from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка "Личный кабинет" в шапке сайта
    ACCOUNT_BUTTON = By.XPATH, './/*[@href = "/account"]'
    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = By.XPATH, './/p[text() = "Конструктор"]'
    # Кнопка "Лента заказов"
    ORDER_LIST_BUTTON = By.XPATH, './/p[text() = "Лента Заказов"]'
    # Кнопка "Оформить заказ"
    ORDER_BUTTON = By.XPATH, './/button[text() = "Оформить заказ"]'
    # Заголовок "Соберите бургер"
    PACK_BURGER = By.XPATH, './/h1[text() = "Соберите бургер"]'
    # Название булки "Флюоресцентная булка"
    INGREDIENT_BUTTON = By.XPATH, './/p[text() = "Флюоресцентная булка R2-D3"]'
    # Окно "Детали ингредиента"
    INGREDIENT_MODAL_WINDOW = By.XPATH, './/h2[text() = "Детали ингредиента"]'
    # Кнопка закрыть окно "Детали ингредиента"
    INGREDIENT_MODAL_CLOSE = By.XPATH, './/button[contains(@class, "modal__close")]'
    # Счетчик ингредиентов
    INGREDIENT_COUNT = By.XPATH, './/p[contains(@class, "counter_counter__num__3nue1")]'
    # Корзина
    BASKET = By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]'
    # Идентификатор заказа"
    ORDER_ID = By.XPATH, './/p[text() = "идентификатор заказа"]'
    # Номер заказа
    ORDER_NUMBER = By.XPATH, './/h2[contains(@class, "Modal_modal__title_shadow")]'
    # Оверлей загрузки
    OVERLAY = By.CSS_SELECTOR, '.Modal_modal__loading__3534A'