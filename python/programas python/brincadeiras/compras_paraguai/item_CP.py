from selenium import webdriver
from selenium.webdriver.firefox.options import Options


option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)

class Item():
    def __init__(self,name,link,price=None):
        self.price = price
        self.name = name
        self.link = link
    

    def getprice(self):
        driver.get(self.link)
        price = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/div/div[3]/div[3]/div/div[3]/div[1]/span').text
        self.price = price[3:]
        self.price = self.price.replace('.','')
        self.price = self.price.replace(',','.')
        print(self.name[0:25] + ':\t' + self.price)
        return self.price

    def price(self):
        print(self.price)
        return self.price


class Kit():
    def __init__(self,*itens):
        self.price = 0.0
        self.itens = itens

    def get_price(self):
        for item in self.itens:
            print(self.item)
        print(self.price)
        return(self.price)





#MAIN
ram = Item('ram 8gb/3200','https://www.comprasparaguai.com.br/memoria-kingston-hyperx-fury-ddr4-8gb-3200mhz_26738/').getprice()
cpu = Item('ryzen 3600','https://www.comprasparaguai.com.br/processador-amd-ryzen-r5-3600-36ghz-am4-35mb_25083/').getprice()
#mob = Item('MSI B450M','https://www.comprasparaguai.com.br/placa-mae-msi-b450m-pro-vdh-plus-amd-soquete-am4_24986/').get_price()
#psu = Item('500W EVGA','https://www.comprasparaguai.com.br/fonte-evga-atx-80-plus-white-500w_12877/').get_price()
#ssd = Item('240GB kingston','https://www.comprasparaguai.com.br/hd-kingston-ssd-sa400s37-240gb-25_15996/').get_price()

pc_novo = Kit(ram,cpu)

print(pc_novo.get_price())

driver.close()
driver.quit()