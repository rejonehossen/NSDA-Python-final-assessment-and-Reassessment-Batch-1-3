# Generated by Django 5.0.6 on 2024-06-11 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_applyjob_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='education',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='qualifications',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
