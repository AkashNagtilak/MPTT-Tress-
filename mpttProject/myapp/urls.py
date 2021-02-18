from django.urls import path, include
from myapp import views

urlpatterns = [
    path(r'^genres/$',views.show_genres),
]
