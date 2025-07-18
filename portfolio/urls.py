"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.auth.decorators import login_required
from myportfolio.admin import custom_admin_site

urlpatterns = [
    # Your custom admin (proper implementation)
    path('admin/', custom_admin_site.urls),  # This should be the main admin URL
    
    # Original admin as backup (optional)
    path('original-admin/', admin.site.urls),
    
    # Your main app URLs
    path('', include('myportfolio.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)