from django.contrib import admin
from django.contrib.auth import views as contrib_view
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as users_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register/', users_view.register, name='register'),
    path('login/', contrib_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', contrib_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('UpdateProfile/', users_view.update_profile, name='update-profile'),
    path('profile/', users_view.profile, name='profile'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
