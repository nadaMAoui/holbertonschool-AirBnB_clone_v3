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
