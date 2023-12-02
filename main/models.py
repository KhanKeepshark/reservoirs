from django.db import models

# Create your models here.
class Reservoirs(models.Model):

    CHOICE_CATEGORY = (
        ('водохранилище', 'водохранилище'),
        ('реки', 'реки'),
        ('озера', 'озера'), 
        ('хвостохранилище', 'хвостохранилище'),
    )

    title = models.CharField("Название", max_length=50)
    category = models.CharField("Категория", choices=CHOICE_CATEGORY, max_length=50, null=True)

    def __str__(self):
        return self.title 

class TextFile(models.Model):
    file = models.FileField(upload_to='txt_files/')  
    uploaded_at = models.DateTimeField(auto_now_add=True)
    reservoir = models.OneToOneField(Reservoirs, on_delete = models.SET_NULL, null = True, blank=True)

    def __str__(self):
        return self.file.name 

# class ExcelFile(models.Model):
#     file = models.FileField(upload_to='excel_files/') 
#     uploaded_at = models.DateTimeField(auto_now_add=True)  
#     reservoir = models.OneToOneField(Reservoirs, on_delete = models.SET_NULL, null = True, blank=True)

#     def __str__(self):
#         return self.file.name 

class ChemistryData(models.Model):
    Dry_residue = models.DecimalField("Dry residue", max_digits=10, decimal_places=2)
    Mineralization = models.DecimalField("Mineralization", max_digits=10, decimal_places=2)
    sum_of_cations = models.DecimalField("Sum of cations", max_digits=10, decimal_places=2)
    iron = models.DecimalField("Iron", max_digits=10, decimal_places=2)
    sodium_and_potassium = models.DecimalField("Sodium and Potassium", max_digits=10, decimal_places=2)
    magnesium = models.DecimalField("Magnesium", max_digits=10, decimal_places=2)
    calcium = models.DecimalField("Calcium", max_digits=10, decimal_places=2)
    anionsum = models.DecimalField("Anionsum", max_digits=10, decimal_places=2)
    nitrates = models.DecimalField("Nitrates", max_digits=10, decimal_places=2)
    sulfates = models.DecimalField("Sulfates", max_digits=10, decimal_places=2)
    chlorides = models.DecimalField("Chlorides", max_digits=10, decimal_places=2)
    bicarbonates = models.DecimalField("Bicarbonates", max_digits=10, decimal_places=2)
    carbonates = models.DecimalField("Carbonates", max_digits=10, decimal_places=2)
    uploaded_at = models.DateField()
    reservoir = models.ForeignKey(Reservoirs, on_delete=models.SET_NULL, null = True)
