$(function() {
    var formHijacker = function() {
        $('#short_form').on('submit', handleShortFormSubmit);
    };

    // getCookie function obtained from https://docs.djangoproject.com/en/1.10/ref/csrf/
    var getCookie = function(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    var handleShortFormSubmit = function(event) {
        event.preventDefault();
        var $theForm = $(event.target); 

        var submissionData = new Object();
        submissionData.long_url = $theForm.find('#long_url')[0].value;
        submissionData.short_url = $theForm.find('#short_url')[0].value;
        submissionData.csrfmiddlewaretoken = csrftoken;

        var submissionString = JSON.stringify(submissionData);

        $.ajax({
            method: "POST",
            url: "/short/api/create/",
            data: submissionData,
            success: function(response) {
                successfulShorten(response);
            },
            error: function(response) {
                errorShorten(response);
            }
        })

        return false;

        
    };

    var successfulShorten = function(event) {
        $('#short_url').css('border', '');
        $('#long_url').css('border', '');
        if(event['success'] == 2) {
            $('#title-extension').css('opacity', 0);
            $('#title-extension').text("/"+event['short_url']);
            $('#title-extension').css('opacity', 1);
        } else if(event['success'] == 1) {
            $('#short_url').css('border', '');
            $('#title-extension').css('opacity', 0);
            $('#title-extension').text("/"+event['short_url']);
            $('#title-extension').css('opacity', 1);
        } else if(event['success'] == 0) {
            $('#title-extension').text('');
            $('#short_url').css('border', 'solid red 3px');
        } else if(event['success'] == -1) {
            $('#long_url').css('border', 'solid red 3px');
        }
    };
    formHijacker();

})