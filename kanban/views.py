from django.views.generic import CreateView, DetailView, ListView

from kanban.forms import BoardForm, CategoryForm
from kanban.models import Category, Board


class CategoryCreateView(CreateView):

    form_class = CategoryForm


class CategoryListView(ListView):
    
    model = Category


class BoardCreateView(CreateView):

    form_class = BoardForm

    def get_form_kwargs(self):
        kwargs = super(BoardCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class BoardListView(ListView):

    model = Board


class BoardDetailView(DetailView):

    model = Board
