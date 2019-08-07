"""
Handle view logic for the XBlock
"""
from __future__ import absolute_import
from xblock.core import XBlock
from xblockutils.resources import ResourceLoader
from xblockutils.studio_editable import StudioEditableXBlockMixin

from .mixins.fragment import XBlockFragmentBuilderMixin


class MufiViewMixin(
        XBlockFragmentBuilderMixin,
        StudioEditableXBlockMixin,
):
    """
    Handle view logic for XBlock instances
    """

    loader = ResourceLoader(__name__)
    static_css = [
        'view.css',
        'library/font-awesome.min.css',
    ]
    static_js_init = 'XblockMufiView'
    # Icon of the XBlock. Values :
    #   [other (default), video, problem]
    icon_class = 'problem'

    def provide_context(self, context=None):
        """
        Build a context dictionary to render the student view
        """
        context = context or {}
        context = dict(context)
        context.update(
            {
                'display_name': self.display_name,
                'student_answer': self.student_answer,
                'is_past_due': self.is_past_due(),
                'your_answer_label': self.your_answer_label,
                'our_answer_label': self.our_answer_label,
                'answer_string': self.answer_string,
            }
        )
        return context

    # pylint: disable=unused-argument
    @XBlock.json_handler
    def publish_event(self, data, **kwargs):
        """
        Publish an event from the front-end
        """
        try:
            event_type = data.pop('event_type')
        except KeyError:
            return {
                'result': 'error',
                'message': 'Missing event_type in JSON data',
            }
        data['user_id'] = self.scope_ids.user_id
        data['component_id'] = self._get_unique_id()
        self.runtime.publish(self, event_type, data)
        return {'result': 'success'}
    # pylint: enable=unused-argument

    # pylint: disable=unused-argument
    @XBlock.json_handler
    def student_submit(self, data, **kwargs):
        """
        Save student answer
        """
        if self.is_past_due():
            success_value = False
        else:
            success_value = True
            self.student_answer = data['answer']
        return {
            'success': success_value,
        }
    # pylint: enable=unused-argument

    def _get_unique_id(self):
        """
        Lookup the component identifier
        """
        try:
            unique_id = self.location.name
        except AttributeError:
            # workaround for xblock workbench
            unique_id = 'workbench-workaround-id'
        return unique_id

    def studio_view(self, context=None):
        """
        Build the fragment for the edit/studio view

        Implementation is optional.
        """
        context = context or {}
        context.update({
            'display_name': self.display_name,
            'your_answer_label': self.your_answer_label,
            'our_answer_label': self.our_answer_label,
            'answer_string': self.answer_string,
        })
        template = 'edit.html'
        fragment = self.build_fragment(
            template=template,
            context=context,
            js_init='XblockMufiEdit',
            css=[
                'edit.css',
                'library/font-awesome.min.css',
            ],
            js=[
                'edit.js',
            ],
        )
        return fragment

    # pylint: disable=unused-argument
    @XBlock.json_handler
    def studio_view_save(self, data, *args, **kwargs):
        """
        Save XBlock fields

        Returns: the new field values
        """
        self.display_name = data['display_name']
        self.your_answer_label = data['your_answer_label']
        self.our_answer_label = data['our_answer_label']
        self.answer_string = data['answer_string']
        return {
            'display_name': self.display_name,
            'your_answer_label': self.your_answer_label,
            'our_answer_label': self.our_answer_label,
            'answer_string': self.answer_string,
        }
    # pylint: enable=unused-argument
