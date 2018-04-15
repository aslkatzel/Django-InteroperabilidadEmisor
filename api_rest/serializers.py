# -*- coding: utf-8 -*-	
from django.contrib.auth.models import User
from rest_framework import serializers
from registro.models import Evento, Revista, Curso, Analista, Proyecto, Libro, Participante

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = ('cod_even', 'even_nom', 'even_date_ini', 'even_date_fin', 'even_site', 'get_even_part', 'even_url')


class RevistaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Revista
        fields = ('rev_num', 'rev_nom', 'rev_date', 'rev_arb', 'rev_cenditel', 'rev_url')


class CursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curso
        fields = ('cod_cur', 'cur_nom', 'cur_date_ini', 'cur_date_fin', 'get_cur_ins')


class AnalistaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ('cod_inv', 'inv_ced', 'inv_nom', 'inv_ape', 'get_inv_pro', 'inv_activo')


class ProyectoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('cod_pto', 'pto_nom', 'pto_date_ini', 'pto_date_fin', 'pto_poa')


class LibroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Libro
        fields = ('cod_lib', 'lib_nom', 'lib_date', 'lib_cenditel', 'lib_url')


class ParticipanteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Participante
        fields = ('cod_part', 'part_ced', 'part_nom', 'part_ape', 'part_cor') 

