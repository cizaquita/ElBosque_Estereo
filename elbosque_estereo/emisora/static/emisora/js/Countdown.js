$(document).ready(function() {
    var clock;   

    var fechaFinal = new Date(2018,5,2,8,0,0);    
	var fechaHoy = new Date();
    
    var diferenciaMilisegundos = fechaFinal.getTime()/1000 - fechaHoy.getTime()/1000;    
  
    clock = $('.clock').FlipClock(diferenciaMilisegundos,{
        clockFace: 'DailyCounter',
        autoStart: false,
        callbacks: {
            stop: function() {
              alert('The clock has stopped!');
            }
        }        
    });
    clock.setCountdown(true);
    clock.start();
});