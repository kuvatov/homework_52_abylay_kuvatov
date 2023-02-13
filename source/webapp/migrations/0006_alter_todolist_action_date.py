# Generated by Django 4.1.5 on 2023-02-13 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0005_alter_todolist_action_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todolist",
            name="action_date",
            field=models.CharField(
                help_text="Please use the following format: <em>YYYY-MM-DD</em>.",
                max_length=20,
                verbose_name="Date of completion",
            ),
        ),
    ]
