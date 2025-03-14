from django.test import TestCase
from .models import Productor

class ProductorTestCase(TestCase):
    def setUp(self):
        Productor.objects.create(documento="12345", nombre="Juan", apellido="Pérez", telefono="123456789", correo="juan@example.com")

    def test_creacion_productor(self):
        productor = Productor.objects.get(documento="12345")
        self.assertEqual(productor.nombre, "Juan")
