# Generated by Django 3.1.4 on 2020-12-22 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewrating',
            name='rating',
            field=models.PositiveIntegerField(choices=[(1, 'Very bad'), (2, 'Bad'), (3, 'Okay'), (4, 'Good'), (5, 'Excellent')], default=5),
        ),
    ]
