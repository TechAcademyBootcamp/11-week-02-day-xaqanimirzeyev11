from django.db import models

SUBJECTS = ((1, 'Dram'), (2, 'Dedektiv'), (3, 'Komediya'))

class Book(models.Model):
    """
    Bu class kitablar table-ni yaradacaq
    """
    # relations

    # informations
    title = models.CharField('Basliq', max_length=50)
    author = models.CharField('Muellif', max_length=50)
    page_count = models.IntegerField('Sehife sayi', default=100)
    price = models.DecimalField('Qiymeti', max_digits=10, decimal_places=2, null=True, blank=True)
    cover = models.ImageField('Uz qabigi', upload_to='book_covers/', null=True, blank=True)
    description = models.TextField('Aciqlama', default="Yaxsi kitabdir!")
    subject = models.IntegerField(choices=SUBJECTS, default=1)
    pdf = models.FileField('PDF', upload_to='book_pdfs/', null=True, blank=True)

    # moderators
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'my_books'
        verbose_name = 'Kitab'
        verbose_name_plural = 'Kitablar'
        ordering = ['price']

    def __str__(self):
        return f"{self.title}  {self.author}nin kitabidir"

GOODS =((1, 'Convenience Goods'), (2, 'Shopping Goods'), (3, 'Specialty Good'))

    
class Product(models.Model):
    
    # relations


    # informations
    name=models.CharField('Mehsul', max_length=125,unique=True)
    description=models.TextField('Aciqlama', default="Yaxsi mehsuldur!", max_length=500)
    category=models.IntegerField(choices=GOODS, default=1)
    picture=models.ImageField('Sekil',upload_to='products/images ', null=True, blank=True)
    amount=models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField('Qiymeti', max_digits=5, decimal_places=2, null=True, blank=True,default=0.00)
    production_date=models.DateTimeField(auto_now_add=True,null=True, blank=True)
    is_new=models.BooleanField(default=0,null=True, blank=True)
    certificate=models.FileField('Sened', upload_to='products/files', null=True, blank=True)
    rating=models.DecimalField("Reytinq", max_digits=1, decimal_places=1, default=0.0)
    detailed_view_link=models.URLField(max_length=300,null=True,blank=True)

    # moderators


    class Meta:
        db_table = 'company_products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"