import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



base_url = 'https://www.bankalfalah.com/personal-banking/cards/privileges-discounts/discounts'
options = Options()
options.headless = False
options.add_argument("--window-size=1920,1200")


DRIVER_PATH = '/opt/homebrew/bin/chromedriver'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get(base_url)



discounts =  driver.execute_script(""" 
var data = [];  var mData = {};
function Convert(element) {
        var table = element.getElementsByClassName('discountTable')[0];
        var header = [];
        var rows = [];
 
        for (var i = 0; i < table.rows[0].cells.length; i++) {
            header.push(table.rows[0].cells[i].innerHTML);
        }
 
        for (var i = 1; i < table.rows.length; i++) {
            var row = {};
            for (var j = 0; j < table.rows[i].cells.length; j++) {
                row[header[j]] = table.rows[i].cells[j].innerHTML;
            }
            rows.push(row);
        }
         return rows
         // console.log(rows);
    }
Array.from(document.getElementsByClassName("popupDiscount"))?.forEach((el) => {
    var category = el?.parentElement?.getElementsByClassName('discountCategory')[0]?.innerText?.trim() ||  "N/A" 
    var city = el?.getElementsByClassName('colorRed  text-left normalFont paddingLeft0 marginBottom0')[0].innerText.trim() ||  "N/A" 
    var title = el?.children[1]?.innerText?.trim() ||  "N/A" 
    var max_discount_cap = el?.getElementsByClassName('checkList')[0]?.innerText?.trim() ||  "N/A" 
    var discount_by_cards = Convert(el) 
    discount_by_cards.map((dis)=>{
        card_detail = dis.Card
        discount = dis.Discount
      data.push({title ,city, category,max_discount_cap,card_detail,discount})
    })
    console.log({category,city,title,max_discount_cap,discount_by_cards}) 
    data.push({title ,city, category,max_discount_cap,card_detail,discount})
  
})
    return data
 """)

print(discounts)


with open('./bank_alfalah/bank_alfalah_discounts.csv','w') as file:

    df = pd.DataFrame(discounts).to_csv(file)

driver.quit()