from django.conf.urls import url
from . import views


app_name = 'projects'

urlpatterns = [
    url(r'^$', views.sajt, name='sajt'),
    url(r'^administracija/$', views.index, name='index'),
    url(r'^administracija/radnici/$', views.ljudi, name='ljudi'),
    url(r'^administracija/vozila/$', views.vozila, name='vozila'),
    url(r'^administracija/login_user/$', views.login_user, name='login_user'),
    url(r'^administracija/logout_user/$', views.logout_user, name='logout_user'),
    url(r'^administracija/novi_projekat/$', views.create_project, name='project-add'),
    url(r'^administracija/mesecni_pregled_radnika/(?P<mesec>[0-9]+)/(?P<godina>[0-9]+)/(?P<posao_id>[a-zA-Z0-9_.-]+)$', views.mesecni_izvod_radnika, name='monthview-workers'),  # samo string (?P<posao>[\w\-]+)
    url(r'^administracija/mesecni_pregled_poslova/(?P<mesec>[0-9]+)/(?P<godina>[0-9]+)$', views.mesecni_izvod_poslova, name='monthview-projects'),
    url(r'^administracija/posao/(?P<project_id>[0-9]+)/$', views.detail, name='posao'),
    url(r'^administracija/radnik/(?P<radnik_id>[0-9]+)/$', views.radnik_detail, name='radnik-detail'),
    url(r'^administracija/vozilo/(?P<vozilo_id>[0-9]+)/$', views.vozilo_detail, name='vozilo-detail'),
    url(r'^administracija/komentar/(?P<komentar_id>[0-9]+)/$', views.komentar_detail, name='komentar-detail'),
    url(r'^administracija/azuriranje_posla/(?P<project_id>[0-9]+)/$', views.posao_update, name='posao-update'),
    url(r'^administracija/azuriranje_radnika/(?P<radnik_id>[0-9]+)/$', views.radnik_update, name='radnik-update'),
    url(r'^administracija/azuriranje_dana/(?P<dan_id>[0-9]+)/(?P<posao_id>[a-zA-Z0-9_.-]+)$', views.dan_update, name='dan-update'),
    url(r'^administracija/azuriranje_akontacije/(?P<mesec>[0-9]+)/(?P<godina>[0-9]+)/(?P<posao_id>[a-zA-Z0-9_.-]+)/(?P<akontacija_id>[0-9]+)$', views.akontacija_update, name='akontacija-update'),
    url(r'^administracija/azuriranje_licnog_dohodka/(?P<mesec>[0-9]+)/(?P<godina>[0-9]+)/(?P<posao_id>[a-zA-Z0-9_.-]+)/(?P<ld_id>[0-9]+)$', views.licni_dohodak_update, name='licni_dohodak-update'),
    url(r'^administracija/azuriranje_vozila/(?P<vozilo_id>[0-9]+)/$', views.vozilo_update, name='vozilo-update'),
    url(r'^administracija/izmena_komentara/(?P<komentar_id>[0-9]+)/$', views.komentar_update, name='komentar-update'),
    url(r'^administracija/novi_prihod/(?P<project_id>[0-9]+)/$', views.create_prihod, name='prihod-add'),
    url(r'^administracija/novi_rashod/(?P<project_id>[0-9]+)/$', views.create_rashod, name='rashod-add'),
    url(r'^administracija/novi_kvadrati/(?P<project_id>[0-9]+)/$', views.create_kvadrat, name='kvadrat-add'),
    url(r'^administracija/novi_komentar/(?P<project_id>[0-9]+)/$', views.create_komentar, name='komentar-add'),
    url(r'^administracija/novo_zanimanje/$', views.create_zanimanje, name='zanimanje-add'),
    url(r'^administracija/novi_radnik/$', views.create_radnik, name='radnik-add'),
    url(r'^administracija/novo_vozilo/$', views.create_vozilo, name='vozilo-add'),
    url(r'^administracija/posao/(?P<project_id>[0-9]+)/obrisi_prihod/(?P<prihod_id>[0-9]+)/$', views.prihod_delete, name='prihod-delete'),
    url(r'^administracija/(?P<project_id>[0-9]+)/obrisi_rashod/(?P<rashod_id>[0-9]+)/$', views.rashod_delete, name='rashod-delete'),
    url(r'^administracija/(?P<project_id>[0-9]+)/obrisi_komentar/(?P<komentar_id>[0-9]+)/$', views.komentar_delete, name='komentar-delete'),
    url(r'^administracija/obrisi_posao/(?P<posao_id>[0-9]+)/$', views.posao_delete, name='posao-delete'),
    url(r'^administracija/obrisi_radnika/(?P<radnik_id>[0-9]+)/$', views.radnik_delete, name='radnik-delete'),
    url(r'^administracija/obrisi_vozilo/(?P<vozilo_id>[0-9]+)/$', views.vozilo_delete, name='vozilo-delete'),
    url(r'^administracija/biranje_meseca/$', views.biranje_meseca, name='biranje_meseca'),
    url(r'^administracija/biranje_meseca_finansije/$', views.biranje_meseca_za_finansije, name='biranje_meseca_finansije'),
    url(r'^administracija/dodaj_dane/(?P<mesec>[0-9]+)/(?P<godina>[0-9]+)/(?P<posao_id>[a-zA-Z0-9_.-]+)$', views.dodaj_dane, name='dodaj_dane'),
    url(r'^administracija/pdf/(?P<posao_id>[0-9]+)$', views.pdf_posao, name='pdf_posao'),
    url(r'^administracija/pdf_radnik/(?P<radnik_id>[0-9]+)$', views.pdf_radnik, name='pdf_radnik'),
    url(r'^administracija/pdf_radnici_mesecni_izvestaj/(?P<mesec>[0-9]+)/(?P<godina>[0-9]+)/(?P<posao_id>[a-zA-Z0-9_.-]+)$', views.pdf_radnici_mesecni_izvestaj, name='pdf_radnici_mesecni_izvestaj'),
    url(r'^administracija/pdf_posao_mesecni_izvestaj/(?P<posao_id>[0-9]+)/(?P<mesec>[0-9]+)/(?P<godina>[0-9]+)/$', views.pdf_posao_mesecni_presek, name='pdf_posao_mesecni')
]
