# Generated by Django 4.2.7 on 2023-11-17 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChopinEcstasy', '0002_userprofile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='John Doe', max_length=50),
        ),
    ]