from django.db import models
from django.utils.encoding import smart_text
from django.utils import timezone

# Create your models here.

class ContactModel(models.Model):
    name_contact = models.CharField(max_length=50)
    email_contact = models.CharField(max_length=30)
    phone_contact = models.CharField(max_length=30)
    contact_sent_date = models.CharField(max_length=35,default=timezone.now)

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

    def __str__(self):
        return smart_text(self.name_contact)

