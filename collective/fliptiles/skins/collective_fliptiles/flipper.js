$(function() {
    
    $('.tileFlip').quickFlip();
    
    for ( var i = 0; i < $.quickFlip.wrappers.length; i++ ) {
        var thisOne = $.quickFlip.wrappers[i];

    $( thisOne.wrapper ).click( function(ev) {
        var $target = $(ev.target);

    if ( !$target.hasClass('tileFlip') ) $target = $target.parent();
                      
    $target.quickFlipper();
                                    
    }, function() {});
}
});
