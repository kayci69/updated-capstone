# Generated by Django 5.1.4 on 2024-12-11 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminlog',
            name='type',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]