#https://who.is/whois/{}
#ip = https://check-host.net/ip-info?host={}
#https://who.is/dns/{}



import requests
from time import sleep
from bs4 import BeautifulSoup


logo = """ 
                 █████                █████████                               
                ░░███                ███░░░░░███                              
 █████ ███ █████ ░███████    ██████ ░███    ░░░   ██████   ██████   ████████  
░░███ ░███░░███  ░███░░███  ███░░███░░█████████  ███░░███ ░░░░░███ ░░███░░███ 
 ░███ ░███ ░███  ░███ ░███ ░███ ░███ ░░░░░░░░███░███ ░░░   ███████  ░███ ░███ 
 ░░███████████   ░███ ░███ ░███ ░███ ███    ░███░███  ███ ███░░███  ░███ ░███ 
  ░░████░████    ████ █████░░██████ ░░█████████ ░░██████ ░░████████ ████ █████
   ░░░░ ░░░░    ░░░░ ░░░░░  ░░░░░░   ░░░░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░ ░░░░░                                                                                                                                                                                                                                       
"""
print(logo)

print("--------------------------------------------------------------")
print(">>>EXAMPLE:  (1) whois sorgulama    (2) dns sorgulama    (3)ip sorgulama")
print("--------------------------------------------------------------")

work_number = input("İSLEM NUMARASI GİRİNİZ: ")
print("\n")


if work_number == '1':


    domain = input('>>[+]DOMAİN GİRİNİZ: ')
    url = 'https://who.is/whois/{}'.format(domain)

    sorgula = requests.get(url)
    sleep(5)

    soup = BeautifulSoup(sorgula.content,'lxml')
    bilgi = soup.find_all('div',attrs={'class':'col-md-12 queryResponseBodyValue'})
    dosyaismi = input("Dosya İsmi Giriniz  (örnek.txt) :")

    for bilgiler in bilgi:

        print(bilgiler.text)
        veri = bilgiler.text
        yazdir = veri
        dosya = open(dosyaismi,"a")
        ekle = dosya.write(yazdir)
        dosya.close()
    print("dosya kaydedildi / / yol: program klasörü >>> ",dosyaismi)


elif work_number == '2':

    domain = input('>>[+]DOMAİN GİRİNİZ: ')
    url = 'https://who.is/dns/{}'.format(domain)

    sorgula = requests.get(url)
    sleep(5)

    soup = BeautifulSoup(sorgula.content,'lxml')
    bilgi = soup.find_all('div',attrs={'class':'col-md-12 queryResponseBodyKey'})
    dosyaismi = input("Dosya İsmi Giriniz  (örnek.txt) :")


    for bilgiler in bilgi:

        print(bilgiler.text)

        veri = bilgiler.text
        yazdir = veri
        dosya = open(dosyaismi,"a")
        ekle = dosya.write(yazdir)
        dosya.close()
    print("dosya kaydedildi / / yol: program klasörü >>> ",dosyaismi)



elif work_number == '3':


    domain = input('>>[+]DOMAİN GİRİNİZ: ')
    url = 'https://check-host.net/ip-info?host={}'.format(domain)

    sorgula = requests.get(url)
    sleep(5)

    soup = BeautifulSoup(sorgula.content,'lxml')
    bilgi = soup.find_all('div',attrs={'class':'ipinfo-item'})
    dosyaismi = input("Dosya İsmi Giriniz  (örnek.txt) :")


    for bilgiler in bilgi:

        print(bilgiler.text)

        veri = bilgiler.text
        yazdir = veri
        dosya = open(dosyaismi,"a")
        ekle = dosya.write(yazdir)
        dosya.close()
    print("dosya kaydedildi / / yol: program klasörü >>> ",dosyaismi)


else:

    print("GEÇERLİ BİR SEÇİM YAPMADINIZ!!")