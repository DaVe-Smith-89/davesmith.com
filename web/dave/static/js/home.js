
$(document).ready(function(){
    $('#about').click(function(){
        if($(window).width() < 450){
            $('.navigations').toggle(500,);
            window.scroll(0, 700);
        } else {
            window.scroll(0, 450);
        }
    });
    $('#languages').click(function(){
        if($(window).width() < 450){
            $('.navigations').toggle(500,);
            window.scroll(0, 1300);
        } else {
            window.scroll(0, 900);
        }
    });
    $('#contact').click(function(){
        if($(window).width() < 450){
            $('.navigations').toggle(500,);
            window.scroll(0, 2000);
        } else {
            window.scroll(0, 1200);
        }
    });
});
