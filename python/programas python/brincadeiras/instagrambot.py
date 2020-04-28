from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from pynput.keyboard import Key, Controller


driver = webdriver.Firefox()
keyboard = Controller()

login_link = 'https://www.instagram.com/accounts/login/?next=%2Fp%2FB-UmqA_g1kI%2F&source=desktop_nav'


def login():
    driver.get(login_link)
    usuario = 'mosermateus75'
    senha = 'Pitocaemissinha'
    sleep(1)
    login_input = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
    login_input.send_keys(usuario)
    senha_input = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
    senha_input.send_keys(senha)
    senha_input.send_keys(Keys.ENTER)


def comment(usuario):
    sleep(3)
    comment = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea')
    comment.click()
    sleep(3)
    keyboard.type(usuario)
    sleep(3)
    post_button = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/button')
    post_button.click()



login()
comment('@edudahah')
comment('@miriafelisbino')
comment('@mateus_moser555')
comment('@mr_imme')
comment('@maif_279')
comment('@markusimme')
