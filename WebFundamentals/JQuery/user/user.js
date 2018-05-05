$(document).ready(function(){
    $('form').submit(function(){
        var form = $(this).serializeArray();
        console.log(form);
        $('tbody').append('<tr>')
        for(var i=0;i<form.length;i++){
            var tdata = '<td>' + form[i].value + '</td>';
            $('tbody').append(tdata);
        }
        $('tbody').append('</tr>');
        $('input[type=text]').val('');
        return false;
    });
});