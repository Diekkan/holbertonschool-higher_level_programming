$(function() {

    $.ajax({
        type: 'GET',
        url: 'https://swapi-api.hbtn.io/api/films/?format=json',
        success: function(movies){
            $('#list_movies').append('<ul>');
            for(var i = 0; movies.results[i]; i++) {
                $('#list_movies').after('<li>' + movies.results[i].title  + '</li>');
            }
            $('#list_movies').append('</ul>');
        }
    })
});