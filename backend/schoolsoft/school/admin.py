from django.contrib import admin
from .models import Section, Classe, Matiere, Professeur, Eleve, Annee, Moyenne, Inscription
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html


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
    list_display = ['first_name', 'last_name' , 'gender', 'status', 'created', 'is_stranger']
    list_filter = ('gender', 'status', 'is_stranger')
    search_fields = ('first_name', 'last_name')
    readonly_fields = ['photo_image']
    def photo_image(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(url = obj.photo.url, width = 120, height =120,))
    
    fields = (('photo_image', 'photo'), ('first_name', 'last_name',), ('gender', 'status'), ('dob', 'phone'),'is_stranger') #to order and organize fields

@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['cnum','cname', 'sections', 'view_eleves_link', 'view_professeurs_link']
    list_filter = ('cnum', 'sections')
    search_fields = ('cnum', 'sections', 'professeurs')

    def view_eleves_link(self, obj):
        count = obj.eleves.count()
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

@admin.register(Moyenne)
class MoyenneAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['eleve','matiere', 'term', 'coef', 'note1', 'note2', 'note3', 'note_compo']
    list_filter = ('eleve', 'matiere', 'term')
    fields = (('eleve','matiere'), 'term', 'coef', ('note1', 'note2', 'note3', 'note_compo'))
    raw_id_fields = ["eleve"]

@admin.register(Matiere)
class CoursAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['cname', 'cdesc']
    list_filter = ('cname', 'cdesc')
    search_fields = ('cname', 'cdesc')

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
    list_display = ['eleve', 'classe' , 'date_inscription', 'annee_scolaire']
    list_filter = ('classe', 'annee_scolaire')

####Site Header+Title####
admin.site.site_header = 'L.P.KA.BA.T'
admin.site.site_title = 'L.P.KA.BA.T'
admin.site.index_title = 'Portail d\'administration L.P.KA.BA.T'
