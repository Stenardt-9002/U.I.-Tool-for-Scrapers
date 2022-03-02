from bs4 import BeautifulSoup,Comment
import requests
import re
import os 
import time 






def function_for_text(soup_obj,atrr):  
    temp_tag = soup_obj.find_all(atrr[0],atrr[1])
    string_data = ""    
    for all_tags in temp_tag:
        string_data+=str(all_tags.get_text())
    return str(string_data)





from bs4 import BeautifulSoup,Comment
import requests
import re
import os 
import time 






def function_for_text(soup_obj,atrr):  
    temp_tag = soup_obj.find_all(atrr[0],atrr[1])
    string_data = ""    
    for all_tags in temp_tag:
        string_data+=str(all_tags.get_text())
    return str(string_data)






html_stuff = requests.get("https://www.w3schools.com/js/js_htmldom.asp").text 
soup = BeautifulSoup(html_stuff,"lxml")
body_tag = soup.body

args1 = ["body",{}]

try:
    print(function_for_text(soup,args1))
except:
    print("Some Error occured")





