# Generated by Django 5.1.4 on 2025-01-05 09:25

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_alter_jobpostpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpostpage',
            name='content',
            field=wagtail.fields.StreamField([('recruitment_header', 3), ('important_dates', 8), ('vacancy_details', 14), ('category_distribution', 18), ('eligibility', 21), ('application_fee', 25), ('important_links', 27), ('how_to_apply', 30), ('additional_information', 32)], block_lookup={0: ('wagtail.blocks.CharBlock', (), {'required': True}), 1: ('wagtail.blocks.CharBlock', (), {'required': False}), 2: ('wagtail.blocks.IntegerBlock', (), {'required': True}), 3: ('wagtail.blocks.StructBlock', [[('post_name', 0), ('organization', 0), ('advertisement_number', 1), ('total_vacancies', 2)]], {}), 4: ('wagtail.blocks.DateBlock', (), {'required': True}), 5: ('wagtail.blocks.DateBlock', (), {'required': False}), 6: ('wagtail.blocks.CharBlock', (), {'help_text': "Can be a specific date or text like 'As per Schedule'", 'required': False}), 7: ('wagtail.blocks.CharBlock', (), {'help_text': "Can be a specific date or text like 'Before Exam'", 'required': False}), 8: ('wagtail.blocks.StructBlock', [[('application_start_date', 4), ('application_end_date', 4), ('fee_payment_deadline', 5), ('exam_date', 6), ('admit_card_date', 7)]], {}), 9: ('wagtail.blocks.CharBlock', (), {}), 10: ('wagtail.blocks.IntegerBlock', (), {}), 11: ('wagtail.blocks.ListBlock', (9,), {}), 12: ('wagtail.blocks.StructBlock', [[('category_name', 9), ('number_of_posts', 10), ('eligibility', 11)]], {}), 13: ('wagtail.blocks.StreamBlock', [[('category', 12)]], {}), 14: ('wagtail.blocks.StructBlock', [[('post_name', 9), ('category_distribution', 13)]], {}), 15: ('wagtail.blocks.CharBlock', (), {'default': 'Category Wise Vacancy Details'}), 16: ('wagtail.blocks.StructBlock', [[('post_name', 9), ('post_code', 9), ('ur', 10), ('obc', 10), ('ews', 10), ('sc', 10), ('st', 10), ('total', 10)]], {}), 17: ('wagtail.blocks.ListBlock', (16,), {}), 18: ('wagtail.blocks.StructBlock', [[('block_title', 15), ('categories', 17)]], {}), 19: ('wagtail.blocks.RichTextBlock', (), {}), 20: ('wagtail.blocks.RichTextBlock', (), {'required': False}), 21: ('wagtail.blocks.StructBlock', [[('minimum_age', 10), ('maximum_age', 10), ('educational_qualification', 19), ('age_relaxation', 20)]], {}), 22: ('wagtail.blocks.DecimalBlock', (), {}), 23: ('wagtail.blocks.StructBlock', [[('category_name', 9), ('fee_amount', 22)]], {}), 24: ('wagtail.blocks.StreamBlock', [[('category_fee', 23)]], {}), 25: ('wagtail.blocks.StructBlock', [[('fee_categories', 24), ('payment_methods', 11)]], {}), 26: ('wagtail.blocks.URLBlock', (), {'required': False}), 27: ('wagtail.blocks.StructBlock', [[('apply_online_url', 26), ('notification_url', 26), ('official_website', 26)]], {}), 28: ('wagtail.blocks.CharBlock', (), {'default': 'How to Apply', 'required': True}), 29: ('wagtail.blocks.ListBlock', (19,), {}), 30: ('wagtail.blocks.StructBlock', [[('title', 28), ('steps', 29)]], {}), 31: ('wagtail.blocks.RichTextBlock', (), {'required': True}), 32: ('wagtail.blocks.StructBlock', [[('text', 31)]], {'required': False})}),
        ),
    ]
