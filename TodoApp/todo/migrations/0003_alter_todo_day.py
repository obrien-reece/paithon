# Generated by Django 4.2.6 on 2023-10-16 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_day_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dow', to='todo.day'),
        ),
    ]