from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

###
# Abstract Base models.
###

class TimestampModel(models.Model):
    """A short mixin abstract class for adding 
    update and creation timestamp fields.
    """
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now_add=True)

    class Meta:
        abstract = True


class ActiveModel(models.Model):
    """A mixin abstract class to provide functionality
    for marking specific rows as active or inactive.
    """
    is_active = models.BooleanField(_('is active?'), default=True)

    class Meta:
        abstract = True

###
# Core models.
###

class Category(models.Model):
    """Allows simple categorisation of the boards, 
    whether that be by client, location, whatever.
    """
    title = models.CharField(_('title'), max_length=100, unique=True)
    slug = models.SlugField(_('slug'), max_length=100, unique=True, 
                            editable=False)
    tagline = models.CharField(_('tagline'), max_length=255, blank=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('kanban_board_list', [self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Board(TimestampModel, ActiveModel):
    """This models represents a single kanban
    chart and all of its attributes.
    """
    #TODO: editing permissions, needs groups and users.
    creator = models.ForeignKey('auth.User', verbose_name=_('creator'),
                                related_name='boards')
    category = models.ForeignKey('kanban.Category', verbose_name=_('category'),
                                related_name='boards', null=True, blank=True)
    title = models.CharField(_('title'), max_length=100, unique=True)
    slug = models.SlugField(_('slug'), max_length=100, unique=True, 
                            editable=False)
    tagline = models.CharField(_('tagline'), max_length=255, blank=True)
    description = models.TextField(_('description'), blank=True)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('kanban_board_detail', [self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Board, self).save(*args, **kwargs)


class State(models.Model):
    """Represents a 'Kanban state', will equate to one 
    customisable column in the chart. Allows us to have
    boards which do different tasks.
    """
    #TODO: editing permissions, needs groups and users.
    board = models.ForeignKey('kanban.Board', verbose_name=_('board'), 
                              related_name='states')
    title = models.CharField(_('title'), max_length=100, unique=True)
    slug = models.SlugField(_('slug'), max_length=100, unique=True)
    tagline = models.CharField(_('tagline'), max_length=255, blank=True)
    order = models.PositiveIntegerField(_('order'))

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(State, self).save(*args, **kwargs)


class Card(models.Model):
    """Represents a 'kanban card', kanban cards sit
    in a given state on a given board and model a single task.
    """
    state = models.ForeignKey('kanban.State', verbose_name=_('state'), 
                              related_name='cards')
    order = models.PositiveIntegerField(_('order'))
    summary = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.summary
