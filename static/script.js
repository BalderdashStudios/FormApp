$(document).ready(function() {	
	$(".ImgSel").click(function() { 
		$('.ImgSel').removeClass('ImgSelChoice');
		$(this).addClass('ImgSelChoice');
		$(this).css("filter", "grayscale(100%)");
		$(this).css('border-width', '5px'); 
	});
})