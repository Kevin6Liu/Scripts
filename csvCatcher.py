from bs4 import BeautifulSoup
import requests

# with open("index.html", "r") as f:
#     doc = BeautifulSoup(f,"html.parser")


# print(doc.prettify())
# tags = doc.find_all("p")[0]

# print(type(tags))
 
GROUP_NUM = 150

url = "http://gbman0mms001.nme.nexperia.com/template/DCF_Dcflist.html?Diagmode=0"

linkHead = "http://gbman0mms001.nme.nexperia.com/template/"

first_level_result = requests.get(url)

doc = BeautifulSoup(first_level_result.text, "html.parser")

# Tree leaves
# 665 li elements

groups = doc.find_all("li")
# print(linkHead + groups[500].a.get('href'))

second_level_link = linkHead + groups[GROUP_NUM].a.get('href')

# Opens the root folder
second_level_result = requests.get(second_level_link)

doc2 = BeautifulSoup(second_level_result.text, "html.parser")

groups2 = doc2.find_all("li")

# Find the link to the sub folder
target_link = linkHead + groups2[GROUP_NUM].ul.li.a.get('href')

final_level_result = requests.get(target_link)

doc3 = BeautifulSoup(final_level_result.text, "html.parser")

groups3 = doc3.find(id = 'MainTable')

print(groups3.tbody.tr.td.a.get('id'))
