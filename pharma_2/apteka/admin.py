from django.contrib import admin

from .models import Category, Question, Answer, ExamManager


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'possible_ticket_numbers',]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['pk', 'number_in_tests', 'text', 'right_answer', 'correct', 'get_answers',]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['pk', 'content', 'question',]


@admin.register(ExamManager)
class ExamManagerAdmin(admin.ModelAdmin):
    list_display = ['pk', 'current_question_number_in_tests', 'right_answers_counter',]
