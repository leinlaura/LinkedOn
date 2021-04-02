$(function() {
    $.validator.addMethod("validUrl", function (value, element) {
        return /[-a-zA-Z0-9@:%_\+.~#?&//=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?/gi.test(value);
    });

    $("#user_form").validate({
        rules: {
            first_name: {
                maxlength: 150,
            },
            last_name: {
                maxlength: 150,
            },
            company: {
                maxlength: COMPANY_MAX_LENGTH,
            },
            password: {
                maxlength: 30,
            },
            website: {
                maxlength: WEBSITE_MAX_LENGTH,
                validUrl: true,
            },
            about: {
                maxlength: ABOUT_MAX_LENGTH,
            },
            searchingInfo: {
                maxlength: SEARCHING_MAX_LENGTH,
            },
        },
        messages: {
            website: {
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