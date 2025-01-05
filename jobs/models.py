# jobs/models.py
from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from . import blocks

class JobPostPage(Page):
    organization = models.CharField(max_length=255)
    advertisement_number = models.CharField(max_length=100)
    post_title = models.CharField(max_length=255)
    
    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    short_description = RichTextField(blank=True)
    
    content = StreamField([
        ('recruitment_header', blocks.RecruitmentHeaderBlock()),
        ('important_dates', blocks.ImportantDatesBlock()),
        ('vacancy_details', blocks.VacancyDetailsBlock()),
        ('category_distribution', blocks.CategoryDistributionBlock()),

        ('eligibility', blocks.EligibilityBlock()),
        ('application_fee', blocks.ApplicationFeeBlock()),
        ('important_links', blocks.ImportantLinksBlock()),
        ('how_to_apply', blocks.HowToApplyBlock()),
        ('additional_information', blocks.TextBlock(required=False)),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('organization'),
            FieldPanel('advertisement_number'),
            FieldPanel('post_title'),
            FieldPanel('header_image'),
            FieldPanel('short_description'),
        ], heading="Basic Information"),
        FieldPanel('content'),
    ]

    class Meta:
        verbose_name = "Job Recruitment Post"