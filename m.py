import requests
import json
import logging as logger
import time
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

# ["43001-45999","73001-74966","97001-97920","15001-19640","29001-29945","57001-57799","37010-38589","73301-88595","84001-84791","05001-05907","20101-24658","98001-99403","53001-54990","82001-83414","35004-36925","33992-34997","06001-06928","02801-02940","19701-19980","19701-19980","99501-99950","85001-86556","71601-72959","90001-92162","80001-81658"]
#zip_list=["87001-88439","07001-08989","03031-03897","88901-89883","68001-69367","63001-65899","58001-58856","38601-39776","01001-05544","03901-04992","70001-71497",27006-28909","24701-26886","48001-49971","20588-21930","55001-56763"]

OUTPUT_FOLDER=r"C:\Users\Sohom\Desktop\scrapping22222\results.txt"

zip_list=[]
# zip = 80004
lst2 = set()
def find(set1):
    for j in set1 :
        try:
            lst1=set()
            url = "https://pro.petsitters.org/directory?field_ym_member_add_zip_tid="+str(j)
            uclient = uReq(url)
            page  = uclient.read()
            page_html = bs(page, "html.parser")
            bigboxes = page_html.findAll("div", {"class": "view-content"})


            pro_link = "https://pro.petsitters.org/"+bigboxes[0].div.span.a["href"]
            pro_data = requests.get(pro_link)
            pro_data.encoding = "utf-8"
            pro_html = bs(pro_data.text, "html.parser")
            # print(pro_html)
            name = pro_html.find("p", {"class" : "name"}).string
            adress = pro_html.find("p", {"class" : "location"}).string
            mail_website = pro_html.find("div", {"class" : "contact-icons"})
            mail_website = mail_website.findAll("a")
            mail = mail_website[0].string
            website = mail_website[1].string
            services = pro_html.find("div", {"class" : "views-field views-field-field-ym-member-services-provide"}).div.ul
            services_provided = services.findAll("li")
            c= 0
            for i in services_provided:
                services_provided[c] = services_provided[c].string
                c = c+1
# print(services_provided)

            lst1.add(j)
            final_data=dict()
            final_data["name"] = name
            final_data["adress"] = adress
            final_data["mail"] = mail
            final_data["website"] = website
            final_data["services-provided"] = services_provided
            # print(final_data)

            with open(OUTPUT_FOLDER, 'a') as f: 
                
                f.write(f'Zip: {j}\n')
                f.write(f'Name: {final_data["name"]}\n')
                f.write(f'services-provided: \n')
                for k in final_data["services-provided"]:
                    f.write(f'{k}\n')
                f.write(f'Address: {final_data["adress"]}\n')
                f.write(f'Website: {final_data["website"]}\n')
    # f.write(f'Phone number: {i[[]}\n\n')

            lst1.add(j)

        except requests.exceptions.ConnectionError as e:
            logger.error(f'Connection failed..')
        except:
            logger.error(f"Zip doesn't exist")
# .div.div.span.a['href']



def scrape():
    for k in zip_list:
        zip=k.split("-")
        set1=set(range(int(zip[0]),int(zip[1])+1))
        lst1=find(set1)
        print(lst1)
        # lst2=set1.difference(lst1)
        # print(lst2)
        # while len(lst2)!=0:
        #     lst2=lst2.difference(find(lst2))
            

scrape()