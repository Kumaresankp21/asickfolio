# Generated by Django 5.1.5 on 2025-01-30 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_skill"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("technologies", models.TextField(blank=True, null=True)),
                ("link", models.URLField(blank=True, null=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="project_images/"
                    ),
                ),
            ],
        ),
    ]
