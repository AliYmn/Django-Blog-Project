# Versiyon Uyumlulukları

* Python 3.x +
* Django 1.9 +

# Demo

* <a href="http://aliyaman.org">Ali Yaman | Kişisel Blog</a>

# Settings.py 
Settings.py üzerinden resim sıkıştırma ayarı, disquss ve küçük resim boyutu ayarları bulunmaktadır.

    # ----------------Ayarlar------------------------ #
    #Resim sıkıştırma oranı %60 ideaildir.
    IMAGE_QUALITY = 60
    # Küçük resim boyutu, bu tema için idealdir.
    THUMBNAIL_SIZE=(300,300)
    
    #Disquss üzerinden api ke almanız gerekiyor.
    DISQUS_API_KEY = 'ApiKey'
    #Disquss üzerinden aldığınız subdomain adını yazın.
    DISQUS_WEBSITE_SHORTNAME = 'aliyaman'
    
    #Sıte ID, admin panelden SİTELER bölümden bilgileri değişin.
    SITE_ID = 1
    # ----------------Ayarlar------------------------ #
    


# Site Ayarları

Site üzerinden tüm özellikler admin panelden özelleştirilme özelliğine sahiptir.

* Etiketler : İçerik etiketlerini tutar.
* Kategori : İçerik kategorileridir. Alt kategori oluşturma özelliği mevcuttur.
* Makale Yaz : İçerik yazabilceğiniz alandır.
* Sevdiklerim : Hakkımda sayfasında bulunan, iconlu açıklamalardır.
* Site Bilgileri : Site'nin genel ayarlarını bulundurur.
* Yeteneklerim : Hakkımda sayfasında bulunan, yetenekleri bulundurur.

<a href="http://aliyaman.org"><img src="http://image.prntscr.com/image/a0731d6c2ae0449b808033475f715ece.png" alt="Kişisel Blog"></a>

# Kategori
Basit şekilde, kategori eklemenizi sağlar.

# İçerik Ekleme
Ckeditör sayesinde rahatlıkla içeriklerinizi oluşturalabilirsiniz.
<a href="http://aliyaman.org"><img src="http://image.prntscr.com/image/eb2ef637ae9e438fa244e2c35238e27d.png" alt="Kişisel Blog"></a>

* Site Hit : Sitenin görüntülenme değerlerini tutar.
<a href="http://aliyaman.org"><img src="http://image.prntscr.com/image/47aa96ade52246ed9852d2d7bc52892e.png" alt="Kişisel Blog"></a>

# Sevdiklerim
Hakkımızda adlı sayfa için iconlu açıklamaları bulundurur.
<a href="http://aliyaman.org"><img src="http://image.prntscr.com/image/abe3b45ff3284f2c90da36bf1fd64482.png" alt="Kişisel Blog"></a>
<a href="http://aliyaman.org"><img src="http://image.prntscr.com/image/60693f8f460845fa9b27122ad82de309.png" alt="Kişisel Blog"></a>

# Site Bilgileri
Site bilgileri üzerinden;

* Başlık
* Slogan
* Açıklama
* Biyografi
* Sosyal medya 
gibi vb. özellikleri ekleyebilirsiniz.

<a href="http://aliyaman.org"><img src="http://image.prntscr.com/image/8e2b663e2bea45d683a69d4afb9757fa.png" alt="Kişisel Blog"></a>

# Yeteneklerim
Hakkımda adlı sayfada yeteneklerinizi yazabilceğiniz alandır.
<a href="http://aliyaman.org"><img src="http://image.prntscr.com/image/3a66844fbf4a4a6e86aa8e772b198c12.png" alt="Kişisel Blog"></a>
<a href="http://aliyaman.org"><img src="http://image.prntscr.com/image/26145f7f02cc42fc853ac5866c5454c8.png" alt="Kişisel Blog"></a>

# SiteMaps

* Kategori    : /sitemap_post.xml
* Yazılar     : /sitemap_category
* Etiket      : /sitemap_tags
 
olmak üzere üç adet sitemaps bulunur.

# Robots.txt

Robots.txt ulaşmak için;
* /robots.txt yazabilirsiniz.

# Kurulum

Tavsiye kurulum : https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04