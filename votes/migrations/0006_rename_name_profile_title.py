# Generated by Django 4.0.5 on 2022-06-12 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0005_profile_date_created_profile_last_updated_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='title',
        ),
    ]
