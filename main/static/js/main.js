var noneCheckbox = document.getElementById('no-injury');
var checkboxes = document.getElementsByName('injuries');

for (var i = 0; i < checkboxes.length; i++) {
    checkboxes[i].onchange = function (e) {
        if (this !== noneCheckbox) {
            var checkboxInput = document.getElementById(this.getAttribute('id')+'-games');
            if (checkboxInput.style.visibility !== 'visible') {
                checkboxInput.style.visibility = 'visible';
            }
            else {
                checkboxInput.style.visibility = 'hidden';
            }
        }
    };
}


noneCheckbox.onchange = function (e) {
    if (noneCheckbox.checked)
    {
        for (var i = 0; i < checkboxes.length; i++)
        {
            if (checkboxes[i] !== this)
            {
                checkboxes[i].checked = false;
                checkboxes[i].disabled = true;
            }
        }
    }
    else
    {
        for (var i = 0; i < checkboxes.length; i++)
        {
            if (checkboxes[i] !== this)
            {
                checkboxes[i].disabled = false;
            }
        }
    }
};

(function ($) {
    "use strict";

  
    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit',function(){
        var check = true;

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
        }

        return check;
    });


    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function validate (input) {
        if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(input).val().trim() == ''){
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
    

})(jQuery);