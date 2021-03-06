# Generated by Django 2.2 on 2020-08-23 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_task_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Дата начала')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата окончания')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Описание')),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='type',
            field=models.ManyToManyField(blank=True, default='Задача', related_name='types', to='webapp.Type', verbose_name='Тип задачи'),
        ),
    ]
