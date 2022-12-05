# Generated by Django 4.1.3 on 2022-12-02 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zords', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mode',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='zord',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='zord',
            name='type',
            field=models.CharField(choices=[('carrierzord', 'Carrierzord'), ('dinozord', 'Dinozord'), ('ninjazord', 'Ninjazord'), ('shogunzord', 'Shogunzord'), ('thunderzord', 'Thunderzord')], max_length=32),
        ),
    ]