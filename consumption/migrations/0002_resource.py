# Generated by Django 4.0.2 on 2022-02-11 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consumption', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of this resource', max_length=50, verbose_name='Resource Name')),
                ('description', models.TextField(blank=True, help_text='An optional description for this resource', verbose_name='Resource Description')),
                ('unit', models.CharField(help_text='The unit of measurement for this resource', max_length=25, verbose_name='Unit of Measurement')),
                ('subject', models.ForeignKey(help_text='The subject to track this resource for', on_delete=django.db.models.deletion.CASCADE, to='consumption.subject', verbose_name='Subject Instance')),
            ],
            options={
                'verbose_name': 'Resource',
                'verbose_name_plural': 'Resources',
            },
        ),
    ]
