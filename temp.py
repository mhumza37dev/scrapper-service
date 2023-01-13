# import pandas as pd
# url='https://github.com/owid/covid-19-data/blob/master/public/data/latest/owid-covid-latest.csv'
# df=pd.read_csv(url, sheet_name='Sheet1')
# print(df)


import re
import requests
import pandas as pd
from os.path import isfile, join
import os




# all_cities = ['Karachi', 'Islamabad', 'Rawalpindi', 'Lahore', 'Sialkot', 'Faisalabad', 'Quetta', 'Peshawar', 'Hyderabad', 'Multan', 'Gujranwala']


# headers= {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.127 Safari/537.36",
#     # "x-xsrf-token": "eyJpdiI6IlBhMktQUEc3d2VLa01uVUxoSjBUREE9PSIsInZhbHVlIjoiemk2SWR5R0Z2N3FobVowTWlMMEg4Tksza1hGZFNic3JtdXJwaHFpb2IxUU0vaGx2bUttZDUwWnB0V2tnV0NCVE4yMnVWcWVYdjRYQUw0TjBBNnhnQnNWR3JoaCtTZVJNR2FXSlQwYWNKbnJGcE1UOE9YZVI2aGl2N2FZbU1rNzkiLCJtYWMiOiJjMjM5N2Q2YWQ3YWUyMDIwNmM2Y2ZiNmIxYTJmZDFmYWVlYzJhMDg0MjU0Nzg2YTIxZmNmNjllNWRhMTFjMGY2IiwidGFnIjoiIn0=",
#     "origin":"https://www.telemart.pk",
#     "referer": "https://bop-web.peekaboo.guru/",
#     "cookie": "_gcl_au=1.1.352435580.1669458536; _ga=GA1.2.1557338994.1669458536; _gid=GA1.2.1272611273.1669458536; _gat_gtag_UA_46073612_1=1; _gat=1; AWSALBTG=rL4JD462OUxWkxL1wk+Te+86w3V4q592iLq0K2WOW8xUlk8PReOlFbwGO3e+WbzEjvGdUN6PMya2UEDMh96FzXiYtm4vdifvQrdADmFJTNpdazs4v7Oz1OLnZLKb86PcmnnHQlGORMGYgcsPg42cOdF7PT2c1o/KPV3m1vqBKFm4B4oW7CU=; AWSALBTGCORS=rL4JD462OUxWkxL1wk+Te+86w3V4q592iLq0K2WOW8xUlk8PReOlFbwGO3e+WbzEjvGdUN6PMya2UEDMh96FzXiYtm4vdifvQrdADmFJTNpdazs4v7Oz1OLnZLKb86PcmnnHQlGORMGYgcsPg42cOdF7PT2c1o/KPV3m1vqBKFm4B4oW7CU=; XSRF-TOKEN=eyJpdiI6IlBhMktQUEc3d2VLa01uVUxoSjBUREE9PSIsInZhbHVlIjoiemk2SWR5R0Z2N3FobVowTWlMMEg4Tksza1hGZFNic3JtdXJwaHFpb2IxUU0vaGx2bUttZDUwWnB0V2tnV0NCVE4yMnVWcWVYdjRYQUw0TjBBNnhnQnNWR3JoaCtTZVJNR2FXSlQwYWNKbnJGcE1UOE9YZVI2aGl2N2FZbU1rNzkiLCJtYWMiOiJjMjM5N2Q2YWQ3YWUyMDIwNmM2Y2ZiNmIxYTJmZDFmYWVlYzJhMDg0MjU0Nzg2YTIxZmNmNjllNWRhMTFjMGY2IiwidGFnIjoiIn0=; telemart_session=eyJpdiI6IjRiMGVhMExwVlNpMjFSZEQvcStIM3c9PSIsInZhbHVlIjoiV2xXLzdEbFE1ZVVGTHhvT29wNlFxY3c2eXQ3bnhVQ1RMTHlBRVU3c3hoZXdSMG9ORUViT0lnMGdxa2s2dEQ0Uk9mN1lWM25NclNVVEdRc1FOc2thRVV4Lzcxb3kwTXdkSGFhU21Vb3hCeHA1TG94eXpHTGY3aXZvUXNneCtsc0UiLCJtYWMiOiI3NjJjZDAyY2FjNWE3NjJhM2IyNDFkMzk1ZTgwY2UxNTI2MjE1YzIzZGJkNGVmYjIwYjMzZGU2MzJjMmMwZTNkIiwidGFnIjoiIn0=",
#     "accept-encoding": "gzip, deflate, br",
#   "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
#   "cache-control": "no-cache",
#   "content-length": "187",
#   "content-type": "application/json", 
#    "origin": "https://bop-web.peekaboo.guru",
#   "ownerkey": "d98a49c8932b09184e9d5bef841d99e0",
#   "pragma": "no-cache",
#   "medium": "IFRAME",
#     "method": "POST",
#     "dnt":"1",
#     "Cookie":"fbp=fb.1.1672841818101.313195498; _gcl_au=1.1.568667475.1672841819; _ga=GA1.2.1207278388.1672841819; __gads=ID=be30c0a23313e962-221c1ac70fd800c0:T=1672841819:RT=1672841819:S=ALNI_MYWxpSROF9-264pZVdSSscM4yq3Pw; __gpi=UID=00000bbaaa291d0f:T=1672841819:RT=1672841819:S=ALNI_MaT1Huw7ygkKi-KrKcTNjn0R7-SmQ; _ga=GA1.3.1115765304.1673523981; _gid=GA1.3.1116659515.1673523981; _gat=1"
# }

# for city in all_cities:


