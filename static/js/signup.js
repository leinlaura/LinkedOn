$(function () {
    $('#formCompany').hide();

    $("#jobseeker").click(function () {
        $("#right").show();
        $('#formFileSm').show();
        $('#formCompany').hide();
        $('#submit').appendTo('#right')
    });

    $("#employer").click(function () {
        $("#right").hide();
        $('#formFileSm').hide();
        $('#formCompany').show();
        $('#submit').appendTo('#middle')
    });
});