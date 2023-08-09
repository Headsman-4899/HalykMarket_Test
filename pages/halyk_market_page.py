from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HalykMarketPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.halykmarket.kz"

    def open(self):
        self.driver.get(self.url)

    def get_title(self):
        return self.driver.title

    def search_product(self, query):
        search_input = self.driver.find_element(By.XPATH, "//div[@class='app-toolbar']//input")
        search_input.send_keys(query + Keys.ENTER)

    def get_search_results_title(self):
        return self.driver.find_element(By.XPATH, "//h1[@class='category-page-title']").text

    def get_first_product_title(self):
        first_product = self.driver.find_element(By.XPATH, "//div[@class='category-page-products']/div[1]")
        return first_product.get_attribute('title')

    def get_first_product_cost(self):
        return self.driver.find_element(By.XPATH,"//div[@class='category-page-products']/div[1]//div[@class='product-card-content']//div[@class='product-card-pay']/span").text

    def click_first_product(self):
        first_product = self.driver.find_element(By.XPATH, "//div[@class='category-page-products']/div[1]")
        first_product.click()

    def get_product_page_title(self):
        return self.driver.find_element(By.XPATH, "//h1[@class='desc-name']").text

    def get_product_page_cost(self):
        return self.driver.find_element(By.XPATH, "//div[@class='product']//div[@class='product-desc']/section/div[@class='desc-price-wrap']/div/div[2]").text

    def add_to_favorites(self):
        is_favorite_button = self.driver.find_element(By.XPATH, "//button[@class='btn product-buttons-favorite filled giant']")
        is_favorite_button.click()

    def goto_favorites_page(self):
        favorite_page_button = self.driver.find_element(By.XPATH, "//div[@class='app-toolbar']//a[@title='Перейти в раздел избранное']")
        favorite_page_button.click()

    def check_favorite_product_is_added(self):
        favorite_product_in_favorite_page = self.driver.find_element(By.XPATH,"//main//div[@class='favorite-product'][1]/div")
        return favorite_product_in_favorite_page.is_displayed()

    def goto_product_page(self):
        favorite_product_in_favorite_page = self.driver.find_element(By.XPATH,"//main//div[@class='favorite-product'][1]/div")
        favorite_product_in_favorite_page.click()

    def get_favorite_product_title(self):
        return self.driver.find_element(By.XPATH, "//main//div[@class='favorite-product'][1]/div//div[@class='product-card-content']/div[1]").text

    def get_favorite_product_cost(self):
        return self.driver.find_element(By.XPATH,"//main//div[@class='favorite-product'][1]//div[@class='product-card-content']/div[3]/span").text
