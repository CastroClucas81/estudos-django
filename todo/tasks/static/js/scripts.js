$(document).ready(function () {
  var searchBtn = $("#search-btn");
  var searchForm = $("#search-form");

  $(searchBtn).on('click', function () {
    searchForm.submit();
  });

  var baseUrl = 'http://localhost:8000/';
  var filter = $('#filter');

  $(filter).change(function () {

    var filter = $(this).val();
    window.location.href = baseUrl + '?filter=' + filter;
  });
});
