from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlPatterns = [
    path('api/eventos/', views.EventosViewSet.as_view()),
    path('api/eventos_buscar/<int:id_evento>/', views.EventosBuscarViewSet.as_view(), name='eventos_buscar'),
]

urlpatterns = format_suffix_patterns(urlPatterns)