$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: function (result) {
    result.results.map(function (item) {
      $('UL#list_movies').append('<li>' + item.title + '</li>');
    });
  }
});
