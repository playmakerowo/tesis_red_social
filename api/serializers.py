from socialDuoc.models import EventoAgendado
from rest_framework import serializers

class EventosSerializers(serializers.ModelSerializer):
    class Meta:
        model = EventoAgendado
        fields = ["nom_even", "descrip", "fecha","fechafin", "estado"]