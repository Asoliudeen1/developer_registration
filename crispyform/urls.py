
from django.contrib import admin
from django.urls import path, include
from crispyform import settings
from django.conf.urls.static import static

# ADMIN PANEL (TITLE)
admin.site.site_header = "HR ADMIN"
admin.site.index_title = "Table of candidates"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
