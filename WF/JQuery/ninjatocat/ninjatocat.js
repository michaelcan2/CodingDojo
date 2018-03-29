$(document).ready(function(){
    $('.cat').hide();
    $('.holder').click(function(){
        $('img', this).toggle();
    });
})