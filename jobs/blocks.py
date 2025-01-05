# jobs/blocks.py
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleBlock(blocks.StructBlock):
    text = blocks.CharBlock(required=True, help_text="Add your title")
    
    class Meta:
        template = "jobs/blocks/title_block.html"
        icon = "title"
        label = "Title"

class TextBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(required=True)
    
    class Meta:
        template = "jobs/blocks/text_block.html"
        icon = "doc-full"
        label = "Text"

class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    caption = blocks.CharBlock(required=False)
    
    class Meta:
        template = "jobs/blocks/image_block.html"
        icon = "image"
        label = "Image"

class LinkBlock(blocks.StructBlock):
    button_text = blocks.CharBlock(required=True)
    button_link = blocks.URLBlock(required=True)
    
    class Meta:
        template = "jobs/blocks/link_block.html"
        icon = "link"
        label = "Link"

# Add job-specific blocks
class ImportantDatesBlock(blocks.StructBlock):
    date_label = blocks.CharBlock(required=True)
    date = blocks.DateBlock(required=True)
    time = blocks.TimeBlock(required=False)

    class Meta:
        template = "jobs/blocks/important_dates_block.html"
        icon = "date"
        label = "Important Date"

class ApplicationFeeBlock(blocks.StructBlock):
    category = blocks.CharBlock(required=True)
    amount = blocks.CharBlock(required=True)
    
    class Meta:
        template = "jobs/blocks/application_fee_block.html"
        icon = "dollar"
        label = "Application Fee"

class VacancyDetailsBlock(blocks.StructBlock):
    trade_name = blocks.CharBlock(required=True)
    total_posts = blocks.CharBlock(required=True)
    eligibility = blocks.RichTextBlock(required=False)
    
    class Meta:
        template = "jobs/blocks/vacancy_details_block.html"
        icon = "group"
        label = "Vacancy Details"
        
        
        

# jobs/blocks.py
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class RecruitmentHeaderBlock(blocks.StructBlock):
    post_name = blocks.CharBlock(required=True)
    organization = blocks.CharBlock(required=True)
    advertisement_number = blocks.CharBlock(required=False)
    total_vacancies = blocks.IntegerBlock(required=True)

    class Meta:
        template = 'jobs/blocks/recruitment_header_block.html'
        icon = 'title'

class ImportantDatesBlock(blocks.StructBlock):
    application_start_date = blocks.DateBlock(required=True)
    application_end_date = blocks.DateBlock(required=True)
    fee_payment_deadline = blocks.DateBlock(required=False)
    exam_date = blocks.CharBlock(required=False, help_text="Can be a specific date or text like 'As per Schedule'")
    admit_card_date = blocks.CharBlock(required=False, help_text="Can be a specific date or text like 'Before Exam'")


    class Meta:
        template = 'jobs/blocks/important_dates_block.html'
        icon = 'date'

class VacancyDetailsBlock(blocks.StructBlock):
    post_name = blocks.CharBlock()
    category_distribution = blocks.StreamBlock([
        ('category', blocks.StructBlock([
            ('category_name', blocks.CharBlock()),
            ('number_of_posts', blocks.IntegerBlock()),
               ('eligibility', blocks.ListBlock(blocks.CharBlock()))

        ]))
    ])

    class Meta:
        template = 'jobs/blocks/vacancy_details_block.html'
        icon = 'group'

class CategoryDistributionBlock(blocks.StructBlock):
    block_title = blocks.CharBlock(default="Category Wise Vacancy Details")
    categories = blocks.ListBlock(blocks.StructBlock([
        ('post_name', blocks.CharBlock()),
        ('post_code', blocks.CharBlock()),
        ('ur', blocks.IntegerBlock()),
        ('obc', blocks.IntegerBlock()),
        ('ews', blocks.IntegerBlock()),
        ('sc', blocks.IntegerBlock()),
        ('st', blocks.IntegerBlock()),
        ('total', blocks.IntegerBlock())
    ]))

    class Meta:
        template = 'jobs/blocks/category_distribution_block.html'
        icon = 'group'



class EligibilityBlock(blocks.StructBlock):
    minimum_age = blocks.IntegerBlock()
    maximum_age = blocks.IntegerBlock()
    educational_qualification = blocks.RichTextBlock()
    age_relaxation = blocks.RichTextBlock(required=False)

    class Meta:
        template = 'jobs/blocks/eligibility_block.html'
        icon = 'user'
        
class ApplicationFeeBlock(blocks.StructBlock):
    fee_categories = blocks.StreamBlock([
        ('category_fee', blocks.StructBlock([
            ('category_name', blocks.CharBlock()),
            ('fee_amount', blocks.DecimalBlock()),
        ]))
    ])
    payment_methods = blocks.ListBlock(blocks.CharBlock())

    class Meta:
        template = 'jobs/blocks/application_fee_block.html'
        icon = 'plus'
        
class ImportantLinksBlock(blocks.StructBlock):
    apply_online_url = blocks.URLBlock(required=False)
    notification_url = blocks.URLBlock(required=False)
    official_website = blocks.URLBlock(required=False)

    class Meta:
        template = 'jobs/blocks/important_links_block.html'
        icon = 'link'

class HowToApplyBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, default="How to Apply")
    steps = blocks.ListBlock(blocks.RichTextBlock())

    class Meta:
        template = 'jobs/blocks/how_to_apply_block.html'
        icon = 'doc-full'