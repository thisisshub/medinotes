from django.urls import path
from users.views import HomePageView

# Bridge b/w medinotes.urls -> users.urls -> users.views
urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
]