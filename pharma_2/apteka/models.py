from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    possible_ticket_numbers = models.CharField(max_length=500, blank=True)

    def get_questions(self):
        return self.questions.all()

    def __str__(self):
        return self.name


class Question(models.Model):
    number_in_tests = models.IntegerField(null=False)
    text = models.CharField(max_length=255)
    right_answer = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='questions')

    def get_answers(self):
        return self.answers.all()

    def __str__(self):
        return str(self.number_in_tests)


class Answer(models.Model):
    content = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return self.content


class ExamManager(models.Model):
    current_question_number_in_tests = models.IntegerField(blank=True, default=1)
    right_answers_counter = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return str(self.right_answers_counter)
