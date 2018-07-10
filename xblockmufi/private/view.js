function XblockMufiView(runtime, element) {
    'use strict';

    var $ = window.jQuery;
    var $element = $(element);

    var handlerUrl = runtime.handlerUrl(element, 'student_submit');
    var publishUrl = runtime.handlerUrl(element, 'publish_event');

    var submit_button = $element.find('.submit_button');
    var reset_button = $element.find('.reset_button');

    var your_answer = $element.find('.your_answer');
    var expert_answer = $element.find('.expert_answer');

    function publish_event(data) {
      $.ajax({
          type: 'POST',
          url: publishUrl,
          data: JSON.stringify(data)
      });
    }

    function post_submit(result) {
        button_holder.addClass(result.submit_class);        
    }

    function show_answer() {
        your_answer.css('display','block');
        expert_answer.css('display','block');
        submit_button.val('Resubmit');

    }

    function reset_answer() {
        your_answer.css('display','none');
        expert_answer.css('display','none');
        submit_button.val('Submit and Compare');
    }

    $('.submit_button', element).click(function(eventObject) {
        $.ajax({
            type: 'POST',
            url: handlerUrl,
            data: JSON.stringify({'answer': $('.contents', element).html() }),
            success: post_submit
        });
        show_answer();
    });

    $('.reset_button', element).click(function(eventObject) {
        $('.contents', element).html('');
        $.ajax({
            type: 'POST',
            url: handlerUrl,
            data: JSON.stringify({'answer': '' }),
            success: post_submit
        });
        reset_answer();
    });

    if ($('.contents', element).html() !== '') {
        show_answer();
    }

    // TEXT EDITOR JS
    $('li.specialButton').click(function(e) {
        e.preventDefault();
        $(this).toggleClass('active');
        $('.sr .toggle-open', this).toggle();
        $('.specialCharTable', $element).toggle();
    });

    $('.txtEditor li.styleButton').click(function(e){
        e.preventDefault();
        var command = $(this).data('command');
        var argument = $(this).data('argument');
        document.execCommand(command, false, argument);
    });

    $('.specialCharTable .charWrapper .char').hover(function() {
        var selChar = $(this).html();
        var selCharTitle = $(this).attr('title');
        if (!selCharTitle) {
            selCharTitle = "";
        }
        $('.charZoom').html(selChar);
        $('.charZoomTitle').text(selCharTitle);
    });

    $('.specialCharTable .charWrapper .char').mousedown(function() {
        var textToInsert = $(this).html();
        document.execCommand('insertHTML', false, textToInsert);
        return false;
    });
}
