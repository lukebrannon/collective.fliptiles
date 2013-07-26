$(function(){

    $(".myFlippyCard").on("hover",function(e){
        $(".flipbox").flippyReverse();
        e.preventDefault();
    });
});
