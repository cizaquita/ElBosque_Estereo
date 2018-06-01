$(document).ready(function() {
    var clock;   

    var fechaFinal = new Date(2018,5,2,9,0,0);    
	var fechaHoy = new Date();
    
    var diferenciaMilisegundos = fechaFinal.getTime()/1000 - fechaHoy.getTime()/1000;    
  
    if(diferenciaMilisegundos<= 0){
        window.location.href = ("http://localhost:8000/ind");
    }
    
    clock = $('.clock').FlipClock(diferenciaMilisegundos,{
        clockFace: 'DailyCounter',
        autoStart: false,
        callbacks: {
            stop: function() {
              window.location.href = ("http://localhost:8000/ind");
            }
        }        
    });
    clock.setCountdown(true);
    clock.start();
});