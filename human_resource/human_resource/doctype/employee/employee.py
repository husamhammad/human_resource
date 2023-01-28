# Copyright (c) 2023, husam hammad and contributors
# For license information, please see license.txt

from frappe import *
from frappe.model.document import Document
from datetime import datetime
class Employee(Document):

 def validate(doc): 
  doc.calucate_dob()
  doc.check_status()
 
 
 def calucate_dob(doc):  
    if doc.date_of_brith:
      today = datetime.now()
      dob = datetime.strptime(doc.date_of_brith, '%Y-%m-%d')
      doc.age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    else:
        throw("choose your birthday")



 def check_status(doc):
        if doc.status == "Active" and doc.age >= 60 :
            throw("Cannot save employee with active status and age 60 ")
        
    




