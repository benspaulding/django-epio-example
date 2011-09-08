import os

from django.db import models
from django.utils.translation import ugettext_lazy as _


# Models.

class Thing(models.Model):
    """"""

    name = models.CharField(_(u'name'), max_length=255, unique=True)
    slug = models.SlugField(_(u'slug'), unique=True)
    image = models.ImageField(_(u'image'), upload_to='images/things/', blank=True)
    description = models.TextField(_(u'description'), blank=True)

    created = models.DateTimeField(_(u'date created'), auto_now_add=True)
    modified = models.DateTimeField(_(u'last modified'), auto_now=True)

    class Meta:
        get_latest_by = 'created'
        ordering = ('name', )
        verbose_name = _(u'thing')
        verbose_name_plural = _(u'things')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('things-thing-detail', (), {'slug': self.slug })
