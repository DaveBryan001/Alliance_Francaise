from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.blocks import CharBlock, RichTextBlock, StructBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.search import index
from wagtail.embeds.blocks import EmbedBlock
from wagtail.documents.blocks import DocumentChooserBlock
# from wagtail.admin.edit_handlers import FieldPanel

# Reusable Content Blocks (Snippets)
@register_snippet
class Testimonial(models.Model):
    """A testimonial from a student or member."""
    text = models.TextField()
    author = models.CharField(max_length=255)

    panels = [
        FieldPanel('text'),
        FieldPanel('author'),
    ]

    def __str__(self):
        return f"Testimonial by {self.author}"


# Page Models
class HomePage(Page):
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    intro_text = RichTextField(blank=True)
    testimonials = StreamField([
        ('testimonial', StructBlock([
            ('quote', RichTextBlock()),
            ('author', CharBlock()),
            ('role', CharBlock())
        ]))
    ], null=True, blank=True)


    content_panels = Page.content_panels + [
        FieldPanel('banner_image'),
        FieldPanel('intro_text'),
        FieldPanel('testimonials'),
    ]

class MaterialsBlock(StructBlock):
    title = CharBlock(required=True, max_length=100)
    content = StreamField([
        ('text', RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock()),
        ('document', DocumentChooserBlock()),
    ])

    class Meta:
        icon = 'doc-full-inverse'

class CoursePage(Page):
    level = models.CharField(
        max_length=50,
        choices=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
        ]
    )
    description = RichTextField()
    schedule = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    instructor = models.CharField(max_length=255, blank=True)  # Add instructor field
    materials = StreamField([
        ('materials_block', MaterialsBlock())
    ], blank=True, use_json_field=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    enrollment_link = models.URLField(max_length=200, blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('level'),
        FieldPanel('description'),
        FieldPanel('schedule'),
        FieldPanel('price'),
        FieldPanel('image'),
        FieldPanel('instructor'),
        FieldPanel('start_date'),
        FieldPanel('end_date'),
        FieldPanel('enrollment_link'),
        FieldPanel('materials'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('description'),
        index.SearchField('level'),
        index.SearchField('instructor'),
    ]

    def __str__(self):
        return self.title

class EventPage(Page):
    date = models.DateTimeField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    description = RichTextField()
    event_image = models.ForeignKey(
        'wagtailimages.Image',  
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Make EventPage searchable
    search_fields = Page.search_fields + [
        index.SearchField('description'),
        index.FilterField('date'), 
    ] 

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('time'),
        FieldPanel('location'),
        FieldPanel('description'),
        # ImageChooserBlock('event_image'), 
    ]

class BlogPost(Page):
    author = models.CharField(max_length=255)
    date = models.DateField("Post date", auto_now_add=True)
    body = RichTextField()

    search_fields = Page.search_fields + [
        index.SearchField('title'), 
        index.SearchField('body'),
        index.FilterField('date'), 
    ]

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('body'),
    ]

class AboutUsPage(Page):
    mission = RichTextField()
    history = RichTextField()
    # ... add fields for team members or use snippets

    content_panels = Page.content_panels + [
        FieldPanel('mission'),
        FieldPanel('history'),
        # ... panels for team members
    ]

