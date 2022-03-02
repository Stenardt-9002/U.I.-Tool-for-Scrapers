import os
import re
import sys
import csv
import urllib.request
from collections import Counter
import json

from bs4 import BeautifulSoup
import requests
import time 

from networkx.readwrite import json_graph
import networkx as nx
import requests
from bs4 import BeautifulSoup
from collections import defaultdict

from beautifulsoup_obj import function1_get_b_object





HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding":"gzip, deflate",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}


























def function_extraction_text(input_tag,args_location,sub_Data_tag_difference,data_count_eachpage):
    #parent tag , location in args 
    # run for each page 
    print(input_tag)
    print(args_location)
    print(sub_Data_tag_difference)
    string_data1 = ""
    #args_location
    temp_tag = input_tag
    for each_tag in args_location:
        temp_tag = function1_get_b_object(temp_tag,each_tag)
        # temp_tag = temp_tag.each_tag
    time.sleep(5)
    for i1 in range(data_count_eachpage):
        temp_tag = function1_get_b_object(temp_tag,sub_Data_tag_difference)
        temp1 = str(temp_tag.text)
        # temp1 = str(temp_tag.sub_Data_tag_difference.text)
        string_data1+=temp1
        string_data1+="\n\n"
        # temp_tag = function1_get_b_object(temp_tag,sub_Data_tag_difference)
        # temp_tag = temp_tag.sub_Data_tag_difference
    return string_data1





#url input  , file storing name
def main_function(url_link1,tag_information ,files_name="Temp1.txt"):

    # tag_information =[["input",{"placeholder":"Search reviews"}],["div",{"class":"pageNumbers"}]]
    #in this manner

    html_stuff = requests.get(url_link1).text
    soup = BeautifulSoup(html_stuff,'lxml')

    input_tag = soup.find(tag_information[0][0],tag_information[0][1] )


    #get data 
    main_string = function_extraction_text(input_tag,["parent"],"next_sibling",5  )
    #ask repeat 
    f1 = open(files_name,"a",encoding="utf-8")
    f1.write(main_string)
    f1.close()


    pass 

#if direct attribute of data 
def new_function(soup_obj,atrr):
    # atrr = ["input",{"placeholder":"Search reviews"}]
    temp_tag = soup_obj.find(atrr[0],atrr[1])
    return str(temp_tag.text)
    pass









vocab = ["service" ,"location","resort","hotel"]




def reviewornot(text_tags):
    #improve it vby adding nltk
    if text_tags.name=="span":
        # if re.compile("(?=.*test)(?=.*long)").search(text_tags.text):
        for echword_1 in vocab:
            if echword_1 in text_tags.text.lower():
                if len(text_tags.text)>30:
                    return text_tags
        return False
    return False

def get_hierarchy(temp_Tag):
    iteration1 = 0
    return_list1 = []
    while temp_Tag.name !="body":
        print(temp_Tag.name,"  ",temp_Tag.attrs)
        return_list1.append([temp_Tag.name,temp_Tag.attrs])
        temp_Tag = temp_Tag.parent
        iteration1+=1
    print(temp_Tag.name,"  ",temp_Tag.attrs)
    return_list1.append([temp_Tag.name,temp_Tag.attrs])
    return return_list1 



























def _traverse_html(_d, _graph, _counter, _parent=None, _node_dict=None):
  """Traverse the DOM elements in a HTML soup and create a networkx graph"""
  for i in _d.contents:
     if i.name is not None:
       try:
         _name_count = _counter.get(i.name)
         if _parent is not None:
           _graph.add_node(_parent)
           _c_name = i.name if not _name_count else f'{i.name}_{_name_count}'
           _graph.add_edge(_parent, _c_name)
           _node_dict[_c_name] = i
         _counter[i.name] += 1
         _traverse_html(i, _graph, _counter, i.name, _node_dict=_node_dict)
       except AttributeError:
         pass

def parse_tag(tag):
  """Parse node id into a HTML tag
  
  eg: div_134 -> div
  """
  return tag[:tag.find('_')] if '_' in tag else tag 



def w2json(url):
  """fetch DOM elements from a URL and return a networkx graph as JSON"""
  # create an empty graph
  wg = nx.Graph()
  # get response from url
  response = requests.get(url, headers=HEADERS)
  # get soup
  soup = BeautifulSoup(response.content, "lxml")
  # remove garbage
  for script in soup.select('script'):
    script.extract()
  # create an empty node dictionary
  node_dict = {}
  # traverse through soup -> get graph
  _traverse_html(soup, wg, defaultdict(int), _node_dict=node_dict)
  return g2json(wg, node_dict)


