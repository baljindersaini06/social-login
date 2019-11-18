jQuery(document).ready(function() {
    $('form[id="form5"]').validate({
    errorClass: 'my-error-class',
    rules: {
        smtp_password: 'required',
        smtp_email: {
        required: true,
        email: true,
        },
    },
    messages: {
        smtp_password: 'This field is required',
        smtp_email: 'Enter a valid email',
        
    },
    submitHandler: function(form) {
        form.submit();
    }
    });
});