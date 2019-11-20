jQuery(document).ready(function() { 
$("form[name='password']").validate({
    errorClass: "my-error-class",
    // Specify validation rules
    rules: {
    // The key name on the left side is the name attribute
    // of an input field. Validation rules are defined
    // on the right side
    old_password: {
        required : true,
        remote : {url: "/test", async:false}
    },
    new_password1:{
        required : true
    },
    new_password2: {
        required : true,
        equalTo: "#new_password1"
    },

    },
    // Specify validation error messages
    messages: {
    old_password: {
        required : "Please enter your Current password",
        remote : "Please enter your corret password",
    },
    new_password1: "Please enter your New Password",
    new_password2: {
        required : "Please Confirm your Password",
        equalTo : "Enter Confirm password same as Password",
    }
    },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    submitHandler: function(form) {
    form.submit();
    toastr.success('Password Changed Successfully')
    }
})
});
