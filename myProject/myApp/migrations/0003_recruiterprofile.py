# Generated by Django 5.0.6 on 2024-06-11 07:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_applyjob'),
    ]

    operations = [
        migrations.CreateModel(
            name='recruiterprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100, null=True)),
                ('company_address', models.CharField(max_length=100, null=True)),
                ('company_description', models.TextField(null=True)),
                ('myuser', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RecruiterProfile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
