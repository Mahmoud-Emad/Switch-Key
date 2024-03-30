# Generated by Django 5.0.3 on 2024-03-29 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("switchkey", "0020_alter_organization_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organization",
            name="name",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="organizationproject",
            name="name",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterUniqueTogether(
            name="organizationproject",
            unique_together={("name", "organization")},
        ),
    ]