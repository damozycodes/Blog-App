import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser, _
#from PIL import Image

from users import validators


class User(AbstractUser):
    id = models.UUIDField(primary_key= True, default= uuid.uuid4, editable= False)

    username = models.Charfield(
        _("username"),
        max_length = 11,
        validator = [validators.UnicodeUsernameValidator]
        )

    country = models.CharField(
        _("country"),
        max_length=225
        )

    description = models.CharField(
        _("description"), 
        max_length=500, 
        blank=True
        )

    phone_number = models.CharField(
        max_length=11,
        unique= True,
        validators= [validators.PhoneNumberValidator],
        )
    
    image = models.ImageField(
        default="default.jpg",
        upload_to="profile_pics"
        )

    def __str__(self):
        return f'{self.User.username} Profile'

    # def save(self):
    #     super().save()

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)chro
    #         img.save(self.image.path)

