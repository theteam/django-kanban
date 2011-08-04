"""
This file is for providing default settings, these can and should
be overridden with your Django project's settings.py.
"""
from django.conf import settings

DEFAULT_BOARD_LAYOUTS = {
    'Development': ['Backlog', 'Todo', 'Doing', 'Done', 'Accepted', 'Live'],
    'Project Pipeline': ['Discover', 'Define', 'Design', 'Deliver', 
                         'Deployed', 'Hold', 'Bin'],
}

# These are the various 'skins' available via the 
# projects CSS. In Django ChoiceField choices style.
# [0] is the classname to be used in templates. [1] is
# the "friendly" display name for that style.
DEFAULT_BOARD_STYLES = (
    ('default', 'Default'),
)

BOARD_LAYOUTS = getattr(settings, 'KANBAN_BOARD_LAYOUTS', 
                        DEFAULT_BOARD_LAYOUTS)

BOARD_STYLES = getattr(settings, 'KANBAN_BOARD_STYLES', 
                       DEFAULT_BOARD_STYLES)
