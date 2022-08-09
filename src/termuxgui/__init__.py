"""This is a library for interacting with the Termux:GUI plugin from python.

You don't need to include all the submodules, all needed classes are automatically included in the package scope upon
importing the package. """

__all__ = ['Activity', 'Buffer', 'Button', 'Checkbox', 'CompoundButton', 'Connection', 'EditText', 'Event',
           'FrameLayout', "GridLayout", 'HorizontalScrollView', 'ImageView', 'LinearLayout', 'NestedScrollView',
           'Notification', 'ProgressBar', 'RadioButton', 'RadioGroup', 'RemoteViews', 'Space', 'Spinner',
           'SwipeRefreshLayout', 'Switch', 'TabLayout', 'Task', 'TextView', 'ToggleButton', 'View', 'ViewGroup',
           'WebView']

from termuxgui.activity import Activity
from termuxgui.buffer import Buffer
from termuxgui.button import Button
from termuxgui.checkbox import Checkbox
from termuxgui.compoundbutton import CompoundButton
from termuxgui.connection import Connection
from termuxgui.edittext import EditText
from termuxgui.event import Event
from termuxgui.framelayout import FrameLayout
from termuxgui.gridlayout import GridLayout
from termuxgui.horizontalscrollview import HorizontalScrollView
from termuxgui.imageview import ImageView
from termuxgui.linearlayout import LinearLayout
from termuxgui.nestedscrollview import NestedScrollView
from termuxgui.notification import Notification
from termuxgui.progressbar import ProgressBar
from termuxgui.radiobutton import RadioButton
from termuxgui.radiogroup import RadioGroup
from termuxgui.remoteviews import RemoteViews
from termuxgui.space import Space
from termuxgui.spinner import Spinner
from termuxgui.swiperefreshlayout import SwipeRefreshLayout
from termuxgui.switch import Switch
from termuxgui.tablayout import TabLayout
from termuxgui.task import Task
from termuxgui.textview import TextView
from termuxgui.togglebutton import ToggleButton
from termuxgui.view import View
from termuxgui.viewgroup import ViewGroup
from termuxgui.webview import WebView

