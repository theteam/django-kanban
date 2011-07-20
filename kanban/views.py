from django.views.generic import DetailView, ListView

from kanban.models import Category, Board


class CategoryListView(ListView):
    
    model = Category


class BoardListView(ListView):

    model = Board


class BoardDetailView(DetailView):

    model = Board
