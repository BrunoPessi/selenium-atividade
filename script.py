from selenium import webdriver #importando o webdriver para acessar o chrome
import time #importação de tempo

#Mostrar/definir caminho da pasta que está localziado o chromedriver
chrome_path = r"/usr/local/bin/chromedriver"
drive= webdriver.Chrome (chrome_path)
#definição de url
drive.get ("https://www.kaggle.com/dongeorge/beer-consumption-sao-paulo")
#ID de botões e .click() para selecionar
drive.find_element_by_xpath ("""//*[@id="sign-in-button"]/div""").click()
time.sleep(2) #time.sleep "pausar" o andamento pelo tempo definido
#login
email_field = drive.find_element_by_id ("username-input-text")
email_field.clear() #Limpar dados já existentes no campo
email_field.send_keys ("grupo5aa") #inserção de dados (nesse caso login)
time.sleep(1)
#senha
password_field = drive.find_element_by_id("password-input-text")
password_field.clear()
password_field.send_keys("@ulaAberta")
time.sleep(1)
#botão de login
sign_in_button = drive.find_element_by_id("submit-sign-in-button")
sign_in_button.click()
#botão de download
download = drive.find_element_by_xpath("""/html/body/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/div[2]/a[1]/div""").click()
time.sleep(3)
#botão de logout para sair da conta
logout_button = drive.find_element_by_xpath("""/html/body/div[2]/div[1]/div/div/div/div/div/div/div[4]""").click()
time.sleep(1)
logout = drive.find_element_by_xpath("""/html/body/div[2]/div[1]/div/div/div/div/div/div/div[4]/div/div/nav/li[4]/a""").click()



