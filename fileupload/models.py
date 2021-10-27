from django.db import models
import uuid

#
# def get_exif(fn):
#     ret = {}
#     i = Image.open(fn)
#     info = i._getexif()
#     for tag, value in info.items():
#         decoded = TAGS.get(tag, tag)
#         ret[decoded] = value
#     return ret
# Create your models here.
class image(models.Model):
    pic=models.ImageField()
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    def __str__(self):
        return str(self.id)
