from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from pass_app.models import PerevalAdded
from pass_app.serializers import PerevalSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all().order_by('-add_time')
    serializer_class = PerevalSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': None,
                'id': serializer.data['id']
            })
        elif status.HTTP_400_BAD_REQUEST:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Bad Request',
                'id': None
            })
        elif status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response({
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': 'Ошибка при подключении к базе данных',
                'id': None
            })
