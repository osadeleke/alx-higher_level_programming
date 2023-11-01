$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  $.each(data, function (key, value) {
    if (key === 'hello') {
      $('#hello').text(value);
    }
  });
});
