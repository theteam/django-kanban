from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

###
# Abstract Base classes
###

class TimestampModel(models.Model):
    """A short mixin abstract class for adding 
    update and creation timestamp fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class ActiveModel(models.Model):
    """A mixin abstract class to provide functionality
    for marking specific rows as active or inactive.
    """
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(models.Model):
    """Allows simple categorisation of the boards, 
    whether that be by client, location, whatever.
    """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('kanban_category', [self.slug])


class Board(TimestampModel, ActiveModel):
    """This models represents a single kanban
    chart and all of its attributes.
    """
    #TODO: editing permissions, needs groups and users.
    creator = models.ForeignKey('auth.User', related_name='boards')
    category = models.ForeignKey('kanban.Category', related_name='boards')
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    tagline = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('kanban_board', [self.category.slug, self.slug])


class State(models.Model):
    """Represents a 'Kanban state', will equate to one 
    customisable column in the chart. Allows us to have
    boards which do different tasks.
    """
    #TODO: editing permissions, needs groups and users.
    board = models.ForeignKey('kanban.Board', related_name='columns')
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    tagline = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.title

class Card(models.Model):
    """Represents a 'kanban card', kanban cards sit
    in a given state on a given board and model a single task.
    """
    state = models.ForeignKey('kanban.State', related_name='cards')
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
