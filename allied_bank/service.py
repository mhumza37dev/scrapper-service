import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


base_url = 'https://allied-web.peekaboo.guru/'
options = Options()
options.headless = False
options.add_argument("--window-size=1920,1200")


DRIVER_PATH = '/opt/homebrew/bin/chromedriver'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get(base_url)


def sleep(sec):
    time.sleep(sec)

sleep(20)




# all_cities = driver.execute_script(""" var arr1 = Array.from(document.getElementsByClassName('Styled__CityTitleHolder-m8ru5e-10')).map((el)=>{return el?.innerText}); return arr1""")
all_cities = driver.execute_script(""" var arr1 = Array.from(document.getElementsByClassName('Styled__CityTitleHolder-m8ru5e-10')).map((el)=>{return el?.innerText}); return arr1""")
# data = driver.execute_script(""" var arr1 = Array.from(document.getElementsByClassName('Styled__CityTitleHolder-m8ru5e-10')).map((el) => {
#     return el?.innerText
# });
# var arr2 = Array.from(document.getElementsByClassName('Styled__CityBlockHolder-m8ru5e-4')).map((el) => {
#     return el?.children[0].innerText.trim().replace('\n', ',')
# });
# var all_citiess = [...arr1, ...arr2];
# console.log({
#     all_citiess
# }); """)

# all_cities =  driver.execute_script("""
#             //alert("javascript working") 
#             try{
#             var all_cities = [];
#             Array.from(document.getElementsByClassName('Styled__CityTitleHolder-m8ru5e-10')).forEach((el)=>{
#                 all_cities.push(el?.innerText)    
#             });
#             Array.from(document.getElementsByClassName('Styled__CityBlockHolder-m8ru5e-4')).forEach((el)=>{
#                 all_cities.push(el?.children[0].innerText.trim().replace('\n',','))
#             });
#             setTimeout(()=>{
#                 return {all_cities};
#             },1000) ;
#             }catch(e){
#                 reutrn e;
#             }
            
#         """)


# print(all_cities)
# driver.quit()


for city in all_cities:
    mCity = city.split(',')[0].lower()
    if ' ' in mCity:
        sleep(5)
        modified_city_name = mCity.replace(" ","-")
        driver.get(base_url+modified_city_name+'/places/_all/all')
        sleep(5)
        discount = driver.execute_script("""
        var discount = []
        Array.from(document.getElementsByClassName('Styled__CardHolder-sc-1u3pjbo-1 dNxLYe')).forEach(el => {
            // console.log("name = : ",el?.getElementsByClassName('Styled__CardHeaderTitle-sc-1u3pjbo-8')[0].innerText)
            var vendor_image = el?.getElementsByClassName('header Styled__CardHeader-sc-1u3pjbo-6')[0].getElementsByTagName('img')[0].src
            var vendor_name = el?.getElementsByClassName('Styled__CardHeaderTitle-sc-1u3pjbo-8')[0].innerText
            var discount_offer = el?.getElementsByClassName('Styled__Holder-jw4r3n-0')[0].innerText
            var more_details = el.getElementsByTagName('a')[0].href

            discount.push({vendor_image,vendor_name,discount_offer,more_details})
        })
        console.log(discount)
        return discount
        """)
        sleep(5)
        with open('./allied_bank/allied_bank_discounts_'+modified_city_name+'.csv','w') as file:

            df = pd.DataFrame(discount).to_csv(file)
        sleep(5)

    else:
        sleep(5)
        driver.get(base_url+mCity+'/places/_all/all')
        sleep(5)
        discount = driver.execute_script("""
        var discount = []
        Array.from(document.getElementsByClassName('Styled__CardHolder-sc-1u3pjbo-1 dNxLYe')).forEach(el => {
            // console.log("name = : ",el?.getElementsByClassName('Styled__CardHeaderTitle-sc-1u3pjbo-8')[0].innerText)
            var vendor_image = el?.getElementsByClassName('header Styled__CardHeader-sc-1u3pjbo-6')[0].getElementsByTagName('img')[0].src
            var vendor_name = el?.getElementsByClassName('Styled__CardHeaderTitle-sc-1u3pjbo-8')[0].innerText
            var discount_offer = el?.getElementsByClassName('Styled__Holder-jw4r3n-0')[0].innerText
            var more_details = el.getElementsByTagName('a')[0].href
            discount.push({vendor_image,vendor_name,discount_offer,more_details})
        })
        console.log(discount)
        return discount
        """)

        sleep(5)
        with open('./allied_bank/allied_bank_discounts_'+mCity+'.csv','w') as file:

            df = pd.DataFrame(discount).to_csv(file)
        sleep(5)




driver.quit()




