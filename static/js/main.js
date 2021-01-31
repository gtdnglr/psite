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

var map = new ol.Map({
    target: 'map',
    layers: [
        new ol.layer.Tile({
            source: new ol.source.OSM()
        })
    ],
    view: new ol.View({
        center: ol.proj.fromLonLat([-84.388168, 33.748783]),
        zoom: 8
    })
});

