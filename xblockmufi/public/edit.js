/* eslint-disable no-unused-vars */
/**
 * Initialize the view
 * @param {Object} runtime - The XBlock JS Runtime
 * @param {Object} element - The containing DOM element for this instance of the XBlock
 * @returns {undefined} nothing
 */
function XblockMufiEdit(runtime, element) {
    /* eslint-enable no-unused-vars */
    'use strict';

    var $ = window.jQuery;
    var $element = $(element);
    var buttonSubmit = $element.find('.submit_button');
    var buttonCancel = $element.find('.reset_button');
    var handlerUrl = runtime.handlerUrl(element, 'studio_view_save');

    buttonCancel.on('click', function () {
        runtime.notify('cancel', {});
        return false;
    });

    buttonSubmit.on('click', function () {
        runtime.notify('save', {
            message: 'Saving...',
            state: 'start',
        });
        /* eslint-disable camelcase */
        $.ajax(handlerUrl, {
            type: 'POST',
            data: JSON.stringify({
                display_name: $('#mufi_edit_display_name').val(),
                your_answer_label: $('#mufi_edit_your_answer_label').val(),
                our_answer_label: $('#mufi_edit_our_answer_label').val(),
                answer_string: $('#mufi_edit_answer_string').html(),
            }),
            success: function buttonSaveOnSuccess() {
                runtime.notify('save', {
                    state: 'end',
                });
            },
            error: function buttonSaveOnError() {
                runtime.notify('error', {});
            },
        });
        /* eslint-enable camelcase */
        return false;
    });

    /* eslint-disable no-invalid-this*/
    $('li.specialButton').mousedown(function () {
        $(this).toggleClass('active');
        $('.sr .toggle-open', this).toggle();
        $('.specialCharTable', $element).toggle();
        return false;
    });

    $('.txtEditor li.styleButton').mousedown(function () {
        var command = $(this).data('command');
        var argument = $(this).data('argument');
        document.execCommand(command, false, argument);
        return false;
    });

    $('.specialCharTable .charWrapper .char').hover(function () {
        var selectedChar = $(this).html();
        var selectedCharTitle = $(this).attr('title') || '';
        $('.charZoom').html(selectedChar);
        $('.charZoomTitle').text(selectedCharTitle);
    });

    $('.specialCharTable .charWrapper .char').mousedown(function () {
        var textToInsert = $(this).html();
        document.execCommand('insertHTML', false, textToInsert);
        return false;
    });
    /* eslint-enable no-invalid-this*/
}
