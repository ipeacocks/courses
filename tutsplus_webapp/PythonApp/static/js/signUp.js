$(function() {
    $('#btnSignUp').click(function() {

        $.ajax({
            url: '/signUp',
            data: $('form').serialize(),
            type: 'POST',
            // console.log( $( data ) );
            success: function(response) {
                // console.log(response);
                console.log($('form').serialize());
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});