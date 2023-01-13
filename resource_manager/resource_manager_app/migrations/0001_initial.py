# Generated by Django 4.1.5 on 2023-01-13 01:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BranchOffice",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("address", models.CharField(max_length=255)),
                ("nit", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=255)),
                ("creation_date", models.DateField(auto_now_add=True)),
                ("active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Resource",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("creation_date", models.DateField(auto_now_add=True)),
                ("active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Technician",
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
                ("name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("id_number", models.CharField(max_length=255)),
                ("code", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("creation_date", models.DateField(auto_now_add=True)),
                ("active", models.BooleanField(default=True)),
                (
                    "base_salary",
                    models.FloatField(
                        default=0.0,
                        validators=[django.core.validators.MinValueValidator(0.0)],
                    ),
                ),
                (
                    "branch_office",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="resource_manager_app.branchoffice",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ResourceAssignment",
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
                ("assignment_date", models.DateField(auto_now_add=True)),
                (
                    "quantity",
                    models.SmallIntegerField(
                        default=1,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(10),
                        ],
                    ),
                ),
                (
                    "resource",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="resource_manager_app.resource",
                    ),
                ),
                (
                    "technician",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="resource_manager_app.technician",
                    ),
                ),
            ],
        ),
    ]