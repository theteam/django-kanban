from django.views.generic import CreateView, DetailView, ListView

from kanban.forms import BoardCreateForm, CategoryForm
from kanban.models import Category, Board


class CategoryCreateView(CreateView):

    form_class = CategoryForm
    template_name = 'kanban/category_create.html'


class CategoryListView(ListView):
    
    model = Category


class BoardCreateView(CreateView):

    form_class = BoardCreateForm
    template_name = 'kanban/board_create.html'

    def get_form_kwargs(self):
        kwargs = super(BoardCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class BoardListView(ListView):

    model = Board


class BoardDetailView(DetailView):

    model = Board
