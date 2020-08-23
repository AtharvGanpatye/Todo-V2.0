from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns=[
	path('', views.index, name='index'),
	path('login/', views.user_login, name='user_login'),
	path('show_todos/', views.show_todos, name='show_todos'),
	path('invalid_login/', views.invalid_login, name='invalid_login'),
	path('logout/', views.user_logout, name='logout'),
	path('register/', views.register, name='register'),
	path('delete_item/<int:pk>/', views.delete_item, name='delete_item'),
	path('add_item/', views.add_item, name='add_item')
]