from __future__ import unicode_literals
import frappe

# @frappe.whitelist()
# def test_api(first_name=None):
#     employees = []
#     if first_name:
#      employees = frappe.db.sql(""" Select * From `tabEmployee` Where first_name Like "{0}" """.format(first_name), as_dict=True)
#     return employees

#################################################################################3
#Function To Create Attendance For Employee When Make Request By Using Api

@frappe.whitelist()
def create_attendance(attendance_date, check_in, check_out, user=""):
    # Check If The Required Fields Are Present
    if  not attendance_date or not check_in or not check_out:
        frappe.throw("Attendance Date, Check In, and Check Out are required")

    # Check If User Does Not Put User Id In Parameter Request In Api
    if user =="":
       user = frappe.session.user

    # Create New Attendance Record For The Requesting Employee
    new_attendance = frappe.new_doc("Attendance")
    new_attendance.employee = frappe.get_doc("Employee", {"user": user}).name
    new_attendance.attendance_date = attendance_date
    new_attendance.check_in = check_in
    new_attendance.check_out = check_out
    new_attendance.insert()
    return {"message": "Attendance created successfully "}

