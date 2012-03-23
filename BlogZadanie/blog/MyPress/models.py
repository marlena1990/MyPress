from django.db import models

# Create your models here.

class Uzytkownik(models.Model):
	uzytkownik_id = models.AutoField(primary_key=True)
	haslo = models.CharField('haslo', max_length=20)
	email = models.EmailField('e-mail', max_length=30)
	def __unicode__(self):
		return str(self.uzytkownik_id)
	class Meta:
		verbose_name = "uzytkownika"
		verbose_name_plural = "Uzytkownicy"

class Strona(models.Model):
	strona_id = models.AutoField(primary_key=True)
	folder = models.CharField('folder', max_length=20)
	uzytkownik_id = models.ForeignKey(Uzytkownik)
	nazwaStrony = models.CharField('nazwa strony', max_length=45)
	opisStrony = models.TextField('opis strony')
	kategoriaStrony = models.CharField('kategoria strony', max_length=20)
	adresLogo = models.CharField('adres logo strony', max_length=255)
	kolorTla = models.CharField('kolor tla strony', max_length=20)
	def __unicode__(self):
                return self.nazwaStrony
	class Meta:
		verbose_name = "strone"
		verbose_name_plural = "Strony"

class Redaktor(models.Model):
	strona_id = models.ForeignKey(Strona)
	uzytkownik_id = models.ForeignKey(Uzytkownik)
	def __unicode__(self):
		return str(self.id)
	class Meta:
		verbose_name = "redaktora"
		verbose_name_plural = "Redaktorzy"

class WiadomoscPrywatna(models.Model):
	wiadomosc_id = models.AutoField(primary_key=True)
	nadawca = models.ForeignKey(Uzytkownik)
	tytulWiadomosci = models.CharField('tytul wiadomosci', max_length=45)
	trescWiadomosci = models.TextField('tresc wiadomosci')
	dataWyslania = models.DateTimeField('data wyslania wiadomosci')
	odbiorca = models.IntegerField('odbiorca')
	czyOdebrana = models.BooleanField('potwierdzenie odebrania wiadomosci')
	def __unicode__(self):
		return str(self.wiadomosc_id)
	class Meta:
		verbose_name = "wiadomosc prywatna"
		verbose_name_plural = "Wiadomosci Prywatne"

class AnkietaPytania(models.Model):
	ankieta_id = models.AutoField(primary_key=True)
	uzytkownik_id = models.ForeignKey(Uzytkownik)
	pytanieAnkiety = models.CharField('pytanie dotyczace ankiety', max_length=45)
	czasRozpoczecia = models.DateTimeField('data rozpoczecia ankiety')
	czasZakonczenia = models.DateTimeField('data zakonczenie ankiety')
	rodzajAnkiety = models.IntegerField('numer rodzaju ankiety')
	def __unicode__(self):
		return str(self.ankieta_id)
	class Meta:
		verbose_name = "pytanie do ankiety"
		verbose_name_plural = "Pytania Ankiet"

class AnkietaOdpowiedzi(models.Model):
	odpowiedz_id = models.AutoField(primary_key=True)
	ankieta_id = models.ForeignKey(AnkietaPytania)
	odpowiedzAnkiety = models.CharField('odpowiedz dotyczaca ankiety', max_length=45)
	def __unicode__(self):
		return str(self.odpowiedz_id)
	class Meta:
		verbose_name = "odpowiedz do ankiety"
		verbose_name_plural = "Odpowiedzi Ankiet"

class OdpUzytkownika(models.Model):
	uzytkownik_id = models.ForeignKey(Uzytkownik)
	odpowiedz_id = models.ForeignKey(AnkietaOdpowiedzi)
	def __unicode__(self):
		return str(self.id)
	class Meta:
		verbose_name = "odpowiedz uzytkownika"
		verbose_name_plural = "Odpowiedzi Uzytkownikow"

class Kategoria(models.Model):
	kategoria_id = models.AutoField(primary_key=True)
	nazwaKategorii = models.CharField('nazwa kategorii', max_length=45)
	opisKategorii = models.TextField('opis kategorii')
	def __unicode__(self):
		return self.nazwaKategorii
	class Meta:
		verbose_name = "kategorie"
		verbose_name_plural = "Kategorie"

class Tag(models.Model):
	tag_id = models.AutoField(primary_key=True)
	nazwaTagu = models.CharField('nazwa tagu', max_length=20)
	def __unicode__(self):
                return self.nazwaTagu
	class Meta:
		verbose_name = "tag"
		verbose_name_plural = "Tagi"

class Artykul(models.Model):
	artykul_id = models.AutoField(primary_key=True)
	kategoria_id = models.ForeignKey(Kategoria)
	uzytkownik_id = models.ForeignKey(Uzytkownik)
	tytulArty = models.CharField('tytul artykulu', max_length=45)
	trescArty = models.TextField('tresc artykulu')
	dataWydania = models.DateTimeField('data wydania artykulu')
	def __unicode__(self):
		return str(self.artykul_id)
	class Meta:
		verbose_name = "artykul"
		verbose_name_plural = "Artykuly"

class TagiArtykulu(models.Model):
	artykul_id = models.ForeignKey(Artykul)
	tag_id = models.ForeignKey(Tag)
	def __unicode__(self):
		return str(self.id)
	class Meta:
		verbose_name = "tag do artykulu"
		verbose_name_plural = "Tagi Artykulow"

class Komentarz(models.Model):
	komentarz_id = models.AutoField(primary_key=True)
	uzytkownik_id = models.ForeignKey(Uzytkownik)
	artykul_id = models.ForeignKey(Artykul)
	trescKomentarza = models.TextField('tresc komentarza')
	dataWyst = models.DateTimeField('data wystawienia komentarza')
	def __unicode__(self):
		return str(self.komentarz_id)
	class Meta:
		verbose_name = "komentarz"
		verbose_name_plural = "Komentarze"			
	
	
