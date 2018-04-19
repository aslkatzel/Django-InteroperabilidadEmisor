# -*- coding: utf-8 -*- 
from django.contrib.auth.models import User
from rest_framework import viewsets
from api_rest.serializers import UserSerializer, EventoSerializer, RevistaSerializer, CursoSerializer, ProyectoSerializer, LibroSerializer, ParticipanteSerializer, InvestigadorSerializer
from registro.models import Evento, Revista, Curso, Proyecto, Libro, Participante, Investigador


class UserViewSet(viewsets.ModelViewSet):
    """
    Final de la API que permite que los usuarios se vean o editen.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class EventoViewSet(viewsets.ModelViewSet):
    """
    Final de la API que permite que los eventos se vean o editen.
    """
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


class RevistaViewSet(viewsets.ModelViewSet):
    """
    Final de la API que permite que las revistas se vean o editen.
    """
    queryset = Revista.objects.all()
    serializer_class = RevistaSerializer


class CursoViewSet(viewsets.ModelViewSet):
    """
    Final de la API que permite que los cursos se vean o editen.
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class ProyectoViewSet(viewsets.ModelViewSet):
    """
    Final de la API que permite que los proyectos se vean o editen.
    """
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer


class LibroViewSet(viewsets.ModelViewSet):
    """
    Final de la API que permite que los libros se vean o editen.
    """
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


class ParticipanteViewSet(viewsets.ModelViewSet):
    """
    Final de la API que permite que los participantes se vean o editen.
    """
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer


class InvestigadorViewSet(viewsets.ModelViewSet):
    queryset = Investigador.objects.all()
    serializer_class = InvestigadorSerializer
