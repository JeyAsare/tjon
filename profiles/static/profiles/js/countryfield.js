let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', 'rgb(196, 162, 133)');
};
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', 'rgb(196, 162, 133)');
    } else {
        $(this).css('color', '#000');
    }
});