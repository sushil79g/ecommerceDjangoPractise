# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Article

# Create your views here.
def year_archieve(request,  year):
    a_list = Article.objects.filter(pub_date__year = year)
    context = {'year':year, 'article_list':a_list}
    return render(request,'news/year_archieve.html', context)

