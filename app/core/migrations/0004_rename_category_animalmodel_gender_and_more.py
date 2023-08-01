# Generated by Django 4.1.2 on 2023-08-01 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_animalmodel_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animalmodel',
            old_name='category',
            new_name='gender',
        ),
        migrations.AddField(
            model_name='animalmodel',
            name='vaccinated',
            field=models.CharField(choices=[('NOT VACCINATED', 'Not Vaccinated'), ('VACCINATED', 'Vaccinated')], default='MALE', max_length=15),
            preserve_default=False,
        ),
    ]
