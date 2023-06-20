from django.contrib import admin
from django.urls import path, include

from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    path('accounts/register/', RegistrationView.as_view(success_url='/profile/'), name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

    path('', include('articles.urls'))
]
