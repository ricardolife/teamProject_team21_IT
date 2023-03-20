$(document).ready(function() {

    $("#19").click(function() {
        var year = "1984";
        $("#submitValue").val(year);
        $("#targetForm").submit();
    });

    $("#Gatsby").click(function() {
        var gatsby = "The Great Gatsby";
        $("#submitValue").val(gatsby);
        $("#targetForm").submit();
    });

    $("#Kill").click(function() {
        var kill = "To Kill a Mockingbird"
        $("#submitValue").val(kill);
        $("#targetForm").submit();
    });

    $("#Hitch").click(function() {
        var hitch = "The Hitchhicker's Guide to the Galaxy";
        $("#submitValue").val(hitch);
        $("#targetForm").submit();
    });

    $("#Catcher").click(function() {
        var catcher = "The Catcher in the Rye";
        $("#submitValue").val(catcher);
        $("#targetForm").submit();
    });

    $("#Lord").click(function() {
        var lord = "The Lord of the Rings";
        $("#submitValue").val(lord);
        $("#targetForm").submit();
    });
})