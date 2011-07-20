from django.contrib import admin

from kanban.models import Category, Board, State, Card


admin.site.register(Category)
admin.site.register(Board)
admin.site.register(State)
admin.site.register(Card)
