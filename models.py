from django.db import models


class Recinto(models.Model):
    id_recinto = models.AutoField(primary_key=True)
    nombre_recinto = models.CharField(max_length=100)
    tipo_habitat = models.CharField(max_length=50)
    capacidad_animales = models.IntegerField()
    dimensiones_m2 = models.DecimalField(max_digits=10, decimal_places=2)
    ubicacion = models.CharField(max_length=100)
    temperatura_controlada = models.BooleanField()
    ultima_limpieza = models.DateTimeField()
    descripcion_caracteristicas = models.TextField()

    def __str__(self):
        return self.nombre_recinto


class Animal(models.Model):
    id_animal = models.AutoField(primary_key=True)
    nombre_animal = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1)
    recinto = models.ForeignKey(Recinto, on_delete=models.CASCADE)
    dieta = models.TextField()
    estado_salud = models.CharField(max_length=50)
    fecha_adquisicion = models.DateField()
    origen = models.CharField(max_length=100)
    chip_identificacion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_animal


class Cuidador(models.Model):
    id_cuidador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad_animal = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    turno = models.CharField(max_length=50)
    certificaciones = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class ActividadCuidado(models.Model):
    id_actividad = models.AutoField(primary_key=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    cuidador = models.ForeignKey(Cuidador, on_delete=models.CASCADE)
    fecha_actividad = models.DateTimeField()
    tipo_actividad = models.CharField(max_length=100)
    observaciones = models.TextField()
    duracion_minutos = models.IntegerField()
    medicamentos_administrados = models.TextField()

    def __str__(self):
        return f"{self.tipo_actividad} - {self.fecha_actividad}"


class Visitante(models.Model):
    id_visitante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)
    tipo_entrada_comprada = models.CharField(max_length=50)
    fecha_visita = models.DateField()
    pais_origen = models.CharField(max_length=50)
    es_membresia_anual = models.BooleanField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Entrada(models.Model):
    id_entrada = models.AutoField(primary_key=True)
    tipo_entrada = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    validez_dias = models.IntegerField()
    beneficios_incluidos = models.TextField()
    es_para_nino = models.BooleanField()
    es_para_adulto = models.BooleanField()

    def __str__(self):
        return self.tipo_entrada


class VentaEntrada(models.Model):
    id_venta = models.AutoField(primary_key=True)
    visitante = models.ForeignKey(Visitante, on_delete=models.CASCADE)
    entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField()
    cantidad = models.IntegerField()
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    fecha_uso_entrada = models.DateField()
    empleado_venta = models.ForeignKey(Cuidador, on_delete=models.CASCADE)

    def __str__(self):
        return f"Venta {self.id_venta}"
