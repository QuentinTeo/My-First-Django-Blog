from django.urls import path
from . import views


urlpatterns = [
    path('',views.post_list, name='post_list'),#register post_list.html as url
    path('post/<int:pk>/', views.post_detail, name = 'post_detail')
]
