/* eslint-disable no-unused-vars */
/**
 * Initialize the view
 * @param {Object} runtime - The XBlock JS Runtime
 * @param {Object} element - The containing DOM element for this instance of the XBlock
 * @returns {undefined} nothing
 */
function XblockMufiView(runtime, element) {
    /* eslint-enable no-unused-vars */
    'use strict';

    var $ = window.jQuery;
    var $element = $(element);
    var buttonSubmit = $element.find('.submit_button');
    var buttonCancel = $element.find('.reset_button');
    var handlerUrl = runtime.handlerUrl(element, 'student_submit');
    var yourAnswer = $element.find('.your_answer');
    var expertAnswer = $element.find('.expert_answer');
    var $contents = $element.find('.contents');

    /**
     * Display user answer
     * @returns {undefined} nothing
     */
    function showAnswer() {
        yourAnswer.css('display', 'block');
        expertAnswer.css('display', 'block');
        buttonSubmit.val('Resubmit');
    }

    /**
     * Reset answer state
     * @returns {undefined} nothing
     */
    function resetAnswer() {
        yourAnswer.css('display', 'none');
        expertAnswer.css('display', 'none');
        buttonSubmit.val('Submit');
    }

    buttonCancel.on('click', function () {
        $contents.html('');
        $.ajax({
            type: 'POST',
            url: handlerUrl,
            data: JSON.stringify({
                answer: '',
            }),
        });
        resetAnswer();
    });

    buttonSubmit.on('click', function () {
        $.ajax({
            type: 'POST',
            url: handlerUrl,
            data: JSON.stringify({
                answer: $contents.html(),
            }),
        });
        showAnswer();
    });

    if ($contents.html() !== '') {
        showAnswer();
    }

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

    $contents.focus();
}
