# Generated by Django 3.1.2 on 2020-10-24 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story6', '0002_auto_20201024_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='participant',
            name='contact_number',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='participant',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
