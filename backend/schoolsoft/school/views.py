from django.shortcuts import render
from django.http import HttpResponse
from .models import Section, Classe, Matiere, Professeur, Eleve, Annee, Moyenne, Inscription, Salle
from school.serializers import EleveSerializer, ProfesseurSerializer, ClasseSerializer, MoyenneSerializer, MatiereSerializer
from rest_framework import viewsets

def index(request):
    print(dir(admin.site))
    return HttpResponse('<h1> hello </h1>')

class EleveViewSet(viewsets.ModelViewSet):
    queryset = Eleve.objects.all()
    serializer_class = EleveSerializer

class ProfesseurViewSet(viewsets.ModelViewSet):
    queryset = Professeur.objects.all()
    serializer_class = ProfesseurSerializer

class ClasseViewSet(viewsets.ModelViewSet):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer

class MatiereViewSet(viewsets.ModelViewSet):
    queryset = Matiere.objects.all()
    serializer_class = MatiereSerializer

class MoyenneViewSet(viewsets.ModelViewSet):
    queryset = Moyenne.objects.all()
    serializer_class = MoyenneSerializer
