from selenium import webdriver
from requests import get
import subprocess

def userAndPassword():
    user = ''
    password = ''
    return user, password

def acess():
    driver = webdriver.Chrome()
    driver.get("https://login.ufpi.br:6082/php/uid.php?vsys=1&rule=0&url=http://conecta.ufpi.br%2f")
    user, password = userAndPassword()

    user_box = driver.find_element_by_name('user')
    pass_box = driver.find_element_by_name('passwd')

    user_box.send_keys(user)
    pass_box.send_keys(password)

    login_button = driver.find_element_by_id('submit')
    login_button.click()

try:
    r = get('https://www.facebook.com')
    status = r.status_code
    print(r.status_code)
    print('Conectado a Internet')
except:
    sistema = str(subprocess.check_output(["arp", "-n"]))
    ip = str("10.94.255.250")
    ip2 = str("10.15.255.250")

    if ip in sistema or ip2 in sistema:
        print('Conectado a Internet da UFPI')
        acess()
    else:
        print('Não está conectado a Internet da UFPI')
