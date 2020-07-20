# Generated by Django 3.0.8 on 2020-07-15 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bid_comment_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='bid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bid',
            name='item',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.Listing'),
            preserve_default=False,
        ),
    ]