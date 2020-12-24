from django.db import models


#Ecole
class Ecole(models.Model):
    enum = models.CharField(max_length = 30)
    ename = models.CharField(max_length = 250)

    class Meta: 
        
        verbose_name_plural = 'École LT'


#Person base class
class Personne(models.Model):
    GENDER = (
        ('h', 'H'),
        ('f', 'F'),
    )
    first_name = models.CharField(max_length = 70, verbose_name ='Prénom')
    last_name = models.CharField(max_length = 70, verbose_name ='Nom')
    dob = models.DateField(verbose_name ='Date de naissance')
    gender = models.CharField(max_length=10, choices=GENDER, default='h', verbose_name ='Genre')
    email = models.EmailField(max_length = 70, blank = True)
    created = models.DateTimeField(auto_now_add=True, verbose_name ='Date de création')
    last_login = models.DateTimeField(auto_now=True)
    adresse = models.CharField(max_length = 250, blank = True)
    phone = models.IntegerField( verbose_name ='Téléphone', null=True, blank = True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    class Meta:
        abstract = True

    def __str__(self):

        return self.first_name + ' ' + self.last_name


#Related section of the class
class Section(models.Model):
    sname = models.CharField(max_length = 70, verbose_name ='Section')
    sdesc = models.CharField(max_length = 100, verbose_name ='Description', blank = True)
    #Ecole

    def __str__(self):
        return self.sname

#Teacher model
class Professeur(Personne):
    STATUS = (
        ('c', 'Contractuel'),
        ('p', 'Permanent'),
    )
    status = models.CharField(max_length=30, choices=STATUS, default='p', verbose_name ='Statut enseignant')
    is_stranger = models.BooleanField(default=False, verbose_name ='Etranger')
    #Date de debut de service
    #date de fin deservice

#Student class
class Eleve(Personne):
    num_mat = models.CharField(max_length = 20, verbose_name ='N° Matricule', blank=True, unique=True, null=True)
    #classes = models.ForeignKey(Classe, on_delete=models.CASCADE, verbose_name ='Classe', related_name='etudiant_classes')
    is_actif = models.BooleanField(default= True, verbose_name ='Est actif')
     
#Classroom model
class Classe(models.Model):
    cnum = models.CharField(max_length = 70, verbose_name ='Classe')
    cname = models.CharField(max_length = 70, verbose_name ='Description', blank = True)
    sections = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='classes_sections')
    professeurs = models.ManyToManyField(Professeur, blank=True )
    eleves = models.ManyToManyField(Eleve, through='Inscription')

    def __str__(self):
        return self.cnum

#Year
class Annee(models.Model):
    fromYear = models.IntegerField(verbose_name = 'De')
    toYear = models.IntegerField(verbose_name = 'A')
    is_actif = models.BooleanField(verbose_name ='Année en cours')

    class Meta:
        verbose_name_plural = "Année Scolaire"
        unique_together = [['fromYear','toYear']]
        
    def __str__(self):
        return str(self.fromYear) + '-' + str(self.toYear)

#Course model
class Matiere(models.Model):
    cname = models.CharField(max_length = 70, verbose_name ='Matière')
    cdesc = models.CharField(max_length = 100, verbose_name ='Description', blank=True)
    classes = models.ManyToManyField(Classe, blank = True)
    professeurs = models.ManyToManyField(Professeur, blank=True)

    def __str__(self):
        return self.cname

#Student Parent model
class Parent(Personne):
    pass

#Note class
class Moyenne(models.Model):
    TERM_STATUS = (
        ('1', '1 er trim'),
        ('2', '2 eme trim'),
        ('3', '3 eme trim'),
    )
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE, related_name='moyenne_professeurs')
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE, related_name='moyenne_eleves')
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name='moyenne_matieres')
    term = models.CharField(max_length=20, choices=TERM_STATUS, default='1')
    coef  = models.DecimalField(max_digits = 5, decimal_places = 2, null=True, blank=True)
    note1 = models.DecimalField(max_digits = 5, decimal_places = 2, null=True, blank=True)
    note2 = models.DecimalField(max_digits = 5, decimal_places = 2, null=True, blank =True)
    note3 = models.DecimalField(max_digits = 5, decimal_places = 2, null=True, blank=True)
    note_compo = models.DecimalField(max_digits = 5, decimal_places = 2, null=True, blank=True)
    #total

    #def __str__(self):
        #return self.etudiant

#Inscription
class Inscription(models.Model):
    ETD_STATUS = (
        ('o', 'Orienttation'),
        ('te', 'Transfert en cours'),
        ('tf', 'Transfert finalisé'),
        ('cl', 'CL'),
    )
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    status =  models.CharField(max_length=30, choices=ETD_STATUS, default='o', verbose_name ='Type d\'inscription')
    date_inscription = models.DateField()
    annee_scolaire = models.ForeignKey(Annee, on_delete = models.CASCADE)

    class Meta:
        unique_together =[['classe','eleve']]

    def __str__(self):
        return Eleve.objects.get(pk = self.eleve.id).first_name





