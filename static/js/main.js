$(document).ready(function () {
	var mainnav = $('#main-nav-section');
	var origOffsetY = mainnav.offset().top;

	function scroll() {
		if ($(window).scrollTop() >= origOffsetY) {
		$('#main-nav-section').addClass('fixed-top');
		} else {
			$('#main-nav-section').removeClass('fixed-top');
			$('#grey-under-bar').css('height', '25px');
		}
	}
	document.onscroll = scroll;
});

