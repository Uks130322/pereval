# Generated by Django 5.0.4 on 2024-04-13 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pass_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='autumn',
            field=models.CharField(blank=True, choices=[('1A', '1А'), ('1B', '1Б'), ('2A', '2А'), ('2B', '2Б'), ('3A', '3А'), ('3B', '3Б')], max_length=2, null=True, verbose_name='autumn level'),
        ),
        migrations.AlterField(
            model_name='level',
            name='spring',
            field=models.CharField(blank=True, choices=[('1A', '1А'), ('1B', '1Б'), ('2A', '2А'), ('2B', '2Б'), ('3A', '3А'), ('3B', '3Б')], max_length=2, null=True, verbose_name='spring level'),
        ),
        migrations.AlterField(
            model_name='level',
            name='summer',
            field=models.CharField(blank=True, choices=[('1A', '1А'), ('1B', '1Б'), ('2A', '2А'), ('2B', '2Б'), ('3A', '3А'), ('3B', '3Б')], max_length=2, null=True, verbose_name='summer level'),
        ),
        migrations.AlterField(
            model_name='level',
            name='winter',
            field=models.CharField(blank=True, choices=[('1A', '1А'), ('1B', '1Б'), ('2A', '2А'), ('2B', '2Б'), ('3A', '3А'), ('3B', '3Б')], max_length=2, null=True, verbose_name='winter level'),
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='connect',
            field=models.TextField(blank=True, null=True, verbose_name='connect'),
        ),
        migrations.AlterField(
            model_name='user',
            name='otc',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='patronymic'),
        ),
    ]
