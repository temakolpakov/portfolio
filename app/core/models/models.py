import datetime
from enum import Enum
from typing import Optional

from tortoise import fields, Model


class Projects(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    brief_description = fields.TextField()
    description = fields.TextField()
    ordering = fields.IntField(default=0)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "projects"


class Images(Model):
    id = fields.IntField(pk=True)
    project = fields.ForeignKeyField('models.Projects', related_name='images')
    title = fields.BooleanField(default=False)
    path = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    ordering = fields.IntField(default=0)

    class Meta:
        table = "images"


