from django.urls import path

from authentication import views


app_name = 'authentication'
urlpatterns = [
    path('retrieve/<int:pk>', views.RetrieveUserView.as_view()),
    path('edit/<int:pk>', views.EditUserView.as_view()),
    path('create/', views.CreateUserView.as_view()),
]
