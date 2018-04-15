# -*- coding: utf-8 -*-

from django.db import models

from django.core.urlresolvers import reverse


# Create your models here.

class Participante(models.Model):
    cod_part = models.CharField('Código del Participante', max_length=10, unique=True)
    part_ced = models.CharField('Cédula de Identidad', max_length=200, unique=True)
    part_nom = models.CharField('Nombres', max_length=200)
    part_ape = models.CharField('Apellidos', max_length=200)
    part_cor = models.EmailField('Correo Electrónico')

    def __str__(self):
        return self.cod_part


class Curso(models.Model):
    cod_cur = models.CharField('Código Indentificación', max_length=200, unique=True)
    cur_nom = models.CharField('Nombre del Curso', max_length=200)
    cur_date_ini = models.DateField('Fecha de Inicio', auto_now=False, auto_now_add=False, null=True, blank=True)
    cur_date_fin = models.DateField('Fecha Finalización', auto_now=False, auto_now_add=False, null=True, blank=True)
    cur_ins = models.ManyToManyField(Participante)

    def get_cur_ins(self):
        return ", ".join([str(p) for p in self.cur_ins.all()])

    def __str__(self):
        return self.cod_cur


class Proyecto(models.Model):
    cod_pto = models.CharField('Código Indentificación', max_length=200, unique=True)
    pto_nom = models.CharField('Nombre del Proyecto', max_length=200)
    pto_date_ini = models.DateField('Fecha de Inicio', auto_now=False, auto_now_add=False, null=True, blank=True)
    pto_date_fin = models.DateField('Fecha Finalización', auto_now=False, auto_now_add=False, null=True, blank=True)
    pto_poa = models.BooleanField('¿Pertenece al POA?')

    def __str__(self):
        return self.cod_pto


class Analista(models.Model):
    cod_inv = models.CharField('Código del Analista', max_length=10, unique=True)
    inv_ced = models.CharField('Cédula de Identidad', max_length=200, unique=True)
    inv_nom = models.CharField('Nombres', max_length=200)
    inv_ape = models.CharField('Apellidos', max_length=200)
    inv_pro = models.ManyToManyField(Proyecto, help_text="Proyectos")
    inv_activo = models.BooleanField('¿Se encuentra activo?')

    def get_inv_pro(self):
        return ", ".join([str(p) for p in self.inv_pro.all()])

    def __str__(self):
        return self.cod_inv


class Libro(models.Model):
    cod_lib = models.CharField('Código Indentificación', max_length=200, unique=True)
    lib_nom = models.CharField('Título del Libro', max_length=200)
    lib_date = models.DateField('Fecha de Publicación', auto_now=False, auto_now_add=False, null=True, blank=True)
    lib_cenditel = models.BooleanField('¿Realizado en CENDITEL?')
    lib_url = models.CharField('URL Visualización', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.cod_lib


class Revista(models.Model):
    rev_num = models.CharField('Número de la Revista', max_length=200, unique=True)
    rev_nom = models.CharField('Título de la Revista', max_length=200)
    rev_date = models.DateField('Fecha de Publicación', auto_now=False, auto_now_add=False, null=True, blank=True)
    rev_arb = models.BooleanField('¿Revista Arbitrada?')
    rev_cenditel = models.BooleanField('¿Realizado en CENDITEL?')
    rev_url = models.CharField('URL Visualización', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.rev_num


class Evento(models.Model):
    cod_even = models.CharField('Código Indentificación', max_length=200, unique=True)
    even_nom = models.CharField('Nombre del Evento', max_length=200) 
    even_date_ini = models.DateField('Fecha de Inicio', auto_now=False, auto_now_add=False, null=True, blank=True)
    even_date_fin = models.DateField('Fecha de Finalización', auto_now=False, auto_now_add=False, null=True, blank=True)
    even_site = models.TextField('Lugar del EVento', max_length=500, null=True, blank=True)
    even_part = models.ManyToManyField(Participante)
    even_url = models.URLField(null=True, blank=True)

    def get_even_part(self):
        return ", ".join([str(p) for p in self.even_part.all()])

    def __str__(self):
        return self.cod_even