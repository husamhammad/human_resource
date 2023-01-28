// Copyright (c) 2023, husam hammad and contributors
// For license information, please see license.txt

frappe.ui.form.on("leave Allocation", {
    from_date:function(frm){
        frm.trigger("get_total_leaves");
    
    
    },
    to_date:function(frm){
        frm.trigger("get_total_leaves");
    
    
    },

    ///// Get Total Leaves Api From File leave_application.py /////

get_total_leaves:function(frm){
    if (!frm.doc.from_date|!frm.doc.to_date ){
        return;
    }
    
    frappe.call({
        method:"human_resource.human_resource.doctype.leave_allocation.leave_allocation.det_diff_date",
        args:{
            from_date:frm.doc.from_date,
            to_date:frm.doc.to_date

        },
        callback:(r) => {
            frm.doc.total_leaves_allocated = r.message;
            frm.refresh()
        }
    })
},

});
