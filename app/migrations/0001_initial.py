# Generated by Django 5.1.5 on 2025-01-30 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="About",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("age", models.PositiveIntegerField()),
                ("height", models.CharField(max_length=10)),
                ("weight", models.CharField(max_length=10)),
                ("nationality", models.CharField(max_length=50)),
                ("languages", models.CharField(max_length=100)),
                ("profile_image", models.ImageField(upload_to="profile_images/")),
            ],
        ),
    ]
