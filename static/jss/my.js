    jQuery(document).ready(function() {  
        $("form[name='avtar']").validate({
        errorClass: "my-error-class",
        // Specify validation rules
        rules: {
        // The key name on the left side is the name attribute
        // of an input field. Validation rules are defined
        // on the right side
        profile_image: {
            required : true
        },
            
        },
        // Specify validation error messages
        messages: {
            profile_image: "This field is required",
        
        },
        // Make sure the form is submitted to the destination defined
        // in the "action" attribute of the form when valid
        submitHandler: function(form) {
        form.submit();
        toastr.success('Image Updated Successfully', {timeOut: 500})
        }
    })
});
