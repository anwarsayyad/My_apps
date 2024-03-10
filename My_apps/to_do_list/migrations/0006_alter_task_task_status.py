# Generated by Django 5.0.1 on 2024-03-10 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0005_alter_task_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.CharField(choices=[('Planned', 'Planned'), ('Working_On', 'Working On'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], max_length=200),
        ),
    ]
