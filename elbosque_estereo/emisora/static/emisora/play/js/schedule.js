var settings = {
  "async": true,
  "crossDomain": true,
  "url": "/get_parrilla/",
  "method": "GET",
  "dataType": "json",
  "headers": {
    "Cache-Control": "no-cache",
    "Postman-Token": "5fa62535-8f43-459e-b012-07d5a0a7c9de"
  }
}

$.ajax(settings).done(function (response) {
  crearTarjetas(response);

  var actionButton = $(".material-card-action a");

  actionButton.on("click", function (e) {
    e.preventDefault();

    $(this).closest(".material-card").toggleClass("triggered");
    $(this).closest(".material-card-action").toggleClass("triggered");

  });
});


function crearTarjetas(data) {
  for (var i in data) {
    var cardImg = data[i].imagen_banner;
    var cardType = data[i].tipo_programa;
    var cardName = data[i].nombre;
    var cardURL = data[i].url_pregrabado;
    if (cardURL != null) cardURL = cardURL.replace('\\', '');
    var cardDescription = (data[i].descripcion == null) ? 'No disponible' : data[i].descripcion;
    var cardCategory = data[i].categoria;
    var cardSubCategory = data[i].subcategoria;
    var dateStart = (data[i].fecha_inicio == null) ? 'No disponible' : data[i].fecha_inicio;
    var dateEnd = data[i].fecha_final;
    var card = '<article class="material-card">' +
      '<header>' +
      '<figure class="material-card-icon ironman">';
    if (cardImg != null) {
      card = card + '<img src="http://media.elbosquestereo.com/' + cardImg + '" width="140px">';
    }
    card = card + '</figure>' +
      '<h2 class="material-card-title">' + cardName + '</h2>' +
      '<div class="material-card-action">' +
      '<a href="#">' +
      '<i class="material-icons md-36">keyboard_arrow_right</i>' +
      '</a>' +
      '</div>' +
      '<div class="material-card-info">' +
      '<i class="material-icons">access_time</i>' +
      '<time>' + dateStart + '</time>' +
      '</div>' +
      '</header>' +
      '<div class="material-card-content">' +
      '<p>' + cardDescription + '</p>';
    if (cardURL != null) {
      card = card + cardURL;
    }
    console.log('iframe: ' + card);
    card = card +
      '</div>' +
      '</article>';
    $('#contentCards').append(card);
    console.log(cardImg);
  }
}