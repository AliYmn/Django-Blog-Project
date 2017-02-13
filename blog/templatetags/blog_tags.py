from django import template
from blog.models import SiteInfo

title = ""
slogan = ""
author = ""
tags = ""
description = ""
image = ""
bio_short = ""
bio_long = ""
bio_index = ""
facebook = ""
github = ""
twitter = ""
email = ""

for i in SiteInfo.objects.all():
    title = i.title
    slogan = i.slogan
    author = i.author
    tags = i.tags
    description = i.description
    image = i.image.url
    bio_short = i.bio_short
    bio_long = i.bio_long
    bio_index = i.bio_index
    facebook = i.facebook
    github = i.github
    twitter = i.twitter
    email = i.email

# Template Kütüphanesi
register = template.Library()

@register.simple_tag
def site_title():
    return title

@register.simple_tag
def site_slogan():
    return slogan

@register.simple_tag
def site_author():
    return author

@register.simple_tag
def site_description():
    return description

@register.simple_tag
def site_tags():
    return tags

@register.simple_tag
def site_image():
    return image

@register.simple_tag
def site_bio_short():
    return bio_short

@register.simple_tag
def site_bio_long():
    return bio_long

@register.simple_tag
def site_bio_index():
    return bio_index

@register.simple_tag
def site_facebook():
    return facebook

@register.simple_tag
def site_github():
    return github

@register.simple_tag
def site_twitter():
    return twitter

@register.simple_tag
def site_email():
    return email

@register.filter(name='post_tags')
def post_tags(value):
    return str("{},".format(value)).replace("-", " ")

@register.filter(name='tags_list')
def tags_list(value):
    return str("{}".format(value)).replace("-", " ")