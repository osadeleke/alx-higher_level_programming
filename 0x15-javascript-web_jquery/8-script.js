$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  $.each(data, function (key, value) {
    if (key === 'results') {
      $.each(value, function (index, movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    }
  });
});
