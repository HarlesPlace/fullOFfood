# Generated by Django 5.1.2 on 2024-11-07 23:01

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("titulo", models.CharField(max_length=255)),
                ("conteudo", models.TextField()),
                ("data", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]