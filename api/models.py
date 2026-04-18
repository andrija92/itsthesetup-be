# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import uuid
from django.db import models
from pgvector.django import VectorField
from django.contrib.auth.models import AbstractUser

class Embeddings(models.Model):
    id = models.BigAutoField(primary_key=True)
    embedding = VectorField(dimensions=1536)
    content = models.CharField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'embeddings'


class RefreshTokens(models.Model):
    id = models.UUIDField(primary_key=True)
    token = models.CharField()
    created_at = models.DateTimeField()
    expires_at = models.DateTimeField()

    class Meta:
        db_table = 'refresh_tokens'


class Setups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'setups'


class Test(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'test'


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    testerino_fielderino = models.BooleanField(default=False)
    sto_ti_cinis = models.TextField(default='', blank=True, null=True)
    
