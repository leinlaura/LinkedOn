$(function () {

    $("#jobseeker").click(function () {
        $("#right").show();
        $('#formFileSm').show();
        $('#formCompany').hide();
    });

    $("#employer").click(function () {
        $("#right").hide();
        $('#formFileSm').hide();
        $('#formCompany').show();
    });
});