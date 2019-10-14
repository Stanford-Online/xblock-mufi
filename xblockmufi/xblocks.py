"""
This is the core logic for the XBlock
"""
from __future__ import absolute_import
from xblock.core import XBlock

from .mixins.dates import EnforceDueDates
from .mixins.scenario import XBlockWorkbenchMixin
from .models import MufiModelMixin
from .views import MufiViewMixin


@XBlock.needs('i18n')
class Mufi(
        EnforceDueDates,
        MufiModelMixin,
        MufiViewMixin,
        XBlockWorkbenchMixin,
        XBlock,
):
    """
    A manuscript transcription XBlock
    """
