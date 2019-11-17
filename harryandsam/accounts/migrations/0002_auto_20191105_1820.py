# Generated by Django 2.2.6 on 2019-11-05 05:20

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accounts',
            options={'verbose_name_plural': 'Accounts'},
        ),
        migrations.AlterField(
            model_name='accounts',
            name='last_login',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='sprc',
            field=models.CharField(max_length=120, verbose_name='Address 2'),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='waiver',
            field=models.BooleanField(default=False, verbose_name='I agree'),
        ),
    ]
