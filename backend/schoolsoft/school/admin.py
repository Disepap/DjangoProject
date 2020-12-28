from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Section, Classe, Matiere, Professeur, Eleve, Annee, Moyenne, Inscription, Salle
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
import django.utils.timezone as timezone
#from django.contrib import messages

admin.site.unregister(User)
admin.site.unregister(Group)

####Import Export section####
class EleveResource(resources.ModelResource):

    class Meta:
        model = Eleve
        skip_unchanged = True
        #fields = ('first_name', 'last_name', 'classes__cnum', )

####Adim ops section####
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['sname','sdesc', 'view_classes_link']
    list_filter = ('sname', 'sdesc')
    search_fields = ('sname', 'sdesc')
    fields = (('sname', 'sdesc'), )

    def view_classes_link(self, obj):
        count = obj.classes_sections.count()
        url = (
            reverse("admin:school_classe_changelist")
            + "?"
            + urlencode({"sections__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Classes</a>', url, count)

    view_classes_link.short_description = "Classes"

@admin.register(Professeur)
class ProfesseurAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['first_name', 'last_name' , 'gender', 'status', 'created', 'date_debut', 'date_depart', 'is_stranger']
    list_filter = ('gender', 'status', 'is_stranger')
    search_fields = ('first_name', 'last_name')
    readonly_fields = ['photo_image']
    def photo_image(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(url = obj.photo.url, width = 120, height =120,))
    
    fields = (('photo_image', 'photo'), ('first_name', 'last_name',), ('gender', 'status'), ('dob', 'phone'), ('date_debut', 'date_depart'),'is_stranger') #to order and organize fields

@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['cnum','cname', 'sections', 'view_eleves_link', 'view_professeurs_link']
    list_filter = ('cnum', 'sections')
    search_fields = ('cnum', 'sections', 'professeurs')
    fields = (('cnum', 'cname'), 'sections', 'professeurs')

    def view_eleves_link(self, obj):
        anne_cur = Annee.objects.get(is_actif = True)
        inscrip = Inscription.objects.filter(classe__id = obj.id, annee_scolaire__id = anne_cur.id)
        #count = obj.eleves.count()
        count = Inscription.objects.filter(classe__id = obj.id, annee_scolaire__id = anne_cur.id).count()
        
        url = (
            reverse("admin:school_eleve_changelist")
            + "?"
            + urlencode({"classe__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Élève(s)</a>', url, count)

    view_eleves_link.short_description = "Élèves"

    def view_professeurs_link(self, obj):
        count = obj.professeurs.count()
        url = (
            reverse("admin:school_professeur_changelist")
            + "?"
            + urlencode({"classe__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Professeur(s)</a>', url, count)

    view_professeurs_link.short_description = "Professeurs"
    

@admin.register(Annee)
class AnneeAdmin(admin.ModelAdmin):
    list_display = ['fromYear','toYear', 'is_actif']
    list_filter = ('fromYear', 'toYear', 'is_actif')
    fields = (('fromYear', 'toYear'), 'is_actif')
    def save_model(self, request, obj, form, change):
        if obj.is_actif is True:
            if (obj.fromYear >= timezone.now().year and obj.toYear <= timezone.now().year + 1):
                #Annee.objects.update(is_actif=True)
                obj.is_actif = True
            else:
                obj.is_actif = False
                #messages.error(request,'Error message')
        super().save_model(request, obj, form, change)

@admin.register(Moyenne)
class MoyenneAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['eleve','matiere', 'get_classe', 'get_AnneSc', 'term', 'coef', 'note1', 'note2', 'note3', 'get_Note_classe', 'note_compo']
    list_filter = ('eleve', 'matiere', 'term')
    fields = (('eleve', 'matiere'), ('term', 'coef'), ('note1', 'note2', 'note3', 'note_compo'))
    #raw_id_fields = ["eleve"]
    def get_classe(self, obj):
        insc = Inscription.objects.filter(eleve__id = obj.eleve.id)
        if(len(insc) > 0):
            return insc[0].classe
        else:
            return ''
    get_classe.short_description = "Classe"

    def get_AnneSc(self, obj):
        insc = Inscription.objects.filter(eleve__id = obj.eleve.id)
        if(len(insc) > 0):
            return insc[0].annee_scolaire
        else:
            return ''
    get_AnneSc.short_description = "Année scolaire"

    def get_Note_classe(self, obj):
        if (obj.note1 != None and obj.note2 != None and obj.note3 != None):
            return round((obj.note1 + obj.note2 + obj.note3)/3, 2)
        elif (obj.note1 != None and obj.note2 != None):
            return round((obj.note1 + obj.note2)/2, 2)
        else:
            return obj.note1

    get_Note_classe.short_description = "Note de classe"

@admin.register(Matiere)
class MatiereAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['cname', 'cdesc', 'view_professeurs_link', 'view_classes_link']
    list_filter = ('cname',)
    search_fields = ('cname', 'cdesc')
    fields = (('cname', 'cdesc'), 'classes', 'professeurs')

    def view_professeurs_link(self, obj):
        count = obj.professeurs.count()
        url = (
            reverse("admin:school_professeur_changelist")
            + "?"
            + urlencode({"matiere__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Professeur(s)</a>', url, count)

    view_professeurs_link.short_description = "Dispensé par"

    def view_classes_link(self, obj):
        count = obj.classes.count()
        url = (
            reverse("admin:school_classe_changelist")
            + "?"
            + urlencode({"matiere__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Classe(s)</a>', url, count)

    view_classes_link.short_description = "Dispensé dans"

@admin.register(Eleve)
class EleveAdmin(admin.ModelAdmin):
#class EleveAdmin(ImportExportModelAdmin):
    #resource_class = EleveResource
    list_per_page = 15
    readonly_fields = ['photo_image']
    def photo_image(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(url = obj.photo.url, width = 120, height =120,))
    list_display = ['first_name', 'last_name' , 'num_mat', 'gender', 'created', 'get_classe', 'is_actif']
    list_filter = ('gender', 'is_actif')
    search_fields = ('first_name', 'last_name', 'num_mat')
    fields = (('photo_image', 'photo'), ('first_name', 'last_name',),'num_mat','gender', ('dob', 'phone'),'is_actif') #to order and organize fields
    def get_classe(self, obj):
        if(obj.classe_set.count() > 0):
            return obj.classe_set.all()[0].cnum
        else:
            return ''
    get_classe.short_description = "Classe"

@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['eleve', 'classe' , 'date_inscription', 'annee_scolaire', 'status']
    list_filter = ('classe', 'annee_scolaire', 'status')
    search_fields = ('classe', 'annee_scolaire', 'eleve')
    fields = (('eleve', 'classe') ,'date_inscription', ('annee_scolaire', 'status'))
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "annee_scolaire":
            kwargs["queryset"] = Annee.objects.filter(is_actif__in=[True])
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Salle)
class SalleAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['sname', 'classe' , 'cap_ac', 'cap_acmax']
    fields = ('sname', 'classe' , ('cap_ac', 'cap_acmax'))

####Site Header+Title####
admin.site.site_header = 'L.P.KA.BA.T'
admin.site.site_title = 'L.P.KA.BA.T'
admin.site.index_title = 'Portail d\'administration L.P.KA.BA.T'
