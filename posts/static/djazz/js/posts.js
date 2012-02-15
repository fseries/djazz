$(document).ready(function(){
	var row1 = ""
	var row2 = ""
	row1 += "formatselect"
	row1 += ",|,bold,italic,underline"
	row1 += ",|,justifyleft,justifycenter,justifyright,justifyfull"
	row1 += ",|,bullist,numlist"
	row1 += ",|,outdent,indent"
	row1 += ",|,hr"
	
	tinyMCE.init({
		mode : "exact",
		elements: "id_content",
		theme : "advanced",
		theme_advanced_buttons1 : row1,
        theme_advanced_buttons2 : row2,
        theme_advanced_buttons3 : "",
		theme_advanced_blockformats : "h2,h3,h4,h5,h6,blockquote,code",
        theme_advanced_toolbar_location : "top",
        theme_advanced_toolbar_align : "left",
        theme_advanced_statusbar_location : "bottom",
        theme_advanced_resizing : true
	});
	
	$("#id_content").before('<input type="button" name="content_switch" value="switch html"><br />');
	$("#id_content").data('switch','editor');
	$("input[name=content_switch]").click(function(){
		if( $("#id_content").data('switch') == "editor" ) {
			tinyMCE.get("id_content").hide();
			$("#id_content").data('switch','textarea');
			$("input[name=content_switch]").val('switch editor');
		} else if( $("#id_content").data('switch') == "textarea" ){
			tinyMCE.get("id_content").show();
			$("#id_content").data('switch','editor');
			$("input[name=content_switch]").val('switch html');
		}
	});
});
