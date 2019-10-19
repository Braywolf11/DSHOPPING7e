from django.db import models
from ckeditor.fields import RichTextField
# class web(main):
#     about_us = models.TextField("about_us")
#     phone =
#     email =
#     address =
#     class   Meta:
#         verbose_name:
#         verbose_name_plural =
#     def __str__(self):
#         return about_us

# Create your models here.
class main(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField('Status',default=True)  
    class Meta:
        abstract = True

class categories(main):
    descripcion = models.CharField('Descripcion', max_length=100, unique=True)
    title = models.CharField('Title', max_length=100, unique=True)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.descripcion

class gender(main):
    title = models.CharField('Title', max_length=100, unique=True)
    descripcion = models.CharField('Descripcion', max_length=100)    
    class Meta:
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'
    def __str__(self):
        return self.title

class country(main):
    title = models.CharField('Title', max_length=100, unique=True)
    addreviatons= models.CharField('Addreviatons', max_length=100)    
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
    def __str__(self):
        return self.title

class clients(main):
    first_name = models.CharField('First name ', max_length=100)
    last_name = models.CharField('Last name ', max_length=100)
    email = models.EmailField('E-mail', max_length=50)
    photo = models.ImageField('Author image', null= True, blank=True, upload_to='clients/')
    id_gender = models.ForeignKey(gender, on_delete=models.CASCADE)
    id_cuntry = models.ForeignKey(country, on_delete=models.CASCADE)
    phone= models.CharField('Phone', max_length=11)
    password = models.CharField('Password', max_length=50)
    credit_card_number = models.CharField('Credit_card_number', max_length=50)
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    def __str__(self):
        return '{0}{1}{2}'.format(self.first_name," ",self.last_name)

class product(main):
    title = models.CharField('Title', max_length=100, unique=True)
    descripcion = models.CharField('Descripcion', max_length=100) 
    id_category = models.ForeignKey(categories, on_delete=models.CASCADE)
    id_country = models.ForeignKey(clients, on_delete=models.CASCADE) 
    photo = models.ImageField('Author image', null= True, blank=True, upload_to='clients/')
    quality = models.CharField('Quality', max_length=100)
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    def __str__(self):
        return self.title

class shopping(models.Model):
    id_products = models.ForeignKey(product, on_delete=models.CASCADE)
    id_client = models.ForeignKey(clients, on_delete=models.CASCADE)
    shopping_date = models.DateField('Shopping_date', auto_now=True, auto_now_add=False)
    class Meta:
        verbose_name = 'Shopping'
        verbose_name_plural = 'Shoppings'
    def __str__(self):
        return self.shopping_date

