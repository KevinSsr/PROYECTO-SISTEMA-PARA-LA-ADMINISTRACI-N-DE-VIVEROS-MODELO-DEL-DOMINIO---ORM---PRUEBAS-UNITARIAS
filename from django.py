from django.db import models

class Productor(models.Model):
    documento = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"  

class Finca(models.Model):
    numero_catastro = models.CharField(max_length=50, unique=True)
    municipio = models.CharField(max_length=100)
    productor = models.ForeignKey(Productor, on_delete=models.CASCADE, related_name="fincas")

    def __str__(self):
        return f"Finca {self.numero_catastro} - {self.municipio}"  

class Vivero(models.Model):
    codigo = models.CharField(max_length=50)
    tipo_cultivo = models.CharField(max_length=100)
    finca = models.ForeignKey(Finca, on_delete=models.CASCADE, related_name="viveros")

    def __str__(self):
        return f"Vivero {self.codigo} - {self.tipo_cultivo}"  

class Labor(models.Model):
    fecha = models.DateField()
    descripcion = models.TextField()
    vivero = models.ForeignKey(Vivero, on_delete=models.CASCADE, related_name="labores")

    def __str__(self):
        return f"{self.fecha} - {self.descripcion[:30]}..."  

class ProductoControl(models.Model):
    registro_ICA = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    frecuencia_aplicacion = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True  

class ProductoControlHongo(ProductoControl):
    periodo_carencia = models.IntegerField()
    nombre_hongo = models.CharField(max_length=100)

class ProductoControlPlaga(ProductoControl):
    periodo_carencia = models.IntegerField()

class ProductoControlFertilizante(ProductoControl):
    fecha_ultima_aplicacion = models.DateField()
