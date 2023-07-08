$(document).ready(function(){
    var CheckAmenity = [];

    $('#Input[type="checkbox"]'.change('click', function(){
        var AmenityId = $(this).data('id');
    

    }))
    if ($(this).is (':checked')){
        CheckAmenity.push(AmenityId);
    }
    else{
        var index = CheckAmenity.indexOf(AmenityId);
        if(index !== -1){
            CheckAmenity.splice(index, 1);
        }
    }
    

    $('#Amenities h4').text('Amenities: ' + CheckAmenity.join(', '));


});

$.getJSON('http://0.0.0.0:5001/api/v1/status/', function(data) {
    
    const status = data.status;

    
    const div = $('#api_status');

    
    if (status === "OK") {
      div.addClass('available');
    } else {
      div.removeClass('available');
    }
})
$.ajax({
    url: 'http://localhost:5001/api/v1/places_search/',
    type: 'POST',
    data: '{}',
    contentType: 'application/json',
    dataType: 'json',
    success: appendPlaces
  });


function appendPlaces (data) {
$('SECTION.places').empty();
$('SECTION.places').append(data.map(place => {
  return `<ARTICLE>
            <DIV class="title">
              <H2>${place.name}</H2>
                <DIV class="price_by_night">
                  ${place.price_by_night}
                </DIV>
              </DIV>
              <DIV class="information">
                <DIV class="max_guest">
                  ${place.max_guest} Guests
                </DIV>
                <DIV class="number_rooms">
                  ${place.number_rooms} Bedrooms
                </DIV>
                <DIV class="number_bathrooms">
                  ${place.number_bathrooms} Bathrooms
                </DIV>
              </DIV>
              <DIV class="description">
                ${place.description}
              </DIV>
            </ARTICLE>`;
}));
}
