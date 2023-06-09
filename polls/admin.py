from django.contrib import admin

from .models import Question, Choice
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,   {'fields': ['question_text']}),
        ('Date Information', {'fields':['pub_date'],'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently')

# class ChoiceAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,   {'fields': ['question']}),
#         (None,{'fields':['choice_text']}),
#         (None,{'fields':['votes']})
#     ]
    

admin.site.register(Question,QuestionAdmin)
# admin.site.register(Choice)