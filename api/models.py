# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import uuid
from django.db import models
from django.db.models.functions import Concat
from pgvector.django import VectorField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    testerino_fielderino = models.BooleanField(default=False)
    sto_ti_cinis = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return self.username


class Game(models.Model):
    id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.short_name

    class Meta:
        db_table = 'games'

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


class SetupData(models.Model):
    id = models.BigAutoField(primary_key=True)
    data = models.JSONField()
    notes = models.TextField(default='', blank=True, null=True)

    class Meta:
        db_table = 'setup_data'


class Car(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.TextField()
    games = models.ManyToManyField(Game)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    full_name = models.GeneratedField(
        expression=Concat(models.F("brand"), models.Value(" "), models.F("model")),
        output_field=models.TextField(),
        db_persist=True
    )

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'cars'

class Track(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    games = models.ManyToManyField(Game)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tracks'

class Setup(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    game = models.ForeignKey('Game', on_delete=models.DO_NOTHING)
    car = models.ForeignKey('Car', on_delete=models.DO_NOTHING)
    track = models.ForeignKey('Track', on_delete=models.DO_NOTHING)
    description = models.TextField()
    setup_data = models.OneToOneField('SetupData', on_delete=models.DO_NOTHING)
    video_url = models.CharField(max_length=255, blank=True, null=True)
    rating = models.IntegerField()
    rating_count = models.IntegerField()
    downloads_count = models.IntegerField()

    class Meta:
        db_table = 'setups'