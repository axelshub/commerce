# Generated by Django 3.0.8 on 2020-07-16 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20200715_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='sold_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='listings', to=settings.AUTH_USER_MODEL),
        ),
    ]
