# Generated by Django 4.2.1 on 2023-05-22 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0004_song_band"),
    ]

    operations = [
        migrations.AddField(
            model_name="band",
            name="like_new",
            field=models.BooleanField(default=False),
        ),
    ]