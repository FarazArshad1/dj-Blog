from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', view=views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', view=views.post_detail, name= 'post_detail'),
]


