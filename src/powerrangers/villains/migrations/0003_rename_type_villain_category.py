# Generated by Django 4.1.3 on 2022-12-08 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('villains', '0002_alter_villain_gender_alter_villain_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='villain',
            old_name='type',
            new_name='category',
        ),
    ]
