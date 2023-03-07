import datetime
import time
from util import read
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By


class JingDong:
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    time_to_buy = '2023-03-07 16:55:00.00000000'
    main_page_url = 'https://www.jd.com/'
    cart_page_url = 'https://cart.jd.com/cart_index/'

    def __init__(self, t=time_to_buy):
        self.time_to_buy = t

    def buy(self):
        edge_driver = webdriver.Edge()

        edge_driver.get(self.main_page_url)
        edge_driver.maximize_window()
        time.sleep(3)

        edge_driver.find_element(By.LINK_TEXT, '你好，请登录').click()
        print('请尽快扫码登录')
        time.sleep(10)

        edge_driver.get(self.cart_page_url)



        read.confirm()

        while True:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            print(now)

            if now >= self.time_to_buy:
                while True:
                    try:
                        if edge_driver.find_element(By.LINK_TEXT, '去结算'):
                            edge_driver.find_element(By.LINK_TEXT, '去结算').click()
                            print('成功锁定商品')
                            break
                    except NoSuchElementException:
                        pass

                while True:
                    try:
                        if edge_driver.find_element(By.ID, 'order-submit'):
                            edge_driver.find_element(By.ID, 'order-submit').click()
                            print('成功提交订单')
                            break
                    except NoSuchElementException:
                        pass
                    except StaleElementReferenceException:
                        break
                break

        print('购买结束，按任意键退出程序')
        input()
