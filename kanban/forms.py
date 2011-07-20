from django import forms

from kanban.models import Board, Category
from kanban.settings import BOARD_LAYOUTS


LAYOUT_CHOICES = [(x, x) for x in BOARD_LAYOUTS.iterkeys()]


class BoardCreateForm(forms.ModelForm):
    starting_layout = forms.ChoiceField(choices=LAYOUT_CHOICES)

    class Meta:
        model = Board
        fields = ['title', 'tagline']

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(BoardCreateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True, *args, **kwargs):
        board = super(BoardCreateForm, self).save(commit=False, *args, **kwargs)
        board.creator = self.user
        if commit:
            board.save()
            # Save, and then work out which default set of 
            # 'state columns' to start the user with. These
            # are retrived from the setings and are basically
            # kanban board 'templates'.
            layout_choice = self.cleaned_data['starting_layout']
            state_list = BOARD_LAYOUTS[layout_choice]
            for i, state in enumerate(state_list):
                board.states.create(title=state, order=i)
        return board


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['title', 'tagline']
