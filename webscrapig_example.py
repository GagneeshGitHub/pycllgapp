import requests
from bs4 import BeautifulSoup

url = "https://www.himtu.ac.in/"

req = requests.get(url)

soup = BeautifulSoup(req.content, "html.parser")

# Menus
id_home = soup.find(id="home")
menu1 = soup.find(id="menu1")
menu2 = soup.find(id="menu2")

home_list = id_home.find_all('a')
menu1_list = menu1.find_all('a')
menu2_list = menu2.find_all('a')

work_dict = {}

string_name = "home"
string_name2 = "menu"
string_name3 = "common"
i = 1

for item in home_list:
	list_one = []
	list_one.append(item.text)
	list_one.append(item.get("href"))
	work_dict[string_name+str(i)] = list_one
	i=i+1
	
for item in menu1_list:
	list_one = []
	list_one.append(item.text)
	list_one.append(item.get("href"))
	work_dict[string_name2+str(i)] = list_one
	i=i+1
	
for item in menu2_list:
	list_one = []
	list_one.append(item.text)
	list_one.append(item.get("href"))
	work_dict[string_name3+str(i)] = list_one
	i=i+1

print(work_dict)


