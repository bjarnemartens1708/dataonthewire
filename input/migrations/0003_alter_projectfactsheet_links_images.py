# Generated by Django 4.1.2 on 2022-10-31 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0002_rename_inputdate_projectfactsheet_input_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectfactsheet',
            name='links_Images',
            field=models.FileField(blank=True, upload_to='linkImages/'),
        ),
    ]
