from django.db import models
from wagtail.images.models import Image, AbstractImage, AbstractRendition

# Custom image model that extends Wagtail's AbstractImage
class CustomImage(AbstractImage):
    # Add a caption field to the image model
    caption = models.CharField(max_length=255, blank=True)
    
    # Update the admin form fields to include the caption
    admin_form_fields = Image.admin_form_fields + ('caption',)
    
# Custom rendition model that extends Wagtail's AbstractRendition    
# A rendition is a specific version of an image (e.g., resized, cropped)
class CustomRendition(AbstractRendition):
    # Link the rendition to the custom image model
    image = models.ForeignKey(
        CustomImage, related_name='renditions', on_delete=models.CASCADE
    ) 
    
    class Meta:
        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )


