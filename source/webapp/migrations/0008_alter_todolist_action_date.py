# Generated by Django 4.1.5 on 2023-02-13 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0007_alter_todolist_action_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todolist",
            name="action_date",
            field=models.DateField(verbose_name="Date of completion"),
        ),
    ]
