from django.db import models

"""
- Whenever we create or make changes to a model, we need to tell django o migrate thos changes to the databases.
- The Django ORM then writes all the SQL CREATE_TABLE commands for us.
- Whenever a new model or entity is created/updated we need to tell Django to migrate those changes.
"""
class Hero(models.Model):
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    "The __str__ tell Django what to print when it needs to display an instance of the Hero model."
    def __str__(self):
        return self.name


