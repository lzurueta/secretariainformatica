# Generated by Django 4.2.8 on 2025-02-12 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0014_remove_estadoticket_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='estadoticket',
            name='color',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
