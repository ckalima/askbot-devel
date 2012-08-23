# -*- coding: utf-8 -*-
"""
:synopsis: connector to standard Django admin interface

To make more models accessible in the Django admin interface, add more classes subclassing ``django.contrib.admin.Model``

Names of the classes must be like `SomeModelAdmin`, where `SomeModel` must 
exactly match name of the model used in the project
"""
from django.contrib import admin
from askbot import models

class AnonymousQuestionAdmin(admin.ModelAdmin):
    """AnonymousQuestion admin class"""

class TagAdmin(admin.ModelAdmin):
    """Tag admin class"""

class VoteAdmin(admin.ModelAdmin):
    """  admin class"""

class FavoriteQuestionAdmin(admin.ModelAdmin):
    """  admin class"""

class PostRevisionAdmin(admin.ModelAdmin):
    """  admin class"""

class AwardAdmin(admin.ModelAdmin):
    """  admin class"""

class ReputeAdmin(admin.ModelAdmin):
    """  admin class"""

class ActivityAdmin(admin.ModelAdmin):
    """  admin class"""
    date_hierarchy = 'active_at'
    list_filter = ('activity_type', 'active_at')
    list_display = ('user', 'activity_type', 'active_at', 'content_type')
    
class ThreadAdmin(admin.ModelAdmin):
    """  admin class"""
    search_fields = ['title']
    date_hierarchy = 'added_at'
    list_filter = ('last_activity_at', 'added_at')
    list_display = ('title', 'added_at', 'last_activity_at', 'answer_count', 'view_count')

class PostAdmin(admin.ModelAdmin):
    """  admin class"""
    search_fields = ['text', 'thread__title']
    date_hierarchy = 'added_at'
    list_filter = ('post_type', 'added_at')
    list_display = ('summary', 'author', 'post_type', 'thread', 'added_at', 'score')

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Thread, ThreadAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Vote, VoteAdmin)
admin.site.register(models.FavoriteQuestion, FavoriteQuestionAdmin)
admin.site.register(models.PostRevision, PostRevisionAdmin)
admin.site.register(models.Award, AwardAdmin)
admin.site.register(models.Repute, ReputeAdmin)
admin.site.register(models.Activity, ActivityAdmin)
