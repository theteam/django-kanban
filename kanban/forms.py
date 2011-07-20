from django import forms

from kanban.models import Board, Category
from kanban.settings import BOARD_LAYOUTS


LAYOUT_CHOICES = [(x, x) for x in BOARD_LAYOUTS.iterkeys()]


class BoardForm(forms.ModelForm):
    starting_layout = forms.ChoiceField(choices=LAYOUT_CHOICES)


    class Meta:
        model = Board
        fields = ['title', 'tagline']


    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(BoardForm, self).__init__(*args, **kwargs)


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['title', 'tagline']
