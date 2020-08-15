from django.urls import path

from authentication import views


app_name = 'authentication'
urlpatterns = [
    path('retrieve/<int:pk>/',
         views.RetrieveUserView.as_view(), name='retrieve'),
    path('edit/<int:pk>/', views.EditUserView.as_view(), name='edit'),
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('list/', views.ListUsersView.as_view(), name='list'),
]
