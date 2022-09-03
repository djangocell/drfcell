from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/v1/cell/", include("apps.cell.urls")),
    path("api/v1/monster/", include("apps.monster.urls")),
    path("api/v1/player/", include("apps.player.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
