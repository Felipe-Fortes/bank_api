from django.db import models

class Bank(models.Model):
    compensation_code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=70)
 
    def to_dict(self):
         return {
            "compensation_code": self.compensation_code,
            "name": self.name,
        }