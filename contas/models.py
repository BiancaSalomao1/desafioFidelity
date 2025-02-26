from django.db import models

class Usuario(models.Model):
    # Your model fields here
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # ... other fields

    def __str__(self):
        return self.nome # or a relevant field.