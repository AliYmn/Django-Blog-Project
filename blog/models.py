# -*- coding: utf-8 -*-
from django.db import models
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from ckeditor.fields import RichTextField

class IpController(models.Model):
    remote = models.CharField(max_length=100)
    http_x =  models.CharField(max_length=1000)
    http_user = models.CharField(max_length=1000)
    url = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Ip Kontrol"
        ordering = ('remote',)

    def __str__(self):
        return '{}'.format("Ziyaret Edilen Url : {}".format(self.url))


class Category(MPTTModel):
    # Kategori adı
    title = models.CharField(max_length=500,
                             null=True,unique=True,verbose_name="Kategori Adı",
                             help_text="Kategori adını belirleyin.")
    # Kategori keywords
    tags = models.CharField(max_length=500,null=True,
                            verbose_name="Anahtar Kelimeler",
                            help_text="virgül (,) ile ayırarak belirtin.")
    # Kategori açıklama
    description = models.CharField(max_length=500,null=True,
                                   verbose_name="Açıklama",
                                   help_text="Kategori hakkında kısa açıklama belirtin.")

    # Kategori fa-fa icon
    icon = models.CharField(max_length=100,null=True,
                            help_text='fa fa-bookmark',verbose_name="Icon")

    #Alt kategori :
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children', db_index=True,
                            verbose_name="Alt Kategori",
                            help_text="Alt kategori belirleyebilirsiniz.")

    # Kategori slug url oluşturma.
    url = models.CharField(max_length=500,null=True, blank=True)
    #Öne çıkan görsel
    image =  ProcessedImageField(upload_to='uploads/category/',options={'quality': 30},blank=True)

    class Meta:
        verbose_name_plural = "Kategoriler"
        ordering = ('title',)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        #dönüş değeri
        return self.title

    def get_absolute_url(self):
        return "/kategori/{}".format(self.url)

    def save(self, *args, **kwargs):
        self.url = slugify(self.title.lower(), allow_unicode=True)
        super(Category, self).save(*args, **kwargs)

class Post(models.Model):
    #Makale başlığı
    title = models.CharField(max_length=500, null=True, unique=True,
                             verbose_name="Başlık",help_text="makale başlığı")
    #İçerik tarihi
    time = models.DateTimeField(auto_now=False, null=True,
                                verbose_name="Zaman",help_text="İçerik zamanı")
    #İçerik
    content = RichTextUploadingField(verbose_name="İçerik",help_text="İçeriğiniz")
    #açıklama
    description = models.TextField(null=True,verbose_name="Açıklama",help_text="description")
    #öne çıkan görsel
    image = ProcessedImageField(upload_to='uploads/blog/',
                                           processors=[ResizeToFill(800, 400)],
                                           format='JPEG',
                                           options={'quality': 60},verbose_name="Öne Çıkan Görsel",
                                            help_text="Öne çıkan görseli oluşturur.")
    #kategoriler
    category_list = models.ForeignKey(Category, null=True, blank=True,
                                   db_index=True,verbose_name="Kategoriler")
    #url
    url = models.CharField(max_length=500, null=True, blank=True)
    #yayınlama durumu
    is_active = models.BooleanField(default=False,verbose_name="Yayınla",
                                    help_text="Aktif olursa makale yayınlanır.")
    #hit
    site_hit = models.IntegerField(default=0,verbose_name="Site Hit",help_text="Site görüntülenme sayısıdır.")
    #Ip Kontrol
    ip = models.ForeignKey(IpController, null=True, blank=True,
                                   db_index=True,verbose_name="Ip Kontrol")
    class Meta:
        verbose_name_plural = "Makale Yaz"
        ordering = ('title',)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return "/{}".format(self.url)




    def save(self, *args, **kwargs):
        self.url = slugify(self.title,allow_unicode=True)
        super(Post, self).save(*args, **kwargs)

class SiteInfo(models.Model):
    #Site adı
    title = models.CharField(max_length=100, null=True,
                             verbose_name="Başlık",help_text="Site başlığı")
    #Site Sloganı
    slogan = models.CharField(max_length=100, null=True,
                             verbose_name="Slogan", help_text="Site slogan")

    #Site Yazarı
    author = models.CharField(max_length=100, null=True,
                             verbose_name="Yazar",help_text="Yazar adı")

    #Site Keywords
    tags = models.CharField(max_length=200, null=True,
                             verbose_name="Anahatar Kelime",help_text="(,) virgül ile ayırarak yazınız.")

    #Site açıklama
    description = models.TextField(null=True, unique=True,
                             verbose_name="Açıklama",help_text="Site açıklama")

    #Kısa biyoğrafi
    bio_short = RichTextField(null=True, unique=True,
                             verbose_name="Kısa Bio",help_text="Kısa biyografi yazın.")
    #Uzun biyoğgrafi
    bio_long = RichTextField(null=True, unique=True,
                             verbose_name="Uzun Bio",help_text="Uzun biyografi yazın.")
    #Ana Sayfa
    bio_index = RichTextField(null=True, unique=True,
                             verbose_name="İndex Bio",help_text="Ana Sayfa için kısa biyografi yazın.")

    #site default resim
    image = ProcessedImageField(upload_to='uploads/blog/',
                                           format='JPEG',
                                           processors=[ResizeToFill(870, 382)],
                                           options={'quality': 60},verbose_name="Default Resim",
                                            help_text="Büyük resim yükleyin.")

    facebook = models.CharField(max_length=100, null=True,
                             verbose_name="Facebook",help_text="Facebook")
    twitter = models.CharField(max_length=100, null=True,
                             verbose_name="twitter",help_text="twitter")
    github = models.CharField(max_length=100, null=True,
                             verbose_name="github",help_text="github")
    email = models.CharField(max_length=100, null=True,
                             verbose_name="e-mail",help_text="e-mail")

    class Meta:
        verbose_name_plural = "Site Bilgileri"
        ordering = ('title',)

    def __str__(self):
        return '{}'.format(self.title)

class Love(models.Model):
    #glyhicon icon
    icon = models.CharField(max_length=50, null=True,
                             verbose_name="Icon",help_text="Glyphicon Icon")
    #Açıklama
    description = RichTextField(null=True,verbose_name="Açıklama",help_text="Kısa Açıklama Yapınız.")

    class Meta:
        verbose_name_plural = "Sevdiklerim"
        ordering = ('description',)

    def __str__(self):
        return '{}'.format(self.icon)

class Skills(models.Model):
    #title
    title = models.CharField(max_length=100, null=True,verbose_name="Yetenek",help_text="Yetenek Adı")
    #Oran
    rate = models.CharField(max_length=25, null=True,verbose_name="Oran",help_text="Yetenek Oranı : 1-100")

    class Meta:
        verbose_name_plural = "Yeteneklerim"
        ordering = ('rate',)

    def __str__(self):
        return '{}'.format(self.title)

class Tags(models.Model):
    tags = models.CharField(max_length=500,
                             null=True,verbose_name="Etiket",
                             help_text="(,) ile ayırın.")

    blog = models.ForeignKey(Post)

    class Meta:
        verbose_name_plural = "Etiketler"
        ordering = ('tags',)



    def get_absolute_url(self):
        return "/etiket/{}".format(self.tags)

    def save(self, *args, **kwargs):
        self.tags = slugify(self.tags.lower(), allow_unicode=True)
        super(Tags, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.tags)