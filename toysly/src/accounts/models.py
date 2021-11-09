from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

def seller_doc_path(instance, x):
    # file will be uploaded to MEDIA_ROOT/'seller_documents'/seller_<id>
    return 'seller_documents/seller_{0}'.format(instance.user.id)

def file_size(value):
    limit = 5 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 5 MiB.')

class Seller(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
	agency_name = models.CharField(max_length=100)
	approval_doc = models.FileField(upload_to=seller_doc_path,validators=[file_size, FileExtensionValidator( ['pdf'] ) ])
	def __str__(self):
		return str(self.id)+' '+str(self.user.first_name)