$(document).ready(function() {	
	$(".ImgSel").click(function() { 
		$('.ImgSel').removeClass('ImgSelChoice');
		$(this).addClass('ImgSelChoice');
		$(this).css('border-width', '5px'); 
	});
	
	$(".optionSel").click(function() { 
		$('.optionSel').removeClass('optionSelChoice');
		$(this).addClass('optionSelChoice');
		$(this).css('border-width', '5px'); 
	});
})