from django.db import models



# Create your models here.
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