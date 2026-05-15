from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.images import get_image_model

class HomePage(Page):
    # Custom fields for model
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    body = RichTextField(blank=True)
    
    image = models.ForeignKey(
        get_image_model(), # Retrieve image model name based on config. Alternatively, a string can be passed in, e.g., 'wagtailimages.Image'
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    # Include custom fields in the admin interface
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
        FieldPanel('image'),
    ]    
    

