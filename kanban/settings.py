"""
This file is for providing default settings, these can and should
be overridden with your Django project's settings.py.
"""
from django.conf import settings

DEFAULT_BOARD_LAYOUTS = {
    'Development': ['Backlog', 'Todo', 'Doing', 'Done', 'Accepted', 'Live'],
    'Project Pipeline': ['Discover', 'Define', 'Design', 'Deliver', 'Deployed', 'Hold', 'Bin'],
}

BOARD_LAYOUTS = settings.get('KANBAN_BOARD_LAYOUTS', DEFAULT_BOARD_LAYOUTS)
