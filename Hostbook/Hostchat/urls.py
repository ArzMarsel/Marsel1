from . import views
from django.urls import path

urlpatterns = [
    path('', views.MyListView.as_view, name='host'),
    path('chat/', views.MylistView1.as_view, name='chat'),
    # path(''),
    # path()
]