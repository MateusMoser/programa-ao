from selenium import webdriver
from selenium.webdriver.firefox.options import Options


option = Options()
option.headless = True


def getprice(link,product):
    driver = webdriver.Firefox(options=option)
    driver.get(link)
    price = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/div/div[3]/div[3]/div/div[3]/div[1]/span').text
    print(product[0:25] + ':\t' + price)

    price_float = price[3:]
    price_float = price_float.replace('.','')
    price_float = price_float.replace(',','.')
    #print(float(price_float))
    driver.close()
    driver.quit()
    return float(price_float)

RAM = getprice('https://www.comprasparaguai.com.br/memoria-kingston-hyperx-fury-ddr4-8gb-3200mhz_26738/','Memoria RAM 8gb 3200mhz')
CPU = getprice('https://www.comprasparaguai.com.br/processador-amd-ryzen-r5-3600-36ghz-am4-35mb_25083/', 'Processador Ryzen 5 3600')
MOB = getprice('https://www.comprasparaguai.com.br/placa-mae-msi-b450m-pro-vdh-plus-amd-soquete-am4_24986/','MSI B450M')
PSU = getprice('https://www.comprasparaguai.com.br/fonte-evga-atx-80-plus-white-500w_12877/','Fonte 500W EVGA')
SSD = getprice('https://www.comprasparaguai.com.br/hd-kingston-ssd-sa400s37-240gb-25_15996/','SSD 240GB kingston')
GAB = 200.00
GPU = getprice('https://www.comprasparaguai.com.br/placa-de-video-evga-geforce-gtx1660ti-sc-ultra-6gb-gddr6-pci-express_29986/','GTX 1660TI EVGA')


print(f'O kit completo vai custar para upgrade ficou \nR$ {RAM+CPU+MOB}')
print(f'Para comprar um pc novo do zero o preço ficou em \nR$ {RAM+CPU+MOB+PSU+SSD+GAB+GPU}')
#getprice('https://www.comprasparaguai.com.br/notebook-hp-14-dq1039wm-intel-core-i5-10ghz-memoria-8gb-ssd-256gb-16gb-optane-14-windows-10_28356/','Notebook i5/8gb/ssd')

