$(function () {
    $('#formCompany').hide();

    $("#jobseeker").click(function () {
        $("#right").show();
        $('#formFileSm').show();
        $('#formCompany').hide();
        $('#submit').appendTo('#right');
    });

    $("#employer").click(function () {
        $("#right").hide();
        $('#formFileSm').hide();
        $('#formCompany').show();
        $('#submit').appendTo('#middle');
    });

    $.validator.addMethod("validUrl", function (value, element) {
        return /[-a-zA-Z0-9@:%_\+.~#?&//=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?/gi.test(value);
    });

    $("#user_form").validate({
        rules: {
            first_name: {
                required: true,
                maxlength: 150,
            },
            last_name: {
                required: true,
                maxlength: 150,
            },
            company: {
                required: {
                    depends: function (element) {
                        return $("#employer").is(":checked");
                    },
                },
                maxlength: COMPANY_MAX_LENGTH,
            },
            username: {
                required: true,
                email: true,
                maxlength: 150,
            },
            password: {
                required: true,
                maxlength: 30,
            },
            website: {
                required: true,
                maxlength: WEBSITE_MAX_LENGTH,
                validUrl: true,
            },
            profileImage: {
                required: false,
            },
            about: {
                required: {
                    depends: function (element) {
                        return $("#jobseeker").is(":checked");
                    },
                },
                maxlength: ABOUT_MAX_LENGTH,
            },
            searchingInfo: {
                required: {
                    depends: function (element) {
                        return $("#jobseeker").is(":checked");
                    },
                },
                maxlength: SEARCHING_MAX_LENGTH,
            },
            category: {
                required: {
                    depends: function (element) {
                        return $("#jobseeker").is(":checked");
                    },
                },
            },
        },
        messages: {
            website: {
                required: "This field is required.",
                validUrl: "Please enter a valid URL.",
            }
        },
        errorPlacement: function (error, element) {
            error.insertBefore(element);
        },
    });
});

