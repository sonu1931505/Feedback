# Generated by Django 5.0.6 on 2024-08-29 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerresponse',
            old_name='selected_option',
            new_name='selected_options',
        ),
        migrations.AlterField(
            model_name='questions',
            name='question_type',
            field=models.CharField(choices=[('Text', 'Text'), ('BigText', 'BigText'), ('Radio', 'Radio'), ('Checkbox', 'Checkboz')], default='Text', max_length=100),
        ),
    ]
