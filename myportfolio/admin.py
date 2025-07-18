from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Project, Contact

class CustomAdminSite(admin.AdminSite):
    site_header = 'My Custom Admin'
    site_title = 'Custom Admin Portal'
    index_template = 'admin/admin_dashboard.html'

# Create instance of custom admin site
custom_admin_site = CustomAdminSite(name='custom_admin')

# ✅ CORRECT: Register models using ONLY ONE METHOD (choose either A or B)

# --- Option A: Using @admin.register decorator (recommended) ---
@admin.register(Project, site=custom_admin_site)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')

@admin.register(Contact, site=custom_admin_site)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'timestamp')

# --- Option B: Using custom_admin_site.register() ---
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('title', 'link')
#
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'timestamp')
#
# custom_admin_site.register(Project, ProjectAdmin)
# custom_admin_site.register(Contact, ContactAdmin)

# Register auth models (no decorator alternative)
custom_admin_site.register(User)
custom_admin_site.register(Group)