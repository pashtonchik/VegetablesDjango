from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register('api/vegetables', VegetablesViewSet, 'Vegetables')

urlpatterns = [
] + router.urls
