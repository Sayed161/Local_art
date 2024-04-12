from django.db import models
from Artists.models import Artists

# Create your models here.
class ArtWorks(models.Model):
    Artworker = models.ForeignKey(Artists,on_delete=models.CASCADE, related_name='artists')
    Title = models.CharField(max_length=256)
    Description = models.TextField()
    Created_date = models.DateTimeField(auto_now_add=True)
    Image_url = models.URLField()

    def __str__(self) -> str:
        return f"{self.Artworker} - {self.Title}"


