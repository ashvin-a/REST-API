from django.urls import path
from django.contrib import admin
from rest_framework import routers
from core import views as core_views

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('contact/', core_views.ContactAPIView.as_view()),
]