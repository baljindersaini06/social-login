jQuery(document).ready(function() {
    $('form[id="form4"]').validate({
        errorClass: 'my-error-class',
        rules: {
            site_name: 'required',
            site_address: 'required',
            copy_right: 'required',
            site_email: {
            required: true,
            email: true,
        },
        site_favicon: {
            required: true,
            extension: "jpg|jpeg|png|ico|bmp"
        },
        site_logo: {
            required: true,
            extension: "jpg|jpeg|png|ico|bmp"
        }
        },
        messages: {
            site_name: 'This field is required',
            site_favicon: {
                required:'This field is required',
                extension:'Please upload file in these format only (jpg, jpeg, png, ico, bmp).'
            },
            site_logo: {
                required:'This field is required',
                extension:'Please upload file in these format only (jpg, jpeg, png, ico, bmp).'
            },
            site_email: 'Enter a valid email',
            site_address: 'This field is required',
            copy_right: 'This field is required',
            
            
        },
        submitHandler: function(form) {
        form.submit();
        toastr.success('site settings added successfully')

        }
    });
});

