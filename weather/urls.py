from django.urls import path

from . import views

app_name = "weather"
urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("results/", views.results, name="results"),
    path("fiveday/", views.fiveday, name="fiveday")
    #path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    #path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    #path("<int:question_id>/vote/", views.vote, name="vote"),
]