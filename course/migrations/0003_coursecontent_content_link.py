# Generated by Django 4.2.3 on 2023-07-25 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0002_coursecontent"),
    ]

    operations = [
        migrations.AddField(
            model_name="coursecontent",
            name="content_link",
            field=models.CharField(max_length=250, null=True),
        ),
    ]
