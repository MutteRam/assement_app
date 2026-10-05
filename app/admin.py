from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CodingQuestion, TestCase

class TestCaseInline(admin.TabularInline):
    model = TestCase
    extra = 3

@admin.register(CodingQuestion)
class CodingQuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'difficulty', 'is_active', 'created_at')
    list_filter = ('difficulty', 'topic', 'is_active')
    search_fields = ('title', 'topic', 'description')
    inlines = [TestCaseInline]
