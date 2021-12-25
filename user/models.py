from django.db import models
from django.core.validators import RegexValidator


class Rentee(models.Model):
    name = models.CharField(max_length=255)
    additional_info = models.CharField(max_length=255)
    phone_regex = RegexValidator(regex=r"^(998)?\d{9}\Z", message="Telefon raqam noto'g'ri.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return self.name


class RenteeImages(models.Model):
    rentee = models.ForeignKey(Rentee, on_delete=models.CASCADE)
    image = models.ImageField()