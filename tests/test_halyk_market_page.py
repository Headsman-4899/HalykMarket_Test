import re
import pytest
from time import sleep
from selenium import webdriver
from pages.halyk_market_page import HalykMarketPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.delete_all_cookies()
    driver.quit()


def test_halyk_market_search_product(driver):
    halyk_page = HalykMarketPage(driver)
    halyk_page.open()

    # Проверить, что заголовок страницы содержит "Halyk Market - Выгодные покупки в рассрочку".
    expected_title = "Halyk Market - Выгодные покупки в рассрочку"
    actual_title = halyk_page.get_title()
    assert expected_title == actual_title
    sleep(1)

    # Проверить, что есть результаты поиска.
    halyk_page.search_product("iPhone 14 Pro 128 Deep Purple")
    sleep(1)
    search_title_text = halyk_page.get_search_results_title()
    assert search_title_text == "По запросу «iPhone 14 Pro 128 Deep Purple» найдено"
    sleep(1)

    # Проверить, что название продукта соответствует "iPhone 14 Pro 128 Deep Purple".
    first_product_title = halyk_page.get_first_product_title()
    first_product_cost = halyk_page.get_first_product_cost()
    assert first_product_title == "Смартфон Apple iPhone 14 Pro 128Gb Deep Purple"
    sleep(1)

    # Проверить, что название продукта на странице соответствует "iPhone 14 Pro 128 Deep Purple".
    halyk_page.click_first_product()
    sleep(1)
    product_page_title = halyk_page.get_product_page_title()
    product_page_cost = halyk_page.get_product_page_cost()
    assert product_page_title == "Смартфон Apple iPhone 14 Pro 128Gb Deep Purple"
    sleep(1)

    # Проверить, что кнопка "Избранное" доступна для нажатия.
    halyk_page.add_to_favorites()
    sleep(1)
    halyk_page.goto_favorites_page()
    sleep(1)

    # Проверить, что продукт успешно добавлен в избранное.
    assert halyk_page.check_favorite_product_is_added() == True

    # Убедиться, что название товара в избранном совпадает с названием товара на странице карточки товара.
    favorite_product_in_favorite_page_title = halyk_page.get_favorite_product_title()
    favorite_product_cost = halyk_page.get_favorite_product_cost()
    assert favorite_product_in_favorite_page_title == product_page_title
    sleep(1)

    # Перейти на страницу карточки товара.
    halyk_page.goto_product_page()
    sleep(q)

    # Убедиться, что цена товара в поиске, избранном и карточке товара одинакова.
    first_product_cost_numbers = re.sub(r'\D', '', first_product_cost)
    product_page_cost_numbers = re.sub(r'\D', '', product_page_cost)
    favorite_product_in_favorite_page_cost_numbers = re.sub(r'\D', '', favorite_product_cost)
    assert first_product_cost_numbers == product_page_cost_numbers == favorite_product_in_favorite_page_cost_numbers

