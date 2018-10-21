from django.db import models
from django.utils.encoding import smart_text
from django.utils import timezone

class ContactModel(models.Model):
    contact_name = models.CharField(max_length=50)
    contact_email = models.EmailField(max_length=30)
    contact_phone = models.CharField(max_length=30)
    contact_sent_date = models.DateTimeField(max_length=35,default=timezone.now)
    contact_message = models.TextField(max_length=500)

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

    def __str__(self):
        return smart_text("{} | {} | {}".format(self.contact_name,self.contact_email,self.contact_sent_date))

