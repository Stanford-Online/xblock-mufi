function XblockMufiView(runtime, element) {
    'use strict';

    var $ = window.jQuery;
    var $element = $(element);

    $('li.specialButton').click(function() {
        $(this).toggleClass('active');
        $('.sr .toggle-open', this).toggle();
        $('.specialCharTable').toggle();
    });

    $('.txtEditor li.styleButton').mousedown(function(){
        var command = $(this).data('command');
        var argument = $(this).data('argument');
        document.execCommand(command, false, argument);
        $('.contents').focus();
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
