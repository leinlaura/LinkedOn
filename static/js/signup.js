$(function () {
    $('#formCompany').hide();

    // Hide and show form fields that a job-seeker should see
    $("#jobseeker").click(function () {
        $("#right").show();
        $('#formFileSm').show();
        $('#formCompany').hide();
        $('#submit').appendTo('#right');
    });

    // Hide and show form fields that a employer should see
    $("#employer").click(function () {
        $("#right").hide();
        $('#formFileSm').hide();
        $('#formCompany').show();
        $('#submit').appendTo('#middle');
    });

    // Add a validation method that checks if a given url is correct
    $.validator.addMethod("validUrl", function (value, element) {
        return /[-a-zA-Z0-9@:%_\+.~#?&//=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?/gi.test(value);
    });

    // Setup client-side form validation of the user-form
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
                remote: {
                    url: USERNAME_CHECK_URL,
                    type: 'GET',
                    dataFilter: function (response) {
                        return JSON.parse(response).unique;
                    },
                },
            },
            password: {
                required: true,
                maxlength: 30,
            },
            website: {
                required: false,
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
            },
            username: {
                remote: "This username is already taken.",
            },
        },
        errorPlacement: function (error, element) {
            error.insertBefore(element);
        },
    });
});

