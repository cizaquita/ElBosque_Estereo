$( document ).ready(function() {
    $('#ico_play').hide();
    $('#ico_pause').show();
    $('#play-control').trigger('play')

    $('#ico_pause').click(function() {
            $('#ico_play').show();
            $('#ico_pause').hide();
            $('#play-control').trigger("pause");
    });

    
    $('#ico_play').click(function() {      
        $('#ico_play').hide();
        $('#ico_pause').show();
        $('#play-control').trigger('play')
    });
});

