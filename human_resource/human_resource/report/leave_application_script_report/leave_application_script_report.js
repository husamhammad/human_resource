// Copyright (c) 2023, husam hammad and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["leave application script report"] = {
	"filters": [
		{
			"fieldname": "leave_type",
			"label": __("Leave Type"),
			"fieldtype": "Link",
			"options": "Leave Type"
		}

	]
};
