from django.urls import path
from.views import *


app_name = "btelecomapp"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("search_results/", SearchResultsView.as_view(), name="search_results"),
    path("form/", FormView.as_view(), name="form"),
    path("dataform/", SearchView.as_view(), name="SearchView"),
    ]
