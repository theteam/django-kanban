from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

###
# Abstract Base classes
###

class TimestampModel(models.Model):
    """
    A short mixin abstract class for adding 
    update and creation timestamp fields.
    """
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class ActiveModel(models.Model):
    """
    A mixin abstract class to provide functionality
    for marking specific rows as active or inactive and
    creating the relevant managers to allow for simple
    use via the ORM.
    """
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
