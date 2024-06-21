# Generated by Django 5.0.4 on 2024-06-21 19:29

import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_alter_commenttask_created_alter_task_time_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commenttask',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 21, 19, 29, 45, 252950)),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 21, 19, 29, 45, 252676)),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_finish',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 21, 19, 29, 45, 252682)),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 21, 19, 29, 45, 252525)),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('8f12ceac-9c66-4be8-9ff8-cd0f35438023'), verbose_name='uuid'),
        ),
    ]
