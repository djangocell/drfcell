# Generated by Django 4.0.3 on 2022-09-03 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cell', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cell',
            name='next_cell',
            field=models.ManyToManyField(blank=True, to='cell.cell'),
        ),
    ]
