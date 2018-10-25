window.TestDrivenDev = {};
window.TestDrivenDev.initialize = function() {
    $('input[name="text"]').on('keypress', function() {
        $('.has-error').hide();
    });
    $('#id_text').on('click', function() {
        $('.has-error').hide();
    });
};

