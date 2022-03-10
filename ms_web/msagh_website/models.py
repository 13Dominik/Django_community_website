from django.db import models
from django.conf import settings
from django.core.validators import MaxLengthValidator, MinLengthValidator
User = settings.AUTH_USER_MODEL


# Create your models here.
class Spot(models.Model):
    title = models.CharField(validators=[MinLengthValidator(5)], max_length=70)
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,
                             blank=True,
                             null=True,
                             on_delete=models.SET_NULL
                             )
    content = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.title[:10]} - {self.content[:10]}"