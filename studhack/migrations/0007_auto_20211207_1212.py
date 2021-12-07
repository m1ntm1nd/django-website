# Generated by Django 3.2.9 on 2021-12-07 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studhack', '0006_tasks_brief_descr'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='brief_descr',
            field=models.CharField(default=" Lorem Ipsum is simply dummy text of the printing and typesetting industry. \n                            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, \n                            when an unknown printer took a galley of type and scrambled it to make a type specimen book. ", max_length=50),
        ),
    ]
