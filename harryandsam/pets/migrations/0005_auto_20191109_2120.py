# Generated by Django 2.2.6 on 2019-11-09 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_auto_20191109_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_type',
            field=models.CharField(choices=[('Dog', 'Dog'), ('Cat', 'Cat')], max_length=10),
        ),
    ]
