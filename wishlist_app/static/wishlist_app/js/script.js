$(function() {
	var rangePercent = $('[type="range"]').val();
	$('[type="range"]').on('change input', function() {
		rangePercent = $('[type="range"]').val();
		$('h4').html(rangePercent+'<span></span>');
		$('[type="range"], h4>span').css('filter', 'hue-rotate(-' + rangePercent + 'deg)');
		$('h4').css({'transform': 'translateX(-50%) scale(' + (1) + ')'});
	});
});