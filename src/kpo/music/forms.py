from django.forms import ModelForm
from music.models import File


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ('file_name', 'pdf', 'part')