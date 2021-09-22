from django.urls import path
from rest_framework import routers
from .views import SpecialistsModelViewSet

urlpatterns = [

]


router = routers.SimpleRouter()
router.register('specialists', SpecialistsModelViewSet)

urlpatterns += router.urls












