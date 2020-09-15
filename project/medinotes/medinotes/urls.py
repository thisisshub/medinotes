from django.contrib import admin
from django.urls import path, include

# views
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include("users.urls")),
    path('', include("notes.urls")),
    path('accounts/', include("allauth.urls")),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]