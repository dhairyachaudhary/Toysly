from django.db import models
from django.contrib.auth.models import User

def seller_doc_path(instance, x):
    # file will be uploaded to MEDIA_ROOT/'seller_documents'/seller_<id>
    return 'seller_documents/seller_{0}'.format(instance.user.id)

class Seller(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
	agency_name = models.CharField(max_length=100)
	approval_doc = models.FileField(upload_to=seller_doc_path)
	def __str__(self):
		return str(self.id)+' '+str(self.user.first_name)