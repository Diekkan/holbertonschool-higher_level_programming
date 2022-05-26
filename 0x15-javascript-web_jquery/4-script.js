$(function() {
    $('#toggle_header').click(function(){
        if ($('header').attr('class') == 'red'){
            $('header').removeClass("red");
            $('header').addClass("green");
        } else {
            $('header').removeClass("green");
            $('header').addClass("red");
        }
    });
});