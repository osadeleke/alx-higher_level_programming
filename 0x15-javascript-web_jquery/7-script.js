$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
  $.each(data, function (key, value) {
    if (key === 'name') {
      $('#character').text(value);
    }
  });
});
