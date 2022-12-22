from django.db import models

# Create your models here.
class Tipo(models.Model):
    nombre=models.CharField(max_length=30, verbose_name='Tipo', unique=True)
    
    class Meta:
        verbose_name='Tipo'
        verbose_name_plural='Tipos'
        

    def __str__(self):
        return self.nombre


class Grupo(models.Model): #fecha, archivo, tipo, grupo, observaciones
    nombre=models.CharField(max_length=30, verbose_name='Tipo', unique=True)
    
    class Meta:
        verbose_name='Grupo'
        verbose_name_plural='Grupos'
        

    def __str__(self):
        return self.nombre


class Archivos(models.Model):
    fecha=models.DateTimeField(auto_now_add=True)
    tipo=models.ForeignKey(Tipo, on_delete=models.PROTECT )
    #codigo=models.ForeignKey(Codigo, on_delete=models.PROTECT)
    grupo=models.ForeignKey(Grupo, on_delete=models.PROTECT )
    image = models.FileField(upload_to='Documentos/Skillhacking/Archivos', verbose_name='Archivo')
    observaciones=models.TextField(max_length=250, blank=True)

    def __str__(self):
         txt="{0}"
         return txt.format(self.fecha)
    
    class Meta:
        verbose_name='Archivo'
        verbose_name_plural='Archivos'
        ordering =['fecha']  