#     main_obj = {
#         "fksyd": city,
#         "n4ja3s": "Pakistan",
#         "js6nwf": "0",
#         "pan3ba": "0",
#         "mstoaw": "en",
#         "angaks": "all",
#         "j87asn": "_all",
#         "makthya": "trending",
#         "mnakls": 10000,
#         "opmsta": "0",
#         "kaiwnua": "_all",
#         "klaosw": "false",
#     }
#     main_url = "https://secure-sdk.peekaboo.guru/uljin2s3nitoi89njkhklgkj5"
#     main_r = requests.post(main_url,headers=headers, json=main_obj).json()
#     # print(main_r)
#     for vendor in main_r:
#         v_name =  vendor["name"]
#         print(v_name, "=== >>> ", city)
#         obj =  {
#             "fksyd": city,
#             "matsw": v_name,
#             "n4ja3s": "Pakistan",
#             "js6nwf": "0",
#             "pan3ba": "0",
#             "mstoaw": "en",
#             "cotuia": 13963,
#             "nai3asnu": "All",
#             "ia3uas": "All",
#             "kaiwnua": "_all",
#             "yudwq": "_all",
#             "njsue": "sdk",
#             "hgoeni": 13963,
#             "mnakls": "100",
#             "opmsta": "0",
#             "mghes": "true",
#             "klaosw": "false",
#             "makthya": "discount"
#         }
#         url = "https://secure-sdk.peekaboo.guru/ksbolruuahrndcjchshjhejgjhasdo787kjieo767kjsgeskoyfgwwhkl6"
#         r = requests.post(url,headers=headers, json=obj).json()
#         response = []
#         if(len(r) > 0 ):
#             for rr in r:
#                 for rrr in rr["associations"]:
#                     response.append({
#                     "card" : rrr["name"],
#                     "vendor_name":v_name,
#                     "city" :city,
#                     "description" : rr["description"],
#                     "title" : rr["title"]
#                     })

#         print(response)
#         new_csv_file = "./bop/discount"+"_cards_"+city+".csv"

#         df = pd.DataFrame(response).to_csv(new_csv_file,mode='a', index=False, header=not os.path.exists(new_csv_file)




# headers = {
#     "accept-encoding": gzip, deflate, br
# "accept-language": en-GB,en-US;q=0.9,en;q=0.8
# authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NzIsInJvbGUiOiJndWVzdCIsImlhdCI6MTU1MzcwMDgwNiwianRpIjoiUEpJMXFTb2ktQzRBZFJWcm9nb3RNV2UzV3VXcFdXTm0ifQ.2mb26xL4Qt7FfBQZ-XQvp-fhecMpaVUVXWp_GEST_6U
# cache-control: no-cache
# content-length: 233
# content-type: application/json
# cookie: _fbp=fb.1.1672841818101.313195498; _gcl_au=1.1.568667475.1672841819; _ga=GA1.2.1207278388.1672841819; __gads=ID=be30c0a23313e962-221c1ac70fd800c0:T=1672841819:RT=1672841819:S=ALNI_MYWxpSROF9-264pZVdSSscM4yq3Pw; connect.sid=s%3AWYE7Z3d1hopRiNhsRaS9eMzyXU3Cdce5.g6gTx0oTkq6mlrjyBrcT7L75%2F9KFCF8Rd6yGKANod7I; _gid=GA1.2.913441069.1673535486; __gpi=UID=00000bbaaa291d0f:T=1672841819:RT=1673535487:S=ALNI_MaT1Huw7ygkKi-KrKcTNjn0R7-SmQ
# launcher: undefined
# medium: WEB
# origin: https://peekaboo.guru
# pragma: no-cache
# referer: https://peekaboo.guru/karachi/card-deal/14127/96/87721/up-to-15-off-on-domestic-flights-hotels-and-tours
# sec-ch-ua: "Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"
# sec-ch-ua-mobile: ?0
# sec-ch-ua-platform: "Windows"

# }




headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.127 Safari/537.36",

    "Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-US,en;q=0.9",
"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NzIsInJvbGUiOiJndWVzdCIsImlhdCI6MTU1MzcwMDgwNiwianRpIjoiUEpJMXFTb2ktQzRBZFJWcm9nb3RNV2UzV3VXcFdXTm0ifQ.2mb26xL4Qt7FfBQZ-XQvp-fhecMpaVUVXWp_GEST_6U",
"Content-Length": "200",
"Content-Type": "application/json",
"Cookie": "_gcl_au=1.1.1597963223.1673333942; _ga=GA1.2.739568908.1673333942; connect.sid=s%3AvCOLEmRM8VTJZ4-ax7_q-b19FHlXUL7E.Ow7WrZFQdEGqP5sgSiT3U%2FuDXVMAEcLqr%2FVyNdHtDp4; _gid=GA1.2.763830127.1673533448",
"Medium": "WEB",
"Origin": "https://peekaboo.guru",
# "Referer": "https://peekaboo.guru/islamabad/detail/778/allied-bank/discounts",
}

obj = {
    "city": "Faisalabad",
    "country": "Pakistan",

    "language": "en",
    "limit": "10000000",
    "offset": "0",
    "skipGlobalDeals": "true",
    "associatedDeals": "true",
    "selfDeal": "false",

}

main_url = "https://peekaboo.guru/api/v8/entity/deals"
main_r = requests.post(main_url,headers=headers, json=obj).json()

# print(main_r)

new_csv_file = "./bop/discount"+"_cards_Faisalabad"+".csv"
#  new_csv_file = "./bop/discount"+"_cards_Islamabad"+city+".csv"
df = pd.DataFrame(main_r["deals"]).to_csv(new_csv_file,mode='a', index=False, header=not os.path.exists(new_csv_file))

   


    #    "lat": 33.729388,
    # "long": 73.093146,