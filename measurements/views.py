from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectSerialazer, MeasurementSerialazer
from .models import Project, Measurement


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerialazer
    """ViewSet для проекта."""
    # TODO: добавьте конфигурацию для объекта


class MeasurementViewSet(ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerialazer
    """ViewSet для измерения."""
    # TODO: добавьте конфигурацию для измерения
