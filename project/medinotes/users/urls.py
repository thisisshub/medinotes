from django.urls import path
from users.views import HomePageView, LoginPageView

# Bridge b/w medinotes.urls -> users.urls -> users.views
urlpatterns = [
    path('', HomePageView.as_view()),
    path('login/', LoginPageView.as_view()),
]
