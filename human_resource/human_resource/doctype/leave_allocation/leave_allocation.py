# Copyright (c) 2023, husam hammad and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model. document import Document
from frappe import _
from frappe.utils import date_diff

class leaveAllocation(Document):
  def validate(self):
      self.check_the_date()
      self.set_total_leave_days()
      self.check_existing_allocation()
  
  

  def check_the_date(self):
        if self.from_date and self.to_date:
            if self.from_date > self.to_date:
               frappe.throw(_("From date cannot be after To date"))
            else :return 1
        else: frappe.throw(_("you must select From and To Date"))



  def set_total_leave_days(self):
        if self.to_date and self.from_date:
             total_leave_days = frappe.utils.date_diff(self.to_date, self.from_date)+1
             if total_leave_days >=0:
                self.total_leaves_allocated = total_leave_days
             else: frappe.throw(("The total leave days can not be less 0"))
        else:frappe.throw(("you must select From and To Date"))


  def check_existing_allocation(self):
        existing_allocation = frappe.db.exists("leave Allocation", {
            "employee": self.employee,
            "leave_type": self.leave_type,
            "from_date": ["<=", self.from_date],
            "to_date": [">=", self.to_date]
        })
        if existing_allocation:
            frappe.throw(_("Leave allocation already exists for the selected dates, employee and leave type"))


@frappe.whitelist()
def det_diff_date(from_date, to_date):
    if to_date and from_date:
            total_leave_day = date_diff(to_date,from_date) +1
            if total_leave_day >=0:
                total_leave_days = total_leave_day
                return int(total_leave_days)            
