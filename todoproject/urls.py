from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='TO DO API')

urlpatterns = [
    path('api_documentation/', schema_view),
    path('admin/', admin.site.urls),
    path('', include('poll.urls')),
    path('api/auth/', include('authentication.urls')),
    path('tasks/', include('tasks.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
