from django.db import models
import os

class MonTruc(models.Model):
    name = models.CharField(max_length=200)
    path = models.FileField(upload_to='trucs/')

    def delete(self, *args, **kwargs):
        fichier = self.path

        # Supprime l'objet de la base
        super().delete(*args, **kwargs)

        # Vérifie si le fichier est encore utilisé par d'autres objets
        encore_utilisé = MonTruc.objects.filter(path=fichier.name).exists()

        # Si non utilisé, supprime physiquement le fichier
        if not encore_utilisé and fichier and os.path.isfile(fichier.path):
            os.remove(fichier.path)