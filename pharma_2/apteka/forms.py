from django import forms
from django.forms import MultipleChoiceField, RadioSelect

from django.forms.widgets import CheckboxSelectMultiple

from .models import Answer, Question, ExamManager


class AnswerForm(forms.Form):
    # content = MultipleChoiceField(widget=CheckboxSelectMultiple)

    # content = forms.ModelChoiceField(queryset=None)

    class Meta:
        model = Answer
        fields = ('content',)
        exclude = ('question',)
        widgets = {'content': RadioSelect}

    def __init__(self, *args, **kwargs):

        super(AnswerForm, self).__init__(*args, **kwargs)
        # self.exam_manager = ExamManager.objects.all().first()
        # print('2_exam_manager.current_question_number_in_tests = ', exam_manager.current_question_number_in_tests)
    #     content = Answer.objects.filter(question=exam_manager.current_question_number_in_tests)
        content = forms.ModelChoiceField(
            queryset=Answer.objects.filter(
                question_id=ExamManager.objects.all().first().current_question_number_in_tests),
            label='Выберите ответ :',
            widget=RadioSelect,
            required=False,
            to_field_name='content')
        self.fields['content'] = content

        # self.fields['content'].queryset = Answer.objects.filter(
        #         question_id=ExamManager.objects.all().first().current_question_number_in_tests)

        # print('CONTENT = ', content)

    # def valid_value(self):
    #     print('OK')

        # choices = [(obj.pk, obj.content) for obj in objects]
        # print('choices = ', choices)
        # self.fields['content'].choices = choices

        # objects_list = []
        # for obj in objects:
        #     objects_list.append(str(obj))
        #
        # print('objects_list = ', objects_list)

    # content = forms.ModelChoiceField
    # exam_manager = ExamManager.objects.all().first()
    # print('exam_manager = ', exam_manager)
    # print('exam_manager.current_question_number_in_tests = ', exam_manager.current_question_number_in_tests)
    # content = forms.ModelChoiceField(
    #     queryset=Answer.objects.filter(question_id=ExamManager.objects.all().first().current_question_number_in_tests),
    #     label='Выберите ответ :',
    #     widget=RadioSelect,
    #     required=False,
    #     to_field_name="content")

    # content = forms.ModelChoiceField(
    #     queryset=Question.objects.values('answers'),
    #     label='Выберите ответ :',
    #     widget=RadioSelect,
    #     required=False,
    #     )