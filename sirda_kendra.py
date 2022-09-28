from kivymd.app import MDApp
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer
from kivymd.uix.button import MDRectangleFlatIconButton, MDFloatingActionButtonSpeedDial, MDRectangleFlatButton, MDRaisedButton, MDFillRoundFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.tab import MDTabsBase
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.tabbedpanel import TabbedPanel
import webbrowser
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
import threading
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
import time
import sqlite3
from kivy.uix.image import Image

from kivy.uix.boxlayout import BoxLayout


from kivy.uix.widget import Canvas
from kivy.graphics import Ellipse

#For MdTabs
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase


#Students Branch and Course
branch = "B.Tech"
course = "CSE"

current_screen = StringProperty('Sirda')
run_thread = True

#Thread for webScraping
web_threading = threading.Thread()

dic_hptu_list = {}
add_buttons = True
can_run_refresh = True

# Used for nsb etc
a_b_dict = {'home1': ('None','None'), 
		'home2': ('None','None'),
		'home3': ('None','None'),
		'home4': ('None','None'),
		'menu1': ('None','None'),
		'menu2': ('None','None'),
		'menu3': ('None','None'),
		'menu4': ('None','None'),
		'common1': ('None','None'),
		'common2': ('None','None')}

def st_thread():
	print("Funciton is executed")
	global web_threading
	web_threading = threading.Thread(target=web_scrap_hptu)
	web_threading.start()
	print("Thread has started")

def web_scrap_hptu():
	global can_run_refresh
	app = MDApp.get_running_app()
	add_buttons = False
	url = "https://www.himtu.ac.in/"
	try:	
		req = requests.get(url)
		web_scrap(req)
		app.root.ids.refresh_btn.disabled = True
	except ConnectionError as e:
		can_run_refresh = True
		app.root.ids.refresh_btn.disabled = False
		print(e)
		


def web_scrap(req):
	global run_thread
	global add_buttons
	global dic_hptu_list
	global run_while_loop
	soup = BeautifulSoup(req.content, "html.parser")
	add_buttons = True

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
	i = 1	

	for item in menu1_list:
		list_one = []
		list_one.append(item.text)
		list_one.append(item.get("href"))
		work_dict[string_name2+str(i)] = list_one
		i=i+1
	i = 1

	for item in menu2_list:
		list_one = []
		list_one.append(item.text)
		list_one.append(item.get("href"))
		work_dict[string_name3+str(i)] = list_one
		i=i+1
	run_thread = False
	dic_hptu_list = work_dict
	btn_names()
	assigning_btnnames()


def assigning_btnnames():
	time.sleep(6)
	app = MDApp.get_running_app()
	app.root.ids.nfb_id.refresh_fun()
	app.root.ids.nsb_id.refresh_fun()
	app.root.ids.ntb_id.refresh_fun()
	app.root.ids.nfob_id.refresh_fun()
	app.root.ids.afb_id.refresh_fun()
	app.root.ids.asb_id.refresh_fun()
	app.root.ids.atb_id.refresh_fun()
	app.root.ids.afob_id.refresh_fun()
	app.root.ids.ofb_id.refresh_fun()
	app.root.ids.osb_id.refresh_fun()

def btn_names():
	global dic_hptu_list
	global a_b_dict
	a_b_dict['home1'] = dic_hptu_list['home1']
	a_b_dict['home2'] = dic_hptu_list['home2']
	a_b_dict['home3'] = dic_hptu_list['home3']
	a_b_dict['home4'] = dic_hptu_list['home4']
	a_b_dict['menu1'] = dic_hptu_list['menu1']
	a_b_dict['menu2'] = dic_hptu_list['menu2']
	a_b_dict['menu3'] = dic_hptu_list['menu3']
	a_b_dict['menu4'] = dic_hptu_list['menu4']
	a_b_dict['common1'] = dic_hptu_list['common1']
	a_b_dict['common2'] = dic_hptu_list['common2']
	print('Assignment is Complete')
	print(a_b_dict)

# MD Tabs
class HptuTab1(FloatLayout,MDTabsBase):
	pass


# Main Screen Class
class TheMainScreen(MDScreen):
	pass

# NavigationLayout
class NavLayout(MDNavigationLayout):
	pass

# NavigationDrawer
class ScrDrawer(MDNavigationDrawer):
	pass

# Screen Manager Class
class ScrManager(ScreenManager):
	def change_current(self,value):
		print("Changing Current Value Is Called")
		self.current = value

# Screen Of ScreenManager
class NHScreen(MDScreen):
	# Defines summaary of all the notification
	def on_enter(self):
		global run_thread
		print("Value of run_thread is")
		print(run_thread)
		if run_thread == True:
			st_thread()

class Sirda(MDScreen):
	def on_enter(self):
		global run_thread
		print("Value of run_thread is")
		print(run_thread)
		if run_thread == True:
			st_thread()

