from django.conf.urls import include, url
from django.contrib import admin

from photos.views import PhotoView
from feedback.views import FeedbackView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', PhotoView.as_view(), name="home"),
    url(r'^feedback/$', FeedbackView.as_view(), name="feedback"),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
