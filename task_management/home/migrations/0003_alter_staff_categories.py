# Generated by Django 4.2.7 on 2023-11-27 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_staff_experience_alter_staff_expert_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='home.category'),
        ),
    ]
