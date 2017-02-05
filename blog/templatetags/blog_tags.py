from django import template
from blog.models import SiteInfo

title = ""
slogan = ""
author = ""
tags = ""
description = ""
image = ""

for i in SiteInfo.objects.all():
    title = i.title
    slogan = i.slogan
    author = i.author
    tags = i.tags
    description = i.description
    image = i.image.url

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
