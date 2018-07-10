"""
This is the core logic for the XBlock MUFI: XBlock for transcribing manuscripts using MUFI font.
"""
import os

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope
from xblock.fields import String
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioEditableXBlockMixin
from .mixins import EnforceDueDates


class XblockMufi(EnforceDueDates, StudioEditableXBlockMixin, XBlock):
    """
    Icon of the XBlock. Values : [other (default), video, problem]
    """
    icon_class = 'problem'

    @staticmethod
    def workbench_scenarios():
        """
        Gather scenarios to be displayed in the workbench
        """
        return [
            ('XBlock MUFI',
             """
                <sequence_demo>
                    <xblockmufi />
                </sequence_demo>
             """),
        ]

    """
    Fields
    """
    DEFAULT_FIELDS = [
        'parent',
        'tags',
    ]
    
    display_name = String(
        default='XBlock MUFI',
        scope=Scope.settings,
        help="This is the XBlock's name",
    )

    student_answer = String(
        default='',
        scope=Scope.user_state,
        help="This is the student's answer to the question",
    )

    your_answer_label = String(
        default='Your Answer:',
        scope=Scope.settings,
        help="Label for the text area containing the student's answer",
    )

    our_answer_label = String(
        default='Our Answer:',
        scope=Scope.settings,
        help="Label for the 'expert' answer",
    )

    answer_string = String(
        default='',
        scope=Scope.settings,
        help="The 'expert' answer.",
    )

    """
    Main functions
    """
    def student_view(self, context=None):
        """
        Build the fragment for the default student view
        """
        fragment = self.build_fragment(
            path_html='view.html',
            paths_css=[
                'view.less.min.css',
                'library/font-awesome.min.css',
            ],
            paths_js=[
                'view.js.min.js',
            ],
            fragment_js='XblockMufiView',
            context={
                'display_name': self.display_name,
                'student_answer': self.student_answer,
                'is_past_due': self.is_past_due(),
				'submit_class': self._get_submit_class(),
                'your_answer_label': self.your_answer_label,
                'our_answer_label': self.our_answer_label,
                'answer_string': self.answer_string,
            },
        )
        return fragment

    def studio_view(self, context=None):
        """
        Build the fragment for the edit/studio view

        Implementation is optional.
        """
        fragment = self.build_fragment(
            path_html='edit.html',
            paths_css=[
                'edit.less.min.css',
                'library/font-awesome.min.css',
            ],
            paths_js=[
                'edit.js.min.js',
            ],
            fragment_js='XblockMufiEdit',
            context = {
                'display_name': self.display_name,
                'your_answer_label': self.your_answer_label,
                'our_answer_label': self.our_answer_label,
                'answer_string': self.answer_string,
            }
        )
        return fragment

    @XBlock.json_handler
    def studio_view_save(self, data, suffix=''):
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

    def get_resource_string(self, path):
        """
        Retrieve string contents for the file path
        """
        path = os.path.join('public', path)
        resource_string = pkg_resources.resource_string(__name__, path)
        return resource_string.decode('utf8')

    def get_resource_url(self, path):
        """
        Retrieve a public URL for the file path
        """
        path = os.path.join('public', path)
        resource_url = self.runtime.local_resource_url(self, path)
        return resource_url

    def build_fragment(self,
        path_html='',
        paths_css=[],
        paths_js=[],
        urls_css=[],
        urls_js=[],
        fragment_js=None,
        context=None,
    ):
        """
        Assemble the HTML, JS, and CSS for an XBlock fragment
        """
        html_source = self.get_resource_string(path_html)
        html_source = html_source.format(
            self=self,
            **context
        )
        fragment = Fragment(html_source)
        for url in urls_css:
            fragment.add_css_url(url)
        for path in paths_css:
            url = self.get_resource_url(path)
            fragment.add_css_url(url)
        for url in urls_js:
            fragment.add_javascript_url(url)
        for path in paths_js:
            url = self.get_resource_url(path)
            fragment.add_javascript_url(url)
        if fragment_js:
            fragment.initialize_js(fragment_js)
        return fragment

    @XBlock.json_handler
    def student_submit(self, data, suffix=''):
        """
        Save student answer
        """

        if self.is_past_due():
            LOG.error(
                'This problem is past due',
            )
            return {
                'success':False,
                'submit_class':self._get_submit_class(),
            }
        self.student_answer = data['answer']
        return {
            'success':True,
            'submit_class': self._get_submit_class(),
        }

    @XBlock.json_handler
    def publish_event(self, data, suffix=''):
        try:
            event_type = data.pop('event_type')
        except KeyError:
            return {'result': 'error', 'message': 'Missing event_type in JSON data'}

        data['user_id'] = self.scope_ids.user_id
        data['component_id'] = self._get_unique_id()
        self.runtime.publish(self, event_type, data)

        return {'result': 'success'}

    """
    Util functions
    """
    def load_resource(self, resource_path):
        """
        Gets the content of a resource
        """
        resource_content = pkg_resources.resource_string(__name__, resource_path)
        return unicode(resource_content)

    def render_template(self, template_path, context={}):
        """
        Evaluate a template by resource path, applying the provided context
        """
        template_str = self.load_resource(template_path)
        return Template(template_str).render(Context(context))

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode('utf8')

    def _get_unique_id(self):
        try:
            unique_id = self.location.name
        except AttributeError:
            # workaround for xblock workbench
            unique_id = 'workbench-workaround-id'
        return unique_id

    def _get_submit_class(self):
        """
        Returns the css class for the submit button
        """
        result = ''
        if self.is_past_due():
            result = 'nodisplay'
        return result
