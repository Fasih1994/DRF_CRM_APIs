from django.urls import path, include
from rest_framework.routers import DefaultRouter

from manifest.manifest_views import ManifestHdrLnsGetView, ManifestHdrLnsPostView, ManifestHdrGetView, ManifestLnsGetView, ManifestHdrDelView, ManifestLnsDelView

router = DefaultRouter()
router.register(prefix="manifest", viewset=ManifestHdrLnsGetView, basename="manifest-hdr-lns-get")
router.register(prefix="manifestHdr", viewset=ManifestHdrGetView, basename="manifest-headers")
router.register(prefix='manifestLns',viewset=ManifestLnsGetView, basename='Lns-view')
# router.register(prefix="postManifest", viewset=ManifestHdrLnsPostView, basename="hdr-ln-post")

urlpatterns = [
    path('', include(router.urls)),
    path("postManifest/", ManifestHdrLnsPostView.as_view(), name="hdr-ln-post"),
    path("deleteManifest/",ManifestHdrDelView.as_view(),name="mainfest_hdr_del"),
    path("deleteManifestLns/",ManifestLnsDelView.as_view(),name="mainfest_lns_del")
]
