from django import forms
from django.contrib.auth.models import User
from .models import Poslovi, Vozilo, Radnik, Prihodi, Rashodi, Dan, Zanimanja, Akontacije, Komentar, RucnoLD, Komentar_za_vozilo

class DateInput(forms.DateInput):
    input_type = 'date'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

class ZanimanjeForm(forms.ModelForm):
    class Meta:
        model = Zanimanja
        fields = ['zanimanje']

class PosloviForm(forms.ModelForm):
    pocetak_radova = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y', attrs={'class': "datum"}),
        input_formats=('%d.%m.%Y', '%d/%m/%Y', '%d.%m.%y', '%d/%m/%y'))
    kraj_radova = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y', attrs={'class': "datum"}),
        input_formats=('%d.%m.%Y', '%d/%m/%Y', '%d.%m.%y', '%d/%m/%y'),
        required=False)
    class Meta:
        model = Poslovi
        fields = ['ime', 'opis', 'dogovoreni_radni_sati', 'dogovoreni_radni_sati_klasa_2', 'dogovoreni_radni_sati_klasa_3', 'dogovoreni_radni_sati_klasa_4', 'dogovoreni_radni_sati_klasa_5', 'dogovoreno_po_kvadratu', 'pocetak_radova', 'kraj_radova']

class RadnikForm(forms.ModelForm):
    poceo_raditi = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y', attrs={'class': "datum"}), input_formats=('%d.%m.%Y', '%d/%m/%Y', '%d.%m.%y', '%d/%m/%y'))
    ugovor_vazi_do = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y', attrs={'class': "datum"}), input_formats=('%d.%m.%Y', '%d/%m/%Y', '%d.%m.%y', '%d/%m/%y'))
    class Meta:
        model = Radnik
        fields = ['ime', 'oib', 'datum_rodjenja', 'prebivaliste', 'poceo_raditi', 'ugovor_vazi_do', 'satnica', 'broj_telefona', 'broj_odela', 'broj_cipela', 'zaduzena_oprema', 'zanimanja', 'u_radnom_odnosu', 'klasa', 'komentar']
        widgets = {
            'zanimanja': forms.CheckboxSelectMultiple,
            'komentar': forms.Textarea
        }

class VoziloForm(forms.ModelForm):
    registracija_istice = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y', attrs={'class': "datum"}), input_formats=('%d.%m.%Y', '%d/%m/%Y', '%d.%m.%y', '%d/%m/%y'))
    class Meta:
        model = Vozilo
        fields = ['marka', 'registracija', 'predjeni_kilometri', 'registracija_istice', 'sledeci_servis', 'potrosnja_goriva', 'trenutno_duzi', 'opis']
        widgets = {
            'opis': forms.Textarea
        }

class RadnikForm__old(forms.ModelForm):
    class Meta:
        model = Radnik
        fields = ['ime', 'oib', 'poceo_raditi', 'ugovor_vazi_do', 'satnica', 'broj_telefona', 'broj_odela', 'broj_cipela', 'zaduzena_oprema', 'zanimanja']
        widgets = {
            'poceo_raditi': DateInput(),
            'ugovor_vazi_do': DateInput(),
            'zanimanja': forms.CheckboxSelectMultiple
        }

class PrihodiForm(forms.ModelForm):
    datum = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y', attrs={'class': "datum"}),
        input_formats=('%d.%m.%Y', '%d/%m/%Y', '%d.%m.%y', '%d/%m/%y'))
    class Meta:
        model = Prihodi
        fields = ['datum', 'vrsta', 'kolicina']

class RashodiForm(forms.ModelForm):
    datum = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y', attrs={'class': "datum"}),
        input_formats=('%d.%m.%Y', '%d/%m/%Y', '%d.%m.%y', '%d/%m/%y'))
    class Meta:
        model = Rashodi
        fields = ['datum', 'vrsta', 'kolicina', 'vozilo']


class KvadratForm(forms.Form):
    datum = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y', attrs={'class': "datum"}),
        input_formats=('%d.%m.%Y', '%d/%m/%Y', '%d.%m.%y', '%d/%m/%y'))
    kolicina = forms.FloatField(label="kolicina")


class DatumForm(forms.Form):
    mesec = forms.IntegerField(max_value=12, min_value=1)
    godina = forms.IntegerField(label="godina")
    posao = forms.ModelChoiceField(queryset=Poslovi.objects.all(), required=False)

class Datum_finansForm(forms.Form):
    od_meseca = forms.IntegerField(max_value=12, min_value=1, required=False)
    do_meseca = forms.IntegerField(max_value=12, min_value=1, required=False)
    godina = forms.IntegerField(label="godina")

class DanForm(forms.ModelForm):
    class Meta:
        model = Dan
        fields = ['radio_sati', 'ishrana', 'smestaj', 'bolovanje', 'dozvoljeno_odsustvo', 'nedozvoljeno_odsustvo', 'doprinos_dodat']

class AkontacijeForm(forms.ModelForm):
    class Meta:
        model = Akontacije
        fields = ['kolicina']

class KomentarForm(forms.ModelForm):
    datum = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y', attrs={'class': "datum"}),
        input_formats=('%d.%m.%Y', '%d/%m/%Y', '%d.%m.%y', '%d/%m/%y'),
        required=False)
    class Meta:
        model = Komentar
        fields = ['datum', 'komentar']

class Komentar_za_voziloForm(forms.ModelForm):
    datum = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y', attrs={'class': "datum"}),
        input_formats=('%d.%m.%Y', '%d/%m/%Y', '%d.%m.%y', '%d/%m/%y'),
        required=False)
    class Meta:
        model = Komentar_za_vozilo
        fields = ['datum', 'komentar_vozilo']

class RucnoLDForm(forms.ModelForm):
    class Meta:
        model = RucnoLD
        fields = ['kolicina', 'komentar']