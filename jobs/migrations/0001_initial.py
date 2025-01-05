# Generated by Django 5.1.4 on 2025-01-05 05:13

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0094_alter_page_locale'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('introduction', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='JobPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('company_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('salary', models.CharField(blank=True, max_length=100)),
                ('job_type', models.CharField(choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('contract', 'Contract'), ('freelance', 'Freelance')], max_length=100)),
                ('description', wagtail.fields.RichTextField()),
                ('requirements', wagtail.fields.RichTextField()),
                ('application_deadline', models.DateField()),
                ('contact_email', models.EmailField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
