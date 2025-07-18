from django.db import models

# admin.py
from django.contrib import admin

class CustomAdminSite(admin.AdminSite):
    site_header = 'My Custom Admin'
    site_title = 'Custom Admin Portal'
    index_template = 'admin/admin_dashboard.html'

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='myportfolio/images/')

    def __str__(self):  # <-- Correct indentation
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


 