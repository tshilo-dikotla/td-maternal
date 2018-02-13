from django.urls.conf import path
from django.views.generic.base import RedirectView

from .admin_site import td_maternal_admin

app_name = 'td_maternal'

urlpatterns = [
    path('admin/', td_maternal_admin.urls),
    path('', RedirectView.as_view(url='admin/'), name='home_url'),
]
