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
