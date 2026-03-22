from django.urls import path
from .views import NoteDetail, NoteListCreateView
# Здесь ты позже импортируешь свои views, например:
# from .views import MyView 

app_name = 'notes'

urlpatterns = [
    # Пока оставь пустым или добавь временный маршрут
    path('notes/', NoteListCreateView.as_view(), name='note-list-create'), 
    path('notes/<int:pk>', NoteDetail.as_view(), name='note-detail')
]