from django.forms import ModelForm
from music.models import File

# TODO: Should this be in models.py?
# Django docs put it in models.py, whereas tutorial has it here
class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ('title', 'pdf', 'part')