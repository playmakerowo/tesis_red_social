from django.shortcuts import render
from socialDuoc.models import EventoAgendado
from .serializers import EventosSerializers
from rest_framework import generics

# Create your views here.

class EventosViewSet(generics.ListAPIView):
    queryset = EventoAgendado.objects.all()
    serializer_class = EventosSerializers


class EventosBuscarViewSet(generics.ListAPIView):
    serializer_class = EventosSerializers
    def get_queryset(self):
        id_evento = self.kwargs['id_evento']
        return EventoAgendado.objects.filter(id_evento=id_evento)
