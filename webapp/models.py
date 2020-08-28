from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.urls import reverse
# Create your models here.


class Obavestenje(models.Model):

	STATUS_CHOICES = (

			('nacrt', 'NACRT'),
			('objavljen', 'Objavljen')

		)

	naslov = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique_for_date = 'datum_objave')

	autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postavljena_obavestenja')

	sadrzaj = models.TextField()

	dokument = models.FileField(upload_to='pdfs/', blank=True)

	datum_objave = models.DateTimeField(default=timezone.now)

	kreiran = models.DateTimeField(auto_now_add=True)

	azuriran = models.DateTimeField(auto_now=True)

	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='objavljen')

	class Meta:

		ordering = ('-datum_objave',)

	def __str__(self):
		return self.naslov



	def get_absolute_url(self):
		return reverse('webapp:obavestenje_detalji',args=[self.datum_objave.year, self.datum_objave.month, self.datum_objave.day, self.slug])



class Kontakt(models.Model):
	funkcija = models.CharField(max_length=250)
	ime = models.CharField(max_length=50)
	prezime = models.CharField(max_length=100)
	adresa = models.CharField(max_length=250)
	telefon = models.CharField(max_length=50)


