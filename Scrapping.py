# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium import webdriver
import csv
driver =webdriver.Chrome(r"E:\Data Preparation\chromeDrive\chromedriver.exe")
driver.get("https://www.sos.ca.gov/state-holidays")
date=driver.find_elements_by_xpath("//td[1]")
holidayes=driver.find_elements_by_xpath("//td[2]")
for i in date:
    print(i.text)
for j in holidayes:
    print(j.text)
     
with open(r'E:\Data Preparation\holidayes.csv' , 'w', encoding='utf-8' , newline='') as csvfile:
    csvwriter=csv.writer(csvfile , delimiter=';')
    csvwriter.writerow(["date","holidayes"])
    for i in range(1,len(date)):
        csvwriter.writerow([date[i].text , holidayes[i].text])
    
   
    