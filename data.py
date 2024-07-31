class TestData:
    user_data = {
        'name': 'Eduard',
        'email': 'Doraido_Pavlov@yandex.ru',
        'password': 'Doraido_123'
    }


class DataUrl:
    STELLAR_BURGERS = 'https://stellarburgers.nomoreparties.site/'
    LOGIN_PAGE = f'{STELLAR_BURGERS}login'
    RECOVERY_PAGE = f'{STELLAR_BURGERS}forgot-password'
    RESET_PAGE = f'{STELLAR_BURGERS}reset-password'
    ORDER_LIST_PAGE = f'{STELLAR_BURGERS}feed'
    HISTORY_ORDER_PAGE = f'{STELLAR_BURGERS}account/order-history'


class TextAnswer:
    ingredient_modal_close = 'Соберите бургер'
    ingredient_modal_open = 'Детали ингредиента'
    ingredient_count = '2'
