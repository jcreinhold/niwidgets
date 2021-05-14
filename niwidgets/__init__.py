"""Top-level package for niwidgets."""

__author__ = """Niwidgets developers, Jacob Reinhold (this verison)"""
__email__ = 'jcreinhold@gmail.com'
__version__ = '0.2.3'

from niwidgets.example_data import example_atlas, example_zmap, example_t1  # noqa: F401
from niwidgets.niwidget_volume import NiftiWidget  # noqa: F401
from niwidgets.niwidget_surface import SurfaceWidget  # noqa: F401
from niwidgets.streamlines import StreamlineWidget  # noqa: F401