class Hptu(MDScreen):
	def on_enter(self):
		global run_thread
		print("Value of run_thread is")
		print(run_thread)
		if run_thread == True:
			st_thread()

class HptuTab(TabbedPanel):
	def on_enter(self):
		global run_thread
		print("Value of run_thread is")
		print(run_thread)
		if run_thread == True:
			st_thread()

#Buttons for all types of notification
class cir_refresh_btn(Button):
	global can_run_refresh
	def on_press(self):
		if(can_run_refresh):
			can_run_refresh = False
			web_scrap_hptu()
		

class NFB(MDFillRoundFlatButton):
	tex_nfb = StringProperty('None')
	url = StringProperty('None')
	def refresh_fun(self):
		self.ra_var = 1
		self.url = a_b_dict['home1'][1]
		ra_text = a_b_dict['home1'][0]
		self.tex_nfb= ''
		for i in ra_text:
			self.tex_nfb = self.tex_nfb + i
			if (self.ra_var/32 == 1):
				self.tex_nfb = self.tex_nfb + "-\n"
				self.ra_var = 1
			self.ra_var = self.ra_var + 1

	def open_browser(self):
		webbrowser.open(self.url)

class NSB(MDFillRoundFlatButton):
	tex_nsb = StringProperty('None')
	url = StringProperty('None')
	def refresh_fun(self):
		self.ra_var = 1
		self.url = a_b_dict['home2'][1]
		ra_text = a_b_dict['home2'][0]
		self.tex_nsb= ''
		for i in ra_text:
			self.tex_nsb = self.tex_nsb + i
			if (self.ra_var/32 == 1):
				self.tex_nsb = self.tex_nsb + "-\n"
				self.ra_var = 1
			self.ra_var = self.ra_var + 1

	def open_browser(self):
		webbrowser.open(self.url)

class NTB(MDFillRoundFlatButton):
	tex_ntb = StringProperty('None')
	url = StringProperty('None')
	def refresh_fun(self):
		self.ra_var = 1
		self.url = a_b_dict['home3'][1]
		ra_text = a_b_dict['home3'][0]
		self.tex_ntb= ''
		for i in ra_text:
			self.tex_ntb = self.tex_ntb + i
			if (self.ra_var/32 == 1):
				self.tex_ntb = self.tex_ntb + "-\n"
				self.ra_var = 1
			self.ra_var = self.ra_var + 1

	def open_browser(self):
		webbrowser.open(self.url)

class NFoB(MDFillRoundFlatButton):
	tex_nfob = StringProperty('None')
	url = StringProperty('None')
	def refresh_fun(self):
		self.ra_var = 1
		self.url = a_b_dict['home4'][1]
		ra_text = a_b_dict['home4'][0]
		self.tex_nfob= ''
		for i in ra_text:
			self.tex_nfob = self.tex_nfob + i
			if (self.ra_var/32 == 1):
				self.tex_nfob = self.tex_nfob + "-\n"
				self.ra_var = 1
			self.ra_var = self.ra_var + 1

	def open_browser(self):
		webbrowser.open(self.url)

class AFB(MDFillRoundFlatButton):
	tex_afb = StringProperty('None')
	url = StringProperty('None')
	def refresh_fun(self):
		self.ra_var = 1
		self.url = a_b_dict['menu1'][1]
		ra_text = a_b_dict['menu1'][0]
		self.tex_afb= ''
		for i in ra_text:
			self.tex_afb = self.tex_afb + i
			if (self.ra_var/32 == 1):
				self.tex_afb = self.tex_afb + "-\n"
				self.ra_var = 1
			self.ra_var = self.ra_var + 1

	def open_browser(self):
		webbrowser.open(self.url)

class ASB(MDFillRoundFlatButton):
	tex_asb = StringProperty('None')
	url = StringProperty('None')
	
	def refresh_fun(self):
		self.ra_var = 1
		self.url = a_b_dict['menu2'][1]
		ra_text = a_b_dict['menu2'][0]
		self.tex_asb= ''
		for i in ra_text:
			self.tex_asb = self.tex_asb + i
			if (self.ra_var/32 == 1):
				self.tex_asb = self.tex_asb + "-\n"
				self.ra_var = 1
			self.ra_var = self.ra_var + 1

	def open_browser(self):
		webbrowser.open(self.url)

class ATB(MDFillRoundFlatButton):
	tex_atb = StringProperty('None')
	url = StringProperty('None')

	def refresh_fun(self):
		self.ra_var = 1
		self.url = a_b_dict['menu3'][1]
		ra_text = a_b_dict['menu3'][0]
		self.tex_atb= ''
		for i in ra_text:
			self.tex_atb = self.tex_atb + i
			if (self.ra_var/32 == 1):
				self.tex_atb = self.tex_atb + "-\n"
				self.ra_var = 1
			self.ra_var = self.ra_var + 1

	def open_browser(self):
		webbrowser.open(self.url)

