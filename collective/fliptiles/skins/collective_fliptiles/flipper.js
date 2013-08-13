$(function() {
    
    $('.quickFlip').quickFlip();
    
    for ( var i = 0; i < $.quickFlip.wrappers.length; i++ ) {
        var thisOne = $.quickFlip.wrappers[i];

    $( thisOne.wrapper ).hover( function(ev) {
        var $target = $(ev.target);

    if ( !$target.hasClass('quickFlip') ) $target = $target.parent();
                      
    $target.quickFlipper();
                                    
    }, function() {});
}
});
