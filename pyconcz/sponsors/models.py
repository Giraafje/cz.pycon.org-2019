from django.db import models

from extended_choices import Choices

from django.utils.text import slugify


class Sponsor(models.Model):
    LEVELS = Choices(
        ('platinum', 1, 'Platinum'),
        ('gold', 2, 'Gold'),
        ('silver', 3, 'Silver'),
        ('bronze', 4, 'Bronze'),
        ('diversity', 5, 'Diversity'),
        ('media', 6, 'Media'),
        ('partners', 7, 'Partners'),
        ('connectivity', 9, 'Con­nectiv­ity'),
    )

    level = models.PositiveSmallIntegerField(choices=LEVELS, default=LEVELS.silver)

    name = models.CharField(max_length=200, unique=True)
    logo = models.FileField(
        null=True, blank=True,
        upload_to='sponsors/pyconcz/',
        help_text='should be SVG'
    )

    description = models.TextField(null=True, blank=True, help_text='Markdown formatted')
    link_url = models.URLField()
    twitter = models.URLField(null=True, blank=True, help_text='full URL')
    facebook = models.URLField(null=True, blank=True, help_text='full URL')

    published = models.BooleanField(default=False)

    class Meta:
        ordering = ['level', 'name']

    def __str__(self):
        return self.name

    @property
    def slug(self):
        return slugify(self.name)
