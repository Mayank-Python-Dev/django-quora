from django.contrib import admin
from .models import (
    Question,
    Answer
)

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("uid","author","question","created_at","updated_at")
    # fields = ["uid","author","question", ("created_at","updated_at")]


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("uid","question","user","answer","get_user_likes","created_at","updated_at")

    def get_user_likes(self, obj):
        return "|".join([user.username for user in obj.likes.all()])


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)