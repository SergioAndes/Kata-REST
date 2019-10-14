from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    usuario = models.CharField(max_length=200)
    foto = models.CharField(max_length=200)
    perfilProfesional = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Portafiolio(models.Model):
    nombrePortafolio = models.CharField(max_length=200)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    esPublico = models.BooleanField()

    def __str__(self):
        return self.nombrePortafolio


class Imagen(models.Model):
    titulo = models.CharField(max_length=200)
    enlace = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    tipoDeArchivo = models.CharField(max_length=200)
    esPublica = models.BooleanField()
    portafolio = models.ForeignKey(Portafiolio, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
