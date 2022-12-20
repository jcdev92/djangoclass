from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UploadSerializer
from rest_framework.decorators import api_view

class StatusView(APIView):

    def get(self, request):
        return Response({'status': 'ok'}, status=status.HTTP_200_OK)

class FileUploadView(APIView):

    serializer_class = UploadSerializer

    def get(self, request):
        return Response('hi')

    def post(self, request):
        file_upload = request.FILES.get('file_upload')
        f= file_upload.open()
        content_type = file_upload.content_type
        response = {
            'result': 'file uploaded successfully',
            'content_type': content_type,
            'value': f.read(),
        }

        return Response(response, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message':'Get some data', 'data': request.data})
    return Response({'message': 'Hello, World!'})