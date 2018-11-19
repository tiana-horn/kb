# Generated by Django 2.1.3 on 2018-11-16 20:59

from django.db import migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0006_adoptionapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoptionapplication',
            name='state',
            field=localflavor.us.models.USStateField(default='AL', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adoptionapplication',
            name='zip',
            field=localflavor.us.models.USZipCodeField(default='36027', max_length=10),
            preserve_default=False,
        ),
    ]