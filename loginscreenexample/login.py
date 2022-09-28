from kivymd.app import MDApp
from kivy.properties import StringProperty,ListProperty
from kivymd.uix.screen import MDScreen

import requests

import ssl

name = ""

course = StringProperty("NoCourse")

branch = StringProperty("NoBranch")

login_id = ""

student_login_id = ""

student_roll_no = ""

class MainScreen(MDScreen):
	global name
	global student_login_id
	global student_roll_no
	global course
	global branch
	def __init__(self, **kwargs):
		super().__init__()
		self.course_value = ['First Select Course']

	def spinner_clicked(self, value):
		branch = str(value) 
		print('Value of course is: ' + str(course))
		if value == "B.Tech": 
			self.course_value = ['CSE','EEE','CIVIL','MECHANICAL','IT','E&C']
			self.ids.spinner_course.values = self.course_value
		elif value == "Polytechnic":
			self.course_value = ['CSE','EEE','CIVIL','MECHANICAL','E&C','AUTOMOBLE','D.Pharmacy']
			self.ids.spinner_course.values = self.course_value
		elif value == "M.Tech":
			self.course_value = ['CIVIL','CSE']
			self.ids.spinner_course.values = self.course_value
	
	def spinner_clicked2(self,value):
		course = str(value)

	def submit_values(self,name_r,rollnum,login):
		ssl._create_default_https_context = ssl._create_unverified_context

		name = name_r
		student_roll_no = rollnum
		student_login_id = login
		student_roll_no = student_roll_no.upper()
		student_login_id = student_login_id.upper()

		values = {'Name': name, 'RollNumber': student_roll_no, 'LoginId': student_login_id, 'Course':course, 'Branch':branch}

		reply_page = requests.get('https://localhost/sirdaseva/student_login.php',params=values)

		print("Function Executed Successfully")

		print(reply_page)


class LoginApp(MDApp):
	pass

if __name__ == "__main__":
	LoginApp().run()
