# Generated by Django 4.1.3 on 2022-12-08 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zords', '0002_alter_mode_id_alter_zord_id_alter_zord_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zord',
            old_name='type',
            new_name='category',
        ),
    ]