class AFoB(MDFillRoundFlatButton):
	tex_afob = StringProperty('None')
	url = StringProperty('None')

	def refresh_fun(self):
		self.ra_var = 1
		self.url = a_b_dict['menu4'][1]
		ra_text = a_b_dict['menu4'][0]
		self.tex_afob= ''
		for i in ra_text:
			self.tex_afob = self.tex_afob + i
			if (self.ra_var/32 == 1):
				self.tex_afob = self.tex_afob + "-\n"
				self.ra_var = 1
			self.ra_var = self.ra_var + 1

	def open_browser(self):
		webbrowser.open(self.url)

class OFB(MDFillRoundFlatButton):
	tex_ofb = StringProperty('None')
	url = StringProperty('None')

	def refresh_fun(self):
		self.ra_var = 1
		self.url = a_b_dict['common1'][1]
		ra_text = a_b_dict['common1'][0]
		self.tex_nfb= ''
		for i in ra_text:
			self.tex_ofb = self.tex_ofb + i
			if (self.ra_var/32 == 1):
				self.tex_ofb = self.tex_ofb + "-\n"
				self.ra_var = 1
			self.ra_var = self.ra_var + 1

	def open_browser(self):
		webbrowser.open(self.url)

class OSB(MDFillRoundFlatButton):
	tex_osb = StringProperty('None')
	url = StringProperty('None')

	def refresh_fun(self):
		self.ra_var = 1
		self.url = a_b_dict['common2'][1]
		ra_text = a_b_dict['common2'][0]
		self.tex_osb= ''
		for i in ra_text:
			self.tex_osb = self.tex_osb + i
			if (self.ra_var/32 == 1):
				self.tex_osb = self.tex_osb + "-\n"
				self.ra_var = 1
			self.ra_var = self.ra_var + 1

	def open_browser(self):
		webbrowser.open(self.url)

class FacultyMembers(MDScreen):
	def on_enter(self):
		add_faculties()

def add_faculties():
	global list_faculties_for_me
	app = MDApp.get_running_app()
	for item in list_faculties_for_me:
		name = item[0]
		semester = item[1]
		branch = item[2]

		label = Faculty_label(name,branch)
		faculty = Faculty_layout()
		photo = Photo(faculty.pos,"faculty_images/nodp.jpg")		
		faculty.add_widget(photo)	
		faculty.add_widget(label)		

		app.root.ids.faculty_grid.add_widget(faculty)	
		

# Widget for faculty memeber

class Photo(Image):
	def __init__(self,pos,img_source,**kwargs):
		super().__init__(**kwargs)
		self.size_hint = (None,None)
		self.width = "100dp"
		self.height = "100dp" 
		self.allow_stretch = True
		#self.pos = pos
		self.source = img_source

class Faculty_label(Label):
	def __init__(self,name,branch,**kwargs):
		super().__init__(**kwargs)
		self.color = [0,0,0,1]
		self.font_size = 20	
		self.markup = True
		self.text = "[b]Name: [/b]"+name+"\n[b]Branch: [/b]"+branch
		
		

class Faculty_layout(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.orientation = "horizontal"
		self.size_hint = (1,None)
		self.height = "50dp"
		


class Fees(MDScreen):
	pass

# BoxLayout classes for Screen Drawer
class NavBoxLayout(MDBoxLayout):
	pass

class NavBoxLayoutHor(MDBoxLayout):
	pass

# Buttons for Drawer
class NHScreenBtn(MDRectangleFlatIconButton):	
	pass

class PaymentBtn(MDRectangleFlatIconButton):
	pass

class HptuBtn(MDRectangleFlatIconButton):
	pass

class SirdaBtn(MDRectangleFlatIconButton):
	pass

class FacultyMembersBtn(MDRectangleFlatIconButton):
	pass

class FeesBtn(MDRectangleFlatIconButton):
	pass


# Payment Buttons
class SemFees(Button):
	def open_browser(self):
		webbrowser.open("Payment/fees.html")

class UdfFees(Button):
	def open_browser(self):
		webbrowser.open("Payment/fees.html")


#Changing Screen
def change_screen(value):
	global current_screen
	current_screen = StringProperty(value)

# Mini Layout inside drawer
class MiniHorizontal(MDBoxLayout):
	pass

class MiniVertical(MDGridLayout):
	pass

# Inside Components Of Screen
class HptuGridLayout(MDGridLayout):
	pass

def go_to_website():
	pass

# Main App Class
class SirdaApp(MDApp):
	global db_conn
	global course
	def on_start(self):
		course = "%CSE%"
		db_conn = sqlite3.connect("Database/sirdadatabase.db")
		faculty_selector(db_conn)

# Selecting Faculties
def faculty_selector(db_conn):
	global list_faculties_for_me
	global course
	c = db_conn.cursor()
	c.execute("SELECT * FROM teachers WHERE branch LIKE (?)",(course,))
	list_faculties_for_me = c.fetchall()

if __name__ == '__main__': 
	SirdaApp().run()
