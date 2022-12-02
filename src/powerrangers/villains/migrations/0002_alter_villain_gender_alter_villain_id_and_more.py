# Generated by Django 4.1.3 on 2022-12-02 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0003_alter_episode_id_alter_series_id_alter_series_parent'),
        ('villains', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='villain',
            name='gender',
            field=models.CharField(blank=True, choices=[('female', 'Female'), ('male', 'Male')], default=None, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='villain',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='villain',
            name='series',
            field=models.ManyToManyField(blank=True, limit_choices_to=models.Q(('series__isnull', True)), related_name='villains', to='series.series'),
        ),
        migrations.AlterField(
            model_name='villain',
            name='type',
            field=models.CharField(blank=True, choices=[('alchemist', 'Alchemist'), ('boss', 'Boss'), ('general', 'General'), ('henchman', 'Henchman'), ('minion', 'Minion'), ('scientist', 'Scientist')], default=None, max_length=32, null=True),
        ),
    ]
