// Copyright (c) 2023, husam hammad and contributors
// For license information, please see license.txt

frappe.ui.form.on("Attendance", {
// 	refresh(frm) {

// 	},

attendance_date: function (frm) {
    frm.trigger("get_work_hours");
},
check_in: function (frm) {
    frm.trigger("get_work_hours");

},
check_out: function (frm) {
    frm.trigger("get_work_hours");
        
},

// Frappe Ajax Call To Find Work Hours For The User
get_work_hours: function (frm) {
    if (!frm.doc.attendance_date | !frm.doc.check_in | !frm.doc.check_out ) {
        return;
    }
    frappe.call({
        method: "human_resource.human_resource.doctype.attendance.attendance.get_work_hours",
        args: {
            attendance_date: frm.doc.attendance_date,
            check_in: frm.doc.check_in,
            check_out: frm.doc.check_out,
        },
        callback: (r) => {
            frm.doc.work_hours = r.message[0];
            frm.doc.late_hours = r.message[1]
            frm.refresh()
            console.log("Successfully Ajax Call")
        }
    })
},

});
