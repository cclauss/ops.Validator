# coding=utf-8
from __future__ import unicode_literals

from django.db import models

SYSTEMS = (
    ("chef", "chef"),
    ("pupp", "puppet"),
    ("mura", "murano"),
)


class Image(models.Model):
    """
    A docker OS image identified by OS name and version
    """
    name = models.CharField(max_length=50, blank=False, default='Unknown')
    version = models.CharField(max_length=50, blank=False, default='Unknown')
    dockerfile = models.CharField(max_length=255, blank=False, default='Unknown')
    system = models.CharField(max_length=4, choices=SYSTEMS, default="chef")

    def __unicode__(self):
        return "%s:%s" % (self.name, self.version)


class Repo(models.Model):
    """
    A repository identified by type and location (url or filepath)
    """
    REPOS = (
        ("svn", "svn"),
        ("git", "git"),
        ("tgz", "tgz"),
        ("zip", "zip"),
    )
    location = models.CharField(max_length=255, blank=False, default='Unknown')
    type = models.CharField(max_length=3, choices=REPOS, default="svn")
    user = models.CharField(max_length=255, blank=False, default='Unknown')
    password = models.CharField(max_length=255, blank=False, default='Unknown')

    def __unicode__(self):
        return self.location


class CookBook(models.Model):
    """
    A collection of cookbooks belonging to a repo, identified by name and version
    """
    name = models.CharField(max_length=50, blank=False, default='Unknown')
    version = models.CharField(max_length=50, blank=False, default='Unknown')
    repo = models.ForeignKey(Repo, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Recipe(models.Model):
    """
    A recipe belonging to a given cookbook, identified by name
    """
    name = models.CharField(max_length=50, blank=False, default='Unknown')
    cookbook = models.ForeignKey(CookBook, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Deployment(models.Model):
    """
    The deployment of a recipe in a system image
    """
    recipe = models.ForeignKey(Recipe, blank=True, null=True)
    image = models.ForeignKey(Image, blank=True, null=True)
    ok = models.BooleanField(default=False)
    description = models.TextField()
