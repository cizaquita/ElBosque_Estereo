
$(document).ready(function() {
    $("#start").click(function() {
        $('#header').hide();
        $('.program').hide();
        $('.onAir').show();
       $("#play-button").click();      
    });

    $("#program").click(function() {
        $('#header').hide();
        $('.onAir').hide();
        $('.program').show();
    });

    $("#logo").click(function() {
        $('#header').hide();
        $('.program').hide();
        $('.onAir').show();
    });

});
