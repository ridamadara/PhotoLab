# Generated by Django 4.0 on 2022-01-02 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoLab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='contact',
            field=models.CharField(max_length=11),
        ),
    ]
