#/opt/homebrew/bin/chromedriver

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv
import os


base_url = 'https://propakistani.pk/tools/cards/discounts/'
options = Options()
options.headless = False
options.add_argument("--window-size=1920,1200")


DRIVER_PATH = '/opt/homebrew/bin/chromedriver'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get(base_url)


city_cards =  driver.execute_script("""var data = [];  var mData = {};
Array.from(document.getElementsByClassName("row align-items-center mb-4 bg-light mx-0")).forEach((el) => {
     
    
  
    mData[el.firstElementChild.firstElementChild.firstElementChild.innerHTML.trim()] = el.firstElementChild.firstElementChild.firstElementChild.innerHTML.trim()
 
    var banks = el.lastElementChild.children
    var mDiscounts = []
    Array.from(banks).forEach((ell) => {


    mDiscounts.push({
        city: el.firstElementChild.firstElementChild.firstElementChild.innerHTML.trim(),
        bank : ell.innerText.split("(")[0],
        count : ell.innerText.split("(").pop().slice(0,ell.innerText.split("(").pop().length-1)
    })    
    data.push({
        city: el.firstElementChild.firstElementChild.firstElementChild.innerHTML.trim(),
        bank : ell.innerText.split("(")[0],
        count : ell.innerText.split("(").pop().slice(0,ell.innerText.split("(").pop().length-1)
    })    

    
    });
    
    // mData['discounts'] = mDiscounts
    // data = mDiscounts
    // data.push(mData)

});
    return {data,  cities : Object.keys( mData) };
""")
# city_cards =  driver.find_elements(By.CLASS_NAME, "row align-items-center mb-4 bg-light mx-0")



print(city_cards['data'])

with open('./pro_pakistani_generic.csv','w') as file:
    writer = csv.writer(file)

    # for city in city_cards:
    #     for bank in city['discounts']:
            
    #         print([city['city'],bank['bank'],bank['count']])
    #         writer.writerows(city['city'],bank['bank'],bank['count'])



    df = pd.DataFrame(city_cards['data']).to_csv(file)
    # print(df)



for city in city_cards['cities'] :
    driver.get(base_url+city+'/')
    city_data =  driver.execute_script("""
    var data = []
    Array.from(document.getElementsByClassName("items-box box")).forEach((el)=>{

    let vendor_image = el.children[0].innerHTML.split(`alt="`)[0].trim().split(`src="`).pop().replace('"','')
    let vendor_name = el.children[1].children[0].innerText
    var discount_description = el.children[1].children[1].innerText


    let active_banks = el.children[1].children[1].getElementsByTagName('a') 
    let banks = []
    Array.from(active_banks).forEach((bank) => {
        banks.push({ 
            bank_name : bank.href.split('/bank/').pop().replace('/',''),
            uri : bank.href
        })
    })
    data.push({vendor_image,vendor_name,discount_description,banks})
    
    })
    // console.log(data)
    return data
    """)
    with open('./pro_pakistani_'+city+'.csv','w') as file:

        df_city = pd.DataFrame(city_data).to_csv(file)




driver.quit()








