# HT_WERKE
pocetak projekta 15.05


spisak:
fasader-moler
keramicar
zidar
armirac
tesar
gipsar
elektricar
vodoinstalater

prestanak radnog odnosa

__________________________________________________________________________________________________________


da li se pogadja posao na sat za sve radnike na projektu isti, onda automatska satnica ima smisla

pregledati titlove



----------------------------------------------------




- brisati i akontacije starije od ?  radnike koji nisu u radnom odnosu duze od ? dane koji su ostali u bazi  (nedelje...)
mozda sve objekte starije od tri godine?
- test test test provera svega sto moze ostati u bazi


- na listi vozila izbaciti kilometre i potrosnju  --  ok
- filter radnika na mesecnom izvodu po poslu.  --  ok (testirati odakle krece autoincrement)
- pregled ukupnog rada od pocetka radnog odnosa za svaki mesec koliko danaa radnih, bolovanja, odmora i nedozvoljenog odstustva,
 kad se udje u detalje radnika na dnu stranice  -- ok
- Izbaciti da mora upisati opis posla -- ok
- ako su dogovoreni radni sati 0kn rashod da ide u minus. --  ok
- dan polje ishrana - automatski rashod na trenutnom projektu.  --  ok
- ne unositi svaki dan na kom je poslu radnik, nego racunati rashod na trenutnom poslu!!!  --  ok
- posao dodati polje pocetak posla, kraja. Racunati broj dana..  ukupan broj radnih sati na projektu svih radnika. --  ok
- mesecni pregled radnika akontacija + ishrana, neto ld.  --  ok
- mozda model akontacija: polja: radnik, mesec, godina.  --  ok
- ukupna kolicina troskova za vozilo -- ok
- finansije -> sve poslove koji trenutno imaju radnike (izabrati mesec kao kod radnika) svaki prihod i rashod mora imati polje datum. i na automatsku satnicu dodati datum   --  ok
- dogovoreno po kvadratu  --  ok  (automatsi racunanje prihoda)
- potrebni komentari za posao ili polje u bazi ili word dokument u file field.  --  ok
- posebno obrisi, posebno napravi pdf izvestaj -- ok
- delete posao create log  AKO JE STARIJI OD DVE GODINE prvo ucitati te poslove pa redirect na default index page  --  ok


- onemoguceno dodavanje na posao kroz objekat radnih, dakle MOOORA kroz posao...!!!!!!
- Ako je datum veci od kraja projekta, radnici se ne mogu dodati vise!
- Posao se ne moze obrisati ako nije postavljen datum na kraj projekta
- Brisanjem projekta se brisu svi prihodi, rashodi vezani za taj projekat!!
- Brisanjem radnika se brisu svi dani vezani za radnika!


- na mesecnom pregledu radnika kad se ubaci posao  server error 500  --  ok
- svakako racunaj radne sate na projektu bez obzira da li je dogovoreno ili nije  --  ok
- radnih dana na pregledu radnika racunati ako je unet broj radnih sati  --  ok
- godiste radnika  datum rodjenja  odakle je on  (prebivaliste)  --  ok
- dan dobija polje smestaj, automatski obracunati na poslu broj smestaja i finansijski  --  ok
- mesecni pregled posla radnih sati za sve radnike na tom poslu u tom mesecu i broj spavanja i finansijski -- ok
- stampati saldo radnika -- ok
- brisanje vozila -- ok


- stampati mesecni presek posla na kartici finansije




- PROBLEM JE AKO SE UPISU RADNI SATI A DA JE RADNIK NA POGRESNOM PROJEKTU, OSTAJU RASHODI ZA TAJ PROJEKAT!!




heroku auth:token
heroku run:detached your command here

heroku run -a htwerke python manage.py collectstatic
git add .
git commit -m "poruka"
git push origin master ( ili heroku master, provera na: git remote -v )
heroku config:set DEBUG_COLLECTSTATIC=0


SSH key za firewall

$ssh-keygen -t rsa
$heroku keys:clear
$heroku keys:add 
$git clone git@heroku.com:my-app.git -o heroku



menjano:

views: funkcija detail, radnik_detail, pdf_radnik, dan_update, detail, mesecni_izvod_poslova, dodate funkcije
models: klasa radnik, dan        ---    mora makemigrations  i migrate
forms: radnikform, danform
urls.py: zadnja linija dodata

poslovi.html
radnik_detalji.html
mesecni_izvod_finansije.html
mesecni_izvod.html
base.html
ljudi.html
vozila.html

style.css

logo.png
