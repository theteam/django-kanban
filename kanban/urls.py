from django.conf.urls.defaults import patterns, url

from kanban.views import (BoardCreateView, BoardDetailView, BoardListView, 
                          CategoryCreateView, CategoryListView)

urlpatterns = patterns('kanban.views',
        # Category URLs
        url(r'^categories/', CategoryListView.as_view(),
            name="kanban_category_list"),
        url(r'^categories/create/', CategoryCreateView.as_view(),
            name="kanban_category_create"),
        url(r'^category/(?P<cat_slug>[\w-]+)', BoardListView.as_view(),
            name="kanban_board_list"),

        # Board URLs
        url(r'^board/create/', BoardCreateView.as_view(),
            name="kanban_board_create"),
        url(r'^(?P<slug>[\w-]+)', BoardDetailView.as_view())


)
