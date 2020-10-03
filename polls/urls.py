from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='result'),
    path('<int:question_id>/vote/', views.results, name='vote'),
    path('api/', include(router.urls)),
    path('api/mono', views.mono, name='mono')
]