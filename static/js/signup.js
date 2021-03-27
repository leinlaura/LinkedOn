$(function () {

    $("#jobseeker").click(function () {
        $("#right").show();
        $('#formCompany').hide();
    });

    $("#employer").click(function () {
        $("#right").hide();
        $('#formFileSm').hide();
        $('#formCompany').show();
    });
});