from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostView.as_view()),
    path('<int:user_id>/', views.PostView.as_view()),
    path('<int:user_id>/<int:post_id>', views.PostView.as_view())
]
