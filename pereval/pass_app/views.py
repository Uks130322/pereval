from django.db import IntegrityError
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from pass_app.models import PerevalAdded
from pass_app.serializers import PerevalSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all().order_by('-add_time')
    serializer_class = PerevalSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ['user__email']

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

    def update(self, request, *args, **kwargs):
        """Update is possible only for objects with status 'new', user update prohibited"""
        instance = self.get_object()
        try:
            serializer = PerevalSerializer(instance, data=request.data)

            if serializer.is_valid():
                if instance.status != 'new':
                    return Response({
                        'status': 0,
                        'message': 'Эта запись уже на модерации либо прошла модерацию, изменение невозможно'
                    })
                else:
                    serializer.save()
                    self.perform_update(serializer)
                    return Response({
                        'state': 1,
                        'message': ''
                    })
            if status.HTTP_400_BAD_REQUEST:
                return Response({
                    'state': 0,
                    'message': 'Bad Request'
                })

            elif status.HTTP_500_INTERNAL_SERVER_ERROR:
                return Response({
                    'state': 0,
                    'message': 'Ошибка при подключении к базе данных'
                })

        except (IntegrityError, AssertionError):
            return Response({
                'state': 0,
                'message': 'Изменение данных пользователя невозможно'
            })

    def partial_update(self, request, *args, **kwargs):
        return Response({
            'state': 0,
            'message': 'Sorry, this method is not supported. Try PUT instead'
        })
