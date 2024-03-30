# Generated by Django 5.0.3 on 2024-03-28 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("switchkey", "0014_alter_organizationgroup_project"),
    ]

    operations = [
        migrations.RenameField(
            model_name="featurestorage",
            old_name="created_at",
            new_name="created",
        ),
        migrations.RenameField(
            model_name="featurestorage",
            old_name="modified_at",
            new_name="modified",
        ),
        migrations.RenameField(
            model_name="organization",
            old_name="created_at",
            new_name="created",
        ),
        migrations.RenameField(
            model_name="organization",
            old_name="modified_at",
            new_name="modified",
        ),
        migrations.RenameField(
            model_name="organizationgroup",
            old_name="created_at",
            new_name="created",
        ),
        migrations.RenameField(
            model_name="organizationgroup",
            old_name="modified_at",
            new_name="modified",
        ),
        migrations.RenameField(
            model_name="organizationproject",
            old_name="created_at",
            new_name="created",
        ),
        migrations.RenameField(
            model_name="organizationproject",
            old_name="modified_at",
            new_name="modified",
        ),
        migrations.RenameField(
            model_name="projectenvironment",
            old_name="created_at",
            new_name="created",
        ),
        migrations.RenameField(
            model_name="projectenvironment",
            old_name="modified_at",
            new_name="modified",
        ),
        migrations.RenameField(
            model_name="projectenvironmentuser",
            old_name="created_at",
            new_name="created",
        ),
        migrations.RenameField(
            model_name="projectenvironmentuser",
            old_name="modified_at",
            new_name="modified",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="created_at",
            new_name="created",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="modified_at",
            new_name="modified",
        ),
        migrations.RenameField(
            model_name="userdevice",
            old_name="created_at",
            new_name="created",
        ),
        migrations.RenameField(
            model_name="userdevice",
            old_name="modified_at",
            new_name="modified",
        ),
    ]