from django.db import models
from django.contrib.auth.models import User
from career.models import Career
from library.models import Module

class Stage(models.Model):
    stage = models.IntegerField(
        verbose_name = "Etapa"
        )
    application_date = models.DateTimeField(
        verbose_name = "Fecha de aplicacion")
    
    
    @property
    def year(self):
        return self.application_date.year
    
    @property
    def month(self):
        months = ['enero', 'febrero',
            'marzo', 'april','mayo', 'junio',
            'julio', 'agosto','septiembre', 'octubre',
            'noviembre', 'Diciembre' ]
        return months[self.application_date.month - 1]
    
    def __srt__(self):
        return f"{self.stage} - { self.month } { self.year}"
    
    class Meta:
        verbose_name = "Etapa"
        verbose_name_plural = "Etapas"
 
class Exam(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        verbose_name = "Usuario")
    stage = models.ForeignKey(
                Stage,
                on_delete = models.CASCADE,
                verbose_name = "Etapa")
    career = models.ForeignKey(
                Career,
                on_delete = models.CASCADE,
                verbose_name = "Carrera")
    modules = models.ManyToManyField(
                Module,
                through='ExamModule',
                verbose_name = "Modulos"
                )
                
    score = models.FloatField(
                verbose_name = "Calificación",
                default = 0.0)        
    
class ExamModule(models.Model):
    exam = models.ForeignKey(
                Exam,
                on_delete = models.CASCADE
                )
    module = models.ForeignKey(
                Module,
                on_delete = models.CASCADE
                )
    active = models.BooleanField(
                verbose_name = "Activo",
                default = True)
    score = models.FloatField(
                verbose_name = "",
                default = 0.0)    