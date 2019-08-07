"""
Handle data access logic for the XBlock
"""
from __future__ import absolute_import
from django.utils.translation import ugettext_lazy as _
from xblock.fields import Scope
from xblock.fields import String


class MufiModelMixin(object):
    """
    Handle data access for the XBlock
    """

    editable_fields = [
        'display_name',
        'image_url',
        'thumbnail_url',
        'description',
        'alt_text',
    ]
    show_in_read_only_mode = True
    answer_string = String(
        default='',
        scope=Scope.settings,
        help=_("The 'expert' answer."),
    )
    display_name = String(
        default='XBlock MUFI',
        display_name=_('Display Name'),
        scope=Scope.settings,
        help=_("This is the XBlock's name"),
    )
    our_answer_label = String(
        default='Our Answer:',
        scope=Scope.settings,
        help=_("Label for the 'expert' answer"),
    )
    student_answer = String(
        default='',
        scope=Scope.user_state,
        help=_("This is the student's answer to the question"),
    )
    your_answer_label = String(
        default='Your Answer:',
        scope=Scope.settings,
        help=_("Label for the text area containing the student's answer"),
    )
