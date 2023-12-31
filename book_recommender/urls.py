"""
URL configuration for book_recommender project.

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from book_recommender.views import top_books_by_category, signup, login, search, add_rating

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books_by_category/<str:category>', top_books_by_category, name='top_books_by_category'),
    path('api/add_rating', add_rating, name='add_rating'),
    path('api/search/<str:query>', search, name='search'),
    path('api/signup', signup),
    path('api/login', login),
]
