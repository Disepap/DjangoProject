from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'eleves', views.EleveViewSet)
router.register(r'professeurs', views.ProfesseurViewSet)
router.register(r'classes', views.ClasseViewSet)
router.register(r'matieres', views.MatiereViewSet)
router.register(r'moyennes', views.MoyenneViewSet)

urlpatterns = [
    #path('', views.index, name ='index'),
    path('',include(router.urls)),
]
