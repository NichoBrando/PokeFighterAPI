from djongo import models
import jsonfield

class Pokemons(models.Model):
  Name = models.CharField()
  Number = models.IntegerField()
  Type_1 = models.CharField()
  Type_2 = models.CharField()
  HP = models.IntegerField()
  Attack = models.IntegerField()
  Defense = models.IntegerField()
  Sp = jsonfield.JSONField()
  Speed = models.IntegerField()
  Generation = models.IntegerField()
  Legendary = models.BooleanField()

  class Meta:
    abstract = True

class Combats(models.Model):
  First_pokemon = models.IntegerField()
  Second_pokemon = models.IntegerField()
  Winner = models.IntegerField()

  class Meta:
    abstract = True

class Tests(models.Model):
  First_pokemon = models.IntegerField()
  Second_pokemon = models.IntegerField()

  class Meta:
    abstract = True