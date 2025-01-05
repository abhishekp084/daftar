# Generated by Django 5.1.4 on 2025-01-05 05:43

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
        ('wagtailcore', '0094_alter_page_locale'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('author', models.CharField(max_length=255)),
                ('date', models.DateField(verbose_name='Post date')),
                ('content', wagtail.fields.StreamField([('title', 1), ('text', 3), ('image', 6), ('link', 9)], block_lookup={0: ('wagtail.blocks.CharBlock', (), {'help_text': 'Add your title', 'required': True}), 1: ('wagtail.blocks.StructBlock', [[('text', 0)]], {}), 2: ('wagtail.blocks.RichTextBlock', (), {'required': True}), 3: ('wagtail.blocks.StructBlock', [[('text', 2)]], {}), 4: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': True}), 5: ('wagtail.blocks.CharBlock', (), {'required': False}), 6: ('wagtail.blocks.StructBlock', [[('image', 4), ('caption', 5)]], {}), 7: ('wagtail.blocks.CharBlock', (), {'required': True}), 8: ('wagtail.blocks.URLBlock', (), {'required': True}), 9: ('wagtail.blocks.StructBlock', [[('button_text', 7), ('button_link', 8)]], {})})),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='jobpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='JobIndexPage',
        ),
        migrations.DeleteModel(
            name='JobPage',
        ),
    ]
