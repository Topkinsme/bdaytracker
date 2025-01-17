# Generated by Django 5.1.1 on 2024-09-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdayapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='name',
            new_name='person_name',
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('BIRTHDAY', 'Birthday'), ('WED-ANNI', 'Wedding Anniversary'), ('MISC', 'Misc')], default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(),
        ),
    ]
