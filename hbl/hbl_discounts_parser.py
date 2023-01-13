
from os import listdir, getcwd
from os.path import isfile, join
import os

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv
import time

base_path = getcwd() + "/allied_bank"

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")


DRIVER_PATH = '/opt/homebrew/bin/chromedriver'


only_csv_files = [f for f in listdir(base_path) if isfile(join(base_path, f)  ) and f.endswith('.csv')]

print(only_csv_files.sort())


any_of_these_cities = ('karachi', 'islamabad', 'rawalpindi', 'lahore', 'sialkot', 'faisalabad', 'quetta', 'peshawar', 'hyderabad', 'multan', 'gujranwala')
url_prefix_base = "https://allied-web.peekaboo.guru/"
url_suffix_tail = "places/_all/all"

print(any_of_these_cities)




for file in only_csv_files:
    if file.__contains__(any_of_these_cities):
        with open(base_path+"/"+file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row.keys().__contains__("more_details"):
                    print(row['more_details'])
                    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
                    driver.get(row['more_details'])

                    time.sleep(20)
                    driver.execute_script(""" document.getElementsByClassName('Styled__ListItem-sc-14n6kj-1 bjMUOR')[0].click(); """)
                    time.sleep(10)
                    cards = driver.execute_script(""" 
                
                






var isEnd = document.getElementsByClassName("Styled__ButtonRow-sc-6akaes-1")[0]?.lastElementChild?.children[0]?.getAttributeNames()?.includes("disabled");
console.log(isEnd);
var cards = [];



if(isEnd === null || isEnd === undefined){
Array.from(document.getElementsByClassName("Styled__CardButton-sc-1digmfo-18 gyonQX")).map((el) => {
         cards.push({
             card: el?.innerText.trim(),
             url: window.location.href,
             discount_offer: document.getElementsByClassName("Styled__DealTitle-sc-1digmfo-8")[0].innerText,
             vendor_name: document.getElementsByClassName("DealEntityTitle__Content-sc-1c75y3r-0")[0].innerText.trim(),
            vendor_image: document.getElementsByClassName("DealEntityTitle__Content-sc-1c75y3r-0")[0].getElementsByTagName("img")[0].src
         })
       })
// console.log(cards)
return cards
    
}
else{

while (isEnd === false && isEnd !== true) {
       isEnd = document.getElementsByClassName("Styled__ButtonRow-sc-6akaes-1")[0]?.lastElementChild?.children[0].getAttributeNames().includes("disabled")
       Array.from(document.getElementsByClassName("Styled__CardButton-sc-1digmfo-18 gyonQX")).map((el) => {
         cards.push({
             card: el?.innerText.trim(),
             url: window.location.href,
             discount_offer: document.getElementsByClassName("Styled__DealTitle-sc-1digmfo-8")[0].innerText,
             vendor_name: document.getElementsByClassName("DealEntityTitle__Content-sc-1c75y3r-0")[0].innerText.trim(),
            vendor_image: document.getElementsByClassName("DealEntityTitle__Content-sc-1c75y3r-0")[0].getElementsByTagName("img")[0].src
         })
       })
       document.getElementsByClassName("Styled__ButtonRow-sc-6akaes-1")[0].lastElementChild.children[0].click()
}
// console.log(cards)
return cards

}
                    """)
                    print(cards)
                    time.sleep(20)
                    new_csv_file = base_path+"/cards/"+"cards_"+file
                    # with open(base_path+"/cards/"+"cards_"+file, 'w') as new_csvfile:
                    dfff = pd.DataFrame(cards).to_csv(new_csv_file,mode='a', index=False, header=not os.path.exists(new_csv_file))
                    driver.quit()