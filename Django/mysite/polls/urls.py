from django.urls import path

from . import views


# #   http://127.0.0.1:8000/polls/index
# urlpatterns = [
#     path('index', views.index, name='index'),
# ]


#   http://127.0.0.1:8000/polls
urlpatterns = [
    path('', views.index, name='index'),
    path('/about', views.about, name='about'),
]
