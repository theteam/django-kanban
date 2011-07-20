from django.conf.urls.defaults import patterns, url

from kanban.views import BoardDetailView, BoardListView, CategoryListView

urlpatterns = patterns('kanban.views',
        url(r'^categories/', CategoryListView.as_view(),
            name="kanban_category_list"),
        url(r'^category/(?P<cat_slug>[\w-]+)', BoardListView.as_view(),
            name="kanban_board_list"),
        url(r'^(?P<slug>[\w-]+)', BoardDetailView.as_view())
)
