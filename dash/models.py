from django.contrib.auth import get_user_model
from django.db import models


USER = get_user_model()


class GenerationHistory(models.Model):
    title = models.CharField(max_length=256)

    # Overrides who the author is going to be
    author_override = models.CharField(max_length=1024)

    # The date the document was created and last modified
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    # The document
    document = models.FileField(upload_to='documents/source/')
    presentation = models.FileField(upload_to='documents/generation/', null=True, blank=True)

    author = models.ForeignKey(USER, on_delete=models.CASCADE, null=True, blank=True)

    @property
    def is_processing(self):
        # Assumes that if presentation is not present, then it's processing
        return self.presentation != '' or self.presentation is not None
