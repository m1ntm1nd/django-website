# Generated by Django 3.2.9 on 2021-12-06 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studhack', '0003_auto_20211206_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participants',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='studhack.teams'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
