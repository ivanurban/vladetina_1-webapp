from django.contrib import admin

from .models import Obavestenje, Kontakt

# Register your models here.

@admin.register(Obavestenje)
class ObavestenjeAdmin(admin.ModelAdmin):
	list_display = ('naslov', 'slug', 'autor', 'datum_objave', 'status')
	list_filter = ('status', 'kreiran','datum_objave', 'autor')

	search_fields = ('naslov', 'sadrzaj')

	prepopulated_fields = {'slug':('naslov',)}

	raw_id_fields = ('autor',)

	date_hierarchy = 'datum_objave'

	ordering = ('status', 'datum_objave')


admin.site.register(Kontakt)