$(document).ready(function(){
    $("#show h3").hide();
// dont close this b/c it needs to hide show, in order to press show to continue. 
$("#slidedown p").hide();

$("#hide").click(function(){
    $("#hide p").hide("slow"); 
});
$("#show").click(function(){
    $("#h3").show("fast");
});
$("#fadeOut").click(function(){
    $("#test").fadeOut("slow");
});
$('#before button').click(function(){
    $('#before button').before('<h3>This was added before the button with jQuery!</h3>');
});
$("#toggle").click(function(){
    $("#toggle p").toggle();
});
$("#slidedown button").click(function(){
    $("#slidedown p").slidedown("slow");
});
$('#after button').click(function(){
    $('#after button').after('<h3>This was added after the button with jQuery!</h3>');
});
$('#html button').click(function(){
    $('#html h3').html('This is the new HTMl that I was just talking about that was brought over thanks to javascript and jQuery.');
});
$('#addClass button').click(function(){
    $('#addClass h3').addClass('blue');
});
$('#data button').click(function(){
    $('#data p span').html($( "#data" ).data( "data" ).value);
});
});

