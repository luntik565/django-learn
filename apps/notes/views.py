from rest_framework import generics, status
from rest_framework.response import Response
from .models import Notes
from .serializator import Noteserializer, NoteCreate, NoteupdateSerializer

class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Notes.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return NoteCreate
        return Noteserializer

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notes.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return NoteupdateSerializer
        return Noteserializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object() # Исправлена опечатка
        self.perform_destroy(instance)
        return Response(
            {'message': 'Заметка удалена'}, 
            status=status.HTTP_204_NO_CONTENT
        )