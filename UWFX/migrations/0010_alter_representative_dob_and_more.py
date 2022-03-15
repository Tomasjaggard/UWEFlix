# Generated by Django 4.0.3 on 2022-03-15 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UWFX', '0009_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='representative',
            name='dob',
            field=models.DateField(default=None, verbose_name='dob'),
        ),
        migrations.AlterField(
            model_name='representative',
            name='firstName',
            field=models.CharField(max_length=30, verbose_name='Forename'),
        ),
        migrations.AlterField(
            model_name='representative',
            name='lastName',
            field=models.CharField(max_length=30, verbose_name='Surname'),
        ),
    ]