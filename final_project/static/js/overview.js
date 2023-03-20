$(document).ready(function() {

    $("#addReview").click(function() {
        var name = $("#bookId").text()
//        var bookName =
        window.location.href = "../redirectRating" + "?" + name;
    });


    $("#addReview1").click(function() {
        var name = $("#bookId").text()
        window.location.href = "../login" + "?" + name;
    });
});