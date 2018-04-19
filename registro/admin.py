# -*- coding: utf-8 -*-
from django.contrib import admin
from registro.models import Revista, Libro, Proyecto, Curso, Participante, Evento, Investigador

class ParticipanteAdmin(admin.ModelAdmin):
	model = Participante
	list_display = ['cod_part', 'part_ced', 'part_nom', 'part_ape', 'part_cor']

class CursoAdmin(admin.ModelAdmin):
	model = Curso
	list_display = ['cod_cur', 'cur_nom', 'cur_date_ini', 'cur_date_fin', 'get_cur_ins']

class RevistaAdmin(admin.ModelAdmin):
	model = Revista
	list_display = ['rev_num', 'rev_nom', 'rev_date', 'rev_arb', 'rev_cenditel', 'rev_url']

class LibroAdmin(admin.ModelAdmin):
	model = Libro
	list_display = ['cod_lib', 'lib_nom', 'lib_date', 'lib_cenditel', 'lib_url']

class ProyectoAdmin(admin.ModelAdmin):
	model = Proyecto
	list_display = ['cod_pto', 'pto_nom', 'pto_date_ini', 'pto_date_fin', 'pto_poa']

class EventoAdmin(admin.ModelAdmin):
	model = Evento
	list_display = ['cod_even', 'even_nom', 'even_date_ini', 'even_date_fin', 'even_site', 'get_even_part', 'even_url']

class InvestigadorAdmin(admin.ModelAdmin):
	model = Investigador
	list_display = ['cod_in', 'in_ced', 'in_nom', 'in_ape', 'get_in_pro', 'in_act']

admin.site.register(Revista, RevistaAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Participante, ParticipanteAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Investigador, InvestigadorAdmin)

