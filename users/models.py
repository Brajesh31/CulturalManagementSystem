from django.db import models

# Create your models here.
class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    password=models.CharField(max_length=100,blank=False)
    email=models.CharField(max_length=100,blank=False)
    username=models.CharField(max_length=100,blank=False)

    class Meta:
        db_table="user_table"
    def str(self):
        return self.username