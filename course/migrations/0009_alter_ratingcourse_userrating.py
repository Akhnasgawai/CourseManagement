# Generated by Django 4.2.3 on 2023-08-03 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0008_ratingcourse"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ratingcourse",
            name="userRating",
            field=models.IntegerField(default=0),
        ),
    ]
