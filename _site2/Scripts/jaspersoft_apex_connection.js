var report_server = "";

var report_name = "Employees_with_param";
var report_format = "pdf";
var data_source = "default";

var ap_1 = $v("P11_DEPT");
var rp_1 = "&P_DEPT";

var param = "" + rp_1 + "=" + ap_1 + "";

var report = "" + report_server +"&_repName=" + report_name  +"&_repFormat=" + report_format + &"&_dataSource=" + data_source + "";

var run_report = "" + report + "" param + "";

window.open(run_report)
