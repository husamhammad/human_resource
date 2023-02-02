# Copyright (c) 2023, husam hammad and contributors
# For license information, please see license.txt

# Copyright (c) 2023, mahmood and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document
from datetime import datetime


class Attendance(Document):
	
	def on_submit(self):
		self.get_work_hours()
		self.update_status()
		

	def get_work_hours(self):
		if self.check_out and self.check_in:
			# Get All Values From Doctypes And Convert It In Time Formate

			start_time = datetime.strptime(str(frappe.db.get_single_value('Attendance Settings', 'start_time')), '%H:%M:%S')
			end_time = datetime.strptime(str(frappe.db.get_single_value('Attendance Settings', 'end_time')), '%H:%M:%S')
			late_entry_grace_period = frappe.db.get_single_value('Attendance Settings', 'late_entry_grace_period')
			early_exit_grace_period = frappe.db.get_single_value('Attendance Settings', 'early_exit_grace_period')
			check_in = datetime.strptime(self.check_in, '%H:%M:%S')
			check_out = datetime.strptime(self.check_out, '%H:%M:%S')

			# Calculate Check In Time With Start Time And Late In The Entry Values

			late_in_the_entry_hours = start_time.hour - check_in.hour 
			late_in_the_entry_minutes = start_time.minute - check_in.minute  + late_entry_grace_period
			late_in_the_entry = late_in_the_entry_hours - (-late_in_the_entry_minutes / 60)
			
			# Calculate Check Out Time With End Time And Early In The Exit Values

			early_in_the_exit_hours = check_out.hour - end_time.hour  
			early_in_the_exit_minutes =  end_time.minute - check_out.minute - early_exit_grace_period
			early_in_the_exit = early_in_the_exit_hours - (early_in_the_exit_minutes / 60)

			#Compare The Late In The Entey And Early In The Exit Values

			if late_in_the_entry > 0: late_in_the_entry = 0
			if early_in_the_exit > 0: early_in_the_exit = 0

			# Set The Fields Values 
			self.late_hours = -late_in_the_entry + -early_in_the_exit
			self.work_hours = 8 - self.late_hours
			frappe.msgprint(f'Attendance For <b>{self.employee_name}</b> inserted successfully')

		else:
			frappe.throw("Attendance Date, Check In, and Check Out are required")


	# Function To Uddate Status In Attendance Doctype
	def update_status(self):
		working_hours_threshold_for_absent = frappe.db.get_single_value('Attendance Settings','working_hours_threshold_for_absent')
		if self.work_hours <=  working_hours_threshold_for_absent:
			self.status = "Absent"
		else:
			self.status = "Present"



@frappe.whitelist()
def get_work_hours(attendance_date,check_out,check_in):
		if check_out and check_in:
			# Get All Values From Doctypes And Convert It In Time Formate

			start_time = datetime.strptime(str(frappe.db.get_single_value('Attendance Settings', 'start_time')), '%H:%M:%S')
			end_time = datetime.strptime(str(frappe.db.get_single_value('Attendance Settings', 'end_time')), '%H:%M:%S')
			late_entry_grace_period = frappe.db.get_single_value('Attendance Settings', 'late_entry_grace_period')
			early_exit_grace_period = frappe.db.get_single_value('Attendance Settings', 'early_exit_grace_period')
			check_in = datetime.strptime(check_in, '%H:%M:%S')
			check_out = datetime.strptime(check_out, '%H:%M:%S')

			# Calculate Check In Time With Start Time And Late In The Entry Values

			late_in_the_entry_hours = start_time.hour - check_in.hour 
			late_in_the_entry_minutes = start_time.minute - check_in.minute  + late_entry_grace_period
			late_in_the_entry = late_in_the_entry_hours - (-late_in_the_entry_minutes / 60)
			
			# Calculate Check Out Time With End Time And Early In The Exit Values

			early_in_the_exit_hours = check_out.hour - end_time.hour  
			early_in_the_exit_minutes =  end_time.minute - check_out.minute - early_exit_grace_period
			early_in_the_exit = early_in_the_exit_hours - (early_in_the_exit_minutes / 60)

			#Compare The Late In The Entey And Early In The Exit Values

			if late_in_the_entry > 0: late_in_the_entry = 0
			if early_in_the_exit > 0: early_in_the_exit = 0

			# Set The Fields Values 
			late_hours = -late_in_the_entry + -early_in_the_exit
			work_hours = 8 - late_hours
			return  work_hours , late_hours