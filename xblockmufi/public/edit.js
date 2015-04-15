function XblockMufiEdit(runtime, element) {
    'use strict';

    var $ = window.$;
    var $element = $(element);
    var buttonSave = $element.find('.save-button');
    var buttonCancel = $element.find('.cancel-button');
    var url = runtime.handlerUrl(element, 'studio_view_save');

    buttonCancel.on('click', function () {
        runtime.notify('cancel', {});
        return false;
    });

    buttonSave.on('click', function () {
        runtime.notify('save', {
            message: 'Saving...',
            state: 'start',
        });
        $.ajax(url, {
            type: 'POST',
            data: JSON.stringify({
                'display_name': $('#mufi_edit_display_name').val(),
                'your_answer_label': $('#mufi_edit_your_answer_label').val(),
                'our_answer_label': $('#mufi_edit_our_answer_label').val(),
                'answer_string': $('#mufi_edit_answer_string').html(),
            }),
            success: function buttonSaveOnSuccess() {
                runtime.notify('save', {
                    state: 'end',
                });
            },
            error: function buttonSaveOnError() {
                runtime.notify('error', {});
            }
        });
        return false;
    });

    // TEXT EDITOR JS
    $('li.specialButton').click(function() {
        $(this).toggleClass('active');
        $('.sr .toggle-open', this).toggle();
        $('.specialCharTable', $element).toggle();
    });

    $('.txtEditor li.styleButton').mousedown(function(){
        var command = $(this).data('command');
        var argument = $(this).data('argument');
        document.execCommand(command, false, argument);
        $('.contents', $element).focus();
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
    });
}
