import flet as ft

def main(page: ft.Page):
	def addTask(p):
		checkBox = ft.Checkbox(value= False)
		checkBoxText = ft.Text(value=textField.value, color="black",size= 15, width=350,bgcolor="white")
		taskRow = ft.Row(controls=[checkBox, checkBoxText], alignment= ft.MainAxisAlignment.START)
		page.add(taskRow)
		# TODO clear the text field

	def editTask(p):
		

	def deleteTask(p):
		pass


	page.window_height = 400
	page.window_width = 700
	page.bgcolor = "#CCD5AE"

	textField = ft.TextField(hint_text="Please enter text here", width=350, height=50,) # TODO add keyboard enter event
	addBtn = ft.ElevatedButton(text="Add", color="green", on_click=addTask) 

	checkBox = ft.Checkbox(value= True, fill_color="blue")
	checkBoxText = ft.Text(value="Task 1", color="black",size= 15, width=350,bgcolor= "white")

	# ft.Row(controls=[textField, addBtn])# This is also valid
	taskRow = ft.Row(controls=[checkBox, checkBoxText], alignment= ft.MainAxisAlignment.START)
	entriesRow = ft.Row(controls=[textField, addBtn], alignment= ft.MainAxisAlignment.SPACE_BETWEEN) #Stacks the controls horizontally
	
	page.add(entriesRow)
	# page.add(entriesRow, taskRow)

	# * page.add(textField, addBtn) # This is also valid


ft.app(target=main)