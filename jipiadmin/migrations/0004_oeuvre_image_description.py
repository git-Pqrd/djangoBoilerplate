# Generated by Django 2.0 on 2017-12-24 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jipiadmin', '0003_oeuvre'),
    ]

    operations = [
        migrations.AddField(
            model_name='oeuvre',
            name='image_description',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
