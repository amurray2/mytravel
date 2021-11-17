from django.urls import path
from .views import showtripsPageView, showAfricaPageView, showAsiaPageView, showEuropePageView, showAustraliaPageView, showNorthAmericaPageView, showSouthAmericaPageView

urlpatterns = [
    path("africa/", showAfricaPageView, name="africa"),
    path("asia/", showAsiaPageView, name="asia"),
    path("australia/", showAustraliaPageView, name="australia"),
    path("europe/", showEuropePageView, name="europe"),
    path("northamerica/", showNorthAmericaPageView, name="northamerica"),
    path("southamerica/", showSouthAmericaPageView, name="southamerica"),
    path("", showtripsPageView, name="showtrips"),
]
