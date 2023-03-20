$(document).ready(function() {

    var bookId = window.location.href.split("?")[1]
    $("#name").val(bookId);

})