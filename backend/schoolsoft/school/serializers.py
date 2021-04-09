from rest_framework import serializers
from .models import Eleve, Professeur, Classe, Moyenne, Matiere

class EleveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eleve
        fields = ('first_name', 'last_name' , 'num_mat', 'gender', 'created', 'is_actif',
                    'dob', 'phone', 'is_actif')

class ProfesseurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Professeur
        fields = ('first_name', 'last_name' , 'gender', 'status', 'created', 'date_debut', 'date_depart', 'is_stranger')

class ClasseSerializer(serializers.HyperlinkedModelSerializer):
    professeurs = ProfesseurSerializer(many = True, required = False)
    class Meta:
        model = Classe
        #fields = ('cnum','cname', 'sections', 'professeurs')
        fields = ('cnum','cname', 'professeurs')

class MatiereSerializer(serializers.HyperlinkedModelSerializer):
    professeurs = ProfesseurSerializer(many = True, required = False)
    classes = ClasseSerializer(many = True, required = False)
    class Meta:
        model = Matiere
        fields = ('cname', 'cdesc', 'classes', 'professeurs')

class MoyenneSerializer(serializers.HyperlinkedModelSerializer):
    eleves = EleveSerializer(many = True, required = False)
    matieres = MatiereSerializer(many = True, required = False)
    class Meta:
        model = Moyenne
        fields = ('eleves', 'matieres', 'term', 'coef', 'note1', 'note2', 'note3', 'note_compo')
        