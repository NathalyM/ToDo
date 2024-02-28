from rest_framework import serializers
from .models import Project

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','titulo','comentario','usuario','fecha_crea')
        read_only_fields =('fecha_crea', )