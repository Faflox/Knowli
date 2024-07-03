from django.contrib import admin
from learn.models import MathTest, MathTask, Score

# Register your models here.
class MathTaskInline(admin.TabularInline):
    model = MathTask
    extra = 1

@admin.register(MathTest)
class MathTestAdmin(admin.ModelAdmin):
    inlines = [MathTaskInline]
    
@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'test', 'score')
    list_filter = ('user', 'test')
    search_fields = ('user__username', 'test__title')

