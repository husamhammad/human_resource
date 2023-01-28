# Copyright (c) 2023, husam hammad and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters ):
	columns, data = [], []
	data = get_all_leave_application(filters)
	columns = get_columns()
	return columns, data


def get_all_leave_application(filters):
	return frappe.db.get_all("Leave Application", 
	['employee_name','leave_type', 'from_date', 'to_date'],filters)


def get_columns():
	columns = [{
    "fieldname": "employee_name",
    "label": _("Employee Name"),
    "fieldtype": "Data",
},
{
    "fieldname": "leave_type",
    "label": _("Leave Type"),
    "fieldtype": "Link",
    "options": "Leave Type",
},
{
    "fieldname": "from_date",
    "label": _("From Date"),
    "fieldtype": "Date",
    "options": "Leave Type",
},
{
    "fieldname": "to_date",
    "label": _("To Date"),
    "fieldtype": "Date",
}
] 
	return columns