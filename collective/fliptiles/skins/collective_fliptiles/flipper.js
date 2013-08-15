$(function() {
    
    $('.quickFlip').quickFlip();

    $('.quickFlip').hover(
    		function() {
    			$(this).quickFlipper();
    		});
});
