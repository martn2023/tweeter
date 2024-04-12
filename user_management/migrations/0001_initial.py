# Generated by Django 5.0.4 on 2024-04-10 13:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedUserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=300)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extended_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]