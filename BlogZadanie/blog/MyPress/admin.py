from django.contrib import admin

from blog.MyPress.models import Uzytkownik
from blog.MyPress.models import Strona
from blog.MyPress.models import Redaktor
from blog.MyPress.models import AnkietaPytania
from blog.MyPress.models import AnkietaOdpowiedzi
from blog.MyPress.models import OdpUzytkownika
from blog.MyPress.models import WiadomoscPrywatna
from blog.MyPress.models import Komentarz
from blog.MyPress.models import Artykul
from blog.MyPress.models import Kategoria
from blog.MyPress.models import TagiArtykulu
from blog.MyPress.models import Tag

class UzytkownikAdmin(admin.ModelAdmin):
	list_display = ('uzytkownik_id', 'email')
admin.site.register(Uzytkownik, UzytkownikAdmin)

class StronaAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,						{'fields': ['uzytkownik_id', 'folder']}),
		('Szczegolowy opis strony:',			{'fields': ['nazwaStrony', 'kategoriaStrony', 'opisStrony']}),
		('Wyglad strony:',				{'fields': ['adresLogo', 'kolorTla']}),
	]
	list_display = ('strona_id', 'uzytkownik_id', 'nazwaStrony')
admin.site.register(Strona, StronaAdmin)

class RedaktorAdmin(admin.ModelAdmin):
	list_display = ('id', 'strona_id', 'uzytkownik_id')
admin.site.register(Redaktor, RedaktorAdmin)

class OdpowiedzAnkiety(admin.StackedInline):
	model = AnkietaOdpowiedzi
	extra = 3

class AnkietaPytAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,						{'fields': ['uzytkownik_id']}),
		('Dane dotyczace ankiety:',			{'fields': ['pytanieAnkiety', 'rodzajAnkiety']}),
		('Informacje o czasie trwania ankiety:',	{'fields': ['czasRozpoczecia', 'czasZakonczenia']}),
	]
	inlines = [OdpowiedzAnkiety]
	list_display = ('ankieta_id', 'uzytkownik_id', 'pytanieAnkiety', 'czasRozpoczecia', 'czasZakonczenia')
	list_filter = ['czasRozpoczecia', 'czasZakonczenia']
	date_hierarchy = 'czasRozpoczecia'
admin.site.register(AnkietaPytania, AnkietaPytAdmin)

class AnkietaOdpAdmin(admin.ModelAdmin):
	list_display = ('odpowiedz_id', 'ankieta_id', 'odpowiedzAnkiety')
admin.site.register(AnkietaOdpowiedzi, AnkietaOdpAdmin)

class OdpUzytAdmin(admin.ModelAdmin):
	list_display = ('id', 'uzytkownik_id', 'odpowiedz_id')
admin.site.register(OdpUzytkownika, OdpUzytAdmin)

class WiadomoscPrywatnaAdmin(admin.ModelAdmin):
	list_display = ('wiadomosc_id', 'nadawca', 'odbiorca', 'tytulWiadomosci', 'dataWyslania')
	list_filter = ['dataWyslania']
	date_hierarchy = 'dataWyslania'
admin.site.register(WiadomoscPrywatna, WiadomoscPrywatnaAdmin)

class KomentarzAdmin(admin.ModelAdmin):
	list_display = ('komentarz_id', 'uzytkownik_id', 'artykul_id', 'dataWyst')
	list_filter = ['dataWyst']
	date_hierarchy = 'dataWyst'
admin.site.register(Komentarz, KomentarzAdmin)

class ArtykulAdmin(admin.ModelAdmin):
	fields = ['tytulArty', 'kategoria_id', 'trescArty', 'dataWydania', 'uzytkownik_id']
	list_display = ('tytulArty', 'dataWydania', 'uzytkownik_id')
	list_filter = ['dataWydania']
	date_hierarchy = 'dataWydania'
	search_fields = ['tytulArty']
admin.site.register(Artykul, ArtykulAdmin)

admin.site.register(Kategoria)
admin.site.register(TagiArtykulu)
admin.site.register(Tag)

