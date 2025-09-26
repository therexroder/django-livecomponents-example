from django.db import models


class Property(models.Model):
    title = models.CharField(max_length=120)
    price = models.PositiveIntegerField()
    city = models.CharField(max_length=255)
    image = models.ImageField(upload_to='properties/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.title

