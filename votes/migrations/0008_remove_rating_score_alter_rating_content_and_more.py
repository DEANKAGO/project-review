# Generated by Django 4.0.5 on 2022-06-12 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0007_rating_score_alter_profile_prof_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='score',
        ),
        migrations.AlterField(
            model_name='rating',
            name='content',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='design',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='usability',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
