# Generated by Django 5.0.3 on 2024-03-28 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("switchkey", "0013_alter_featurestorage_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organizationgroup",
            name="project",
            field=models.ManyToManyField(
                related_name="project_groups", to="switchkey.organizationproject"
            ),
        ),
    ]