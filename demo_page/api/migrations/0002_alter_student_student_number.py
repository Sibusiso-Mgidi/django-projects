# Generated by Django 3.2 on 2021-04-08 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_number',
            field=models.CharField(max_length=20),
        ),
    ]
