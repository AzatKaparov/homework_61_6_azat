# Generated by Django 2.2 on 2020-08-23 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20200823_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tasks_project', to='webapp.Project', verbose_name='Проект'),
        ),
    ]
