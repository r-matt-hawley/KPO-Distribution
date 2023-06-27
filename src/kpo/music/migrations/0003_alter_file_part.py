# Generated by Django 4.2 on 2023-06-27 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0002_alter_file_part"),
    ]

    operations = [
        migrations.AlterField(
            model_name="file",
            name="part",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="files",
                to="music.part",
            ),
        ),
    ]