def g2json(g, node_dict):
  """Convert a networkx graph to JSON format"""
  # make unique tags
  tags = [ parse_tag(key) for key in list(node_dict.keys()) ]
  tag_id = { tag: i for i, tag in enumerate(sorted(set(tags))) }
  # include html tag
  tag_id.update({'html' : len(tag_id) })
  json_g = json_graph.node_link_data(g)
  for i, node in enumerate(json_g['nodes']):
    json_g['nodes'][i]['label'] = tag_id[parse_tag(node['id'])]
    if node['id'] in node_dict:
      json_g['nodes'][i]['attrs'] = node_dict[node['id']].attrs
    else:
      json_g['nodes'][i]['attrs'] = {}
  return json_g






























if __name__ == "__main__":

    DEBUG11 = 0
    url = sys.argv[1]
    domain = sys.argv[2]
    link1 = url


    # files1 = open("heh.txt",'a')
    # # files1.write(url)
    # files1.write(domain)
    # files1.close()




    # obj = Webpage(url, domain)

    # tables = obj.get_tables()
    # if DEBUG11==1:

    #     files1 = open("heh.txt",'w')
    #     files1.write(tables)
    #     files1.close()
    # images = obj.get_images()
    # if DEBUG11==1:

    #     files1 = open("heh.txt",'w')
    #     files1.write(images)
    #     files1.close()
    # elements = obj.get_elements()
    # if DEBUG11==1:

    #     files1 = open("heh.txt",'w')
    #     files1.write(elements)
    #     files1.close()
    # links = []
    # for x in elements:
    #     if "a" in x.keys():
    #         links.append(x)

    # result = dict()

    # result["elements"] = elements
    # result["tables"] = tables
    # result["images"] = images
    # result["links"] = links
    # result["others"] = []


    
    
    # html_stuff = requests.get("https://www.tripadvisor.in/Hotel_Review-g306995-d7367388-Reviews-La_Vie_Woods-Calangute_North_Goa_District_Goa.html").text
    
    
    
    
    
    
    
    
    
    
    # html_stuff = requests.get(link1).text

    # soup = BeautifulSoup(html_stuff,'lxml')
    # body_tag = soup.body

    # text_data = body_tag.find_all(reviewornot)
    # iteration2 = 0

    # for stuff1 in text_data:
    #     iteration2+=1
    #     print("\nText Tag " ,iteration2 )
    #     print()
    #     sample_text_hierarchy = get_hierarchy(stuff1)
    #     print(stuff1.text)







    result = dict()
    # elements = 
    args1 =[["input",{"placeholder":"Search reviews"}],["div",{"class":"pageNumbers"}]]

    # main_function(link1,args1,"file1.txt")
    result["elements"] = ["Sample1 Addition" ]
    result["tables"] = []
    result["images"] = []
    result["links"] = []
    result["others"] = []

    
    # print(json.dumps(result))
    

    print(json.dumps(w2json(url)))

















































































































# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import os
# import re
# import sys
# import csv
# import urllib.request
# from collections import Counter
# import json
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By



# def valid_link(link, domain):
#     '''
#         Utility
#         Determine whether the link is within the domain
#     '''

#     if link.find("https://") == 0:
#         link = link[8:]
#     if link.find("http://") == 0:
#         link = link[7:]

#     if domain in link.split("."):
#         return True
#     return False


# def find_last_name(url):
#     '''
#         Returns string between last and second-last '/'
#     '''

#     if url[-1] == '/':
#         url = url[:-1]

#     return url.split('/')[-1]


# class Webpage(object):

#     def __init__(self, url, domain):
#         # ch = os.getcwd() + '/python/tools/chromedriver'
#         ch = os.getcwd() + '/tools/chromedriver'

#         options = Options()
#         # options.set_headless(headless=True)
#         options.add_argument("--headless")
#         options.add_argument("--disable-gpu")
#         options.add_argument("--disable-dev-shm-usage")
#         options.add_argument("--no-sandbox")
#         self.driver = webdriver.Chrome(options=options, executable_path=ch)
#         self.domain = domain
#         self.url = url
#         self.driver.get(self.url)
#         # self.driver.implicitly_wait(10)
#         WebDriverWait(self.driver, 10)

#         body = self.driver.find_element_by_tag_name("body")
#         # body = self.driver.find_element(By.TAG_NAME ,"body")
#         print(body)
#         text = body.get_attribute("innerText")
#         # text = body["innerText"]

#         spaced_text = ""
#         for s in text:
#             if s == "\n":
#                 spaced_text += " "
#             elif s.isupper():
#                 spaced_text += s.lower()
#             else:
#                 spaced_text += s
#         self.words = spaced_text.split()
#         self.sentences = spaced_text.split('\n')
#         self.frequency = Counter(self.words)
#         self.befores = dict()
#         self.afters = dict()
#         for i in range(len(self.words)):
#             if i == 0:
#                 self.befores[self.words[i]] = [""]
#                 self.afters[self.words[i]] = [self.words[i+1]]
#                 continue

#             if i == len(self.words) - 1:
#                 if self.words[i] in self.befores.keys():
#                     self.befores[self.words[i]].append(self.words[i-1])
#                 else:
#                     self.befores[self.words[i]] = [self.words[i-1]]
#                 if self.words[i] in self.afters.keys():
#                     self.afters[self.words[i]].append("")
#                 else:
#                     self.afters[self.words[i]] = [""]
#                 continue

#             if self.words[i] in self.befores.keys():
#                 self.befores[self.words[i]].append(self.words[i-1])
#             else:
#                 self.befores[self.words[i]] = [self.words[i-1]]
#             if self.words[i] in self.afters.keys():
#                 self.afters[self.words[i]].append(self.words[i+1])
#             else:
#                 self.afters[self.words[i]] = [self.words[i+1]]

#     def get_links(self):
#         '''
#             Fetch all the a-tags in the webpage
#         '''

#         page_links = self.driver.find_elements_by_xpath("//a[@href]")

#         if len(page_links) == 0:
#             print("No links found!")
#             return

#         links = []
#         for link_el in page_links:
#             link = link_el.get_attribute("href")
#             if valid_link(link, self.domain):  # tested
#                 links.append(link)
#         return links

#     def get_words(self):
#         '''
#             Get all the words from the webpage
#         '''

#         return list(filter(lambda x: len(x) > 2 and all(char.isalpha() for char in x), self.words))

#     def get_numbers(self):
#         '''
#             Get all the numbers from the webpage
#         '''

#         return list(filter(lambda x: all(char.isdigit() for char in x), self.words))

#     def get_emails(self):
#         '''
#             Get all the emails from the webpage
#         '''

#         return list(filter(lambda x: re.match(r"[^@]+@[^@]+\.[^@]+", x), self.words))

#     def get_tables_as_list(self, start=None, end=None):
#         '''
#             Fetch all tables
#             Return content from tables no. "start" to table no. "end" as lists
#             [
#                 [
#                     [col1, col2, col3],
#                     [val1, val2, val3],
#                     [val4, val5, val6],
#                 ],
#                 [
#                     [col1, col2, col3],
#                     [val1, val2, val3],
#                     [val4, val5, val6],                    
#                 ]
#             ]
#         '''

#         tables = self.driver.find_elements_by_tag_name("table")
#         if len(tables) == 0:
#             print("No tables found!")
#             return

#         if end != None:
#             tables = tables[start:end]

#         content = []

#         for table in tables:
#             table_content = []

#             rows = table.find_elements_by_tag_name("tr")
#             for row in rows:
#                 row_content = []
#                 cols = row.find_elements_by_css_selector("*")
#                 for col in cols:
#                     row_content.append(col.text)
#                 table_content.append(row_content)
#             content.append(table_content)

#         return content

#     def get_tables_as_csv(self, start=None, end=None):
#         '''
#             Get Tables and save as csv file
#         '''

#         content = self.get_tables_as_list(start, end)

#         if len(content) == 0:
#             print("No tables found!")
#             return

#         with open(self.domain + "-tables.csv", "w", newline="") as new_file:
#             csv_writer = csv.writer(new_file)

#             for table in content:
#                 empty = ""
#                 for row in table:
#                     csv_writer.writerow(row)
#                 csv_writer.writerow(empty)

#     def get_images(self):
#         '''
#             Get all images from the website
#         '''

#         images = self.driver.find_elements_by_tag_name("img")
#         image_urls = []
#         for img in images:
#             xp = self.driver.execute_script("""gPt=function(c){
#                                  if(c.id!==''){
#                                      return'id("'+c.id+'")'
#                                  } 
#                                  if(c===document.body){
#                                      return c.tagName
#                                  }
#                                  var a=0;
#                                  var e=c.parentNode.childNodes;
#                                  for(var b=0;b<e.length;b++){
#                                      var d=e[b];
#                                      if(d===c){
#                                          return gPt(c.parentNode)+'/'+c.tagName+'['+(a+1)+']'
#                                      }
#                                      if(d.nodeType===1&&d.tagName===c.tagName){
#                                          a++
#                                      }
#                                  }
#                              };
#                              return gPt(arguments[0]).toLowerCase();""", img)
#             attr = self.driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', img)
#             one_attr = ""
#             for key,val in attr.items():
#                 one_attr = str(key) + "=" + str(val)
#                 break
#             image_urls.append(["src=" + img.get_attribute('src'), "xpath=" + xp, one_attr])

#         imgs = []
#         for x in image_urls:
#             imgs.append({"img": x})

#         return imgs

#         # try:
#         #     os.mkdir(find_last_name(self.url) + "-images")
#         # except:
#         #     pass
#         # index = 1
#         # for img in images:
#         #     src = img.get_attribute('src')
#         #     urllib.request.urlretrieve(
#         #         src, "./" + find_last_name(self.url) + "-images/" + find_last_name(src))
#         #     index += 1

#     def get_elements(self):
#         els = self.driver.find_elements_by_css_selector("*")
#         elements = []
#         flag = True
#         for el in els:
#             tg_name = el.tag_name
#             if tg_name == "body":
#                 flag = False
#             if flag or tg_name in ["br","hr"]:
#                 continue
#             temp = {tg_name: []}
#             xp = self.driver.execute_script("""gPt=function(c){
#                                  if(c.id!==''){
#                                      return'id("'+c.id+'")'
#                                  } 
#                                  if(c===document.body){
#                                      return c.tagName
#                                  }
#                                  var a=0;
#                                  var e=c.parentNode.childNodes;
#                                  for(var b=0;b<e.length;b++){
#                                      var d=e[b];
#                                      if(d===c){
#                                          return gPt(c.parentNode)+'/'+c.tagName+'['+(a+1)+']'
#                                      }
#                                      if(d.nodeType===1&&d.tagName===c.tagName){
#                                          a++
#                                      }
#                                  }
#                              };
#                              return gPt(arguments[0]).toLowerCase();""", el)
#             temp[tg_name].append("xpath=" + str(xp))

#             attr = self.driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', el)
#             i = 0
#             for key,val in attr.items():
#                 if i == 2:
#                     break
#                 one_attr = str(key) + "=" + str(val)
#                 temp[tg_name].append(one_attr)
#                 i += 1
#             elements.append(temp)
#         return elements

#     def get_tables(self):
#         tables = self.driver.find_elements_by_tag_name("table")
#         tbs = []
#         for table in tables:
#             xp = self.driver.execute_script("""gPt=function(c){
#                                  if(c.id!==''){
#                                      return'id("'+c.id+'")'
#                                  } 
#                                  if(c===document.body){
#                                      return c.tagName
#                                  }
#                                  var a=0;
#                                  var e=c.parentNode.childNodes;
#                                  for(var b=0;b<e.length;b++){
#                                      var d=e[b];
#                                      if(d===c){
#                                          return gPt(c.parentNode)+'/'+c.tagName+'['+(a+1)+']'
#                                      }
#                                      if(d.nodeType===1&&d.tagName===c.tagName){
#                                          a++
#                                      }
#                                  }
#                              };
#                              return gPt(arguments[0]).toLowerCase();""", table)
#             tbs.append(["xpath=" + xp, "rows:4", "columns:3"])

#         tbr = []
#         for x in tbs:
#             tbr.append({"table": x})

#         return tbr







# if __name__ == "__main__":

#     DEBUG11 = 0
#     url = sys.argv[1]
#     domain = sys.argv[2]



#     # files1 = open("heh.txt",'a')
#     # # files1.write(url)
#     # files1.write(domain)
#     # files1.close()




#     # obj = Webpage(url, domain)

#     # tables = obj.get_tables()
#     # if DEBUG11==1:

#     #     files1 = open("heh.txt",'w')
#     #     files1.write(tables)
#     #     files1.close()
#     # images = obj.get_images()
#     # if DEBUG11==1:

#     #     files1 = open("heh.txt",'w')
#     #     files1.write(images)
#     #     files1.close()
#     # elements = obj.get_elements()
#     # if DEBUG11==1:

#     #     files1 = open("heh.txt",'w')
#     #     files1.write(elements)
#     #     files1.close()
#     # links = []
#     # for x in elements:
#     #     if "a" in x.keys():
#     #         links.append(x)

#     result = dict()

#     # result["elements"] = elements
#     # result["tables"] = tables
#     # result["images"] = images
#     # result["links"] = links
#     # result["others"] = []



#     result = dict()

#     result["elements"] = []
#     result["tables"] = []
#     result["images"] = []
#     result["links"] = []
#     result["others"] = []

    
#     print(json.dumps(result))
    












