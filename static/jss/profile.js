jQuery(document).ready(function() {  
    $("form[name='profile']").validate({
    errorClass: "my-error-class", //for error colors
    // Specify validation rules
    rules: {
    // The key name on the left side is the name attribute
    // of an input field. Validation rules are defined
    // on the right side
    first_name: {
        required : true
    },
    last_name: {
        required : true
    },
    username: {
        required : true
    },
    email: {
        required : true,
        email: true
    },
        
    },
    // Specify validation error messages
    messages: {
        first_name: "This field is required",
        last_name: "This field is required",
        username: "This field is required",
        email: "Enter correct email",
    },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    submitHandler: function(form) {
    form.submit();
    toastr.success('Profile Updated Successfully')
    }
})
});
