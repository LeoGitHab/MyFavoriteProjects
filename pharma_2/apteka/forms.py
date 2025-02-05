from django import forms

from .models import Answer, Question, ExamManager


class AnswerForm(forms.Form):

    class Meta:
        model = Answer
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        list_content = Answer.objects.filter(
            question_id=ExamManager.objects.all().first().current_question_number_in_tests
        )
        print('list_content = ', list_content)

        MyListTuples = [(str(c.id), c.content) for c in list_content]
        print('MyListTuples = ', MyListTuples)

        content = forms.MultipleChoiceField(
            choices=MyListTuples,
            widget=forms.CheckboxSelectMultiple(),
        #     initial=[('5', 'индивидуальные'), ('6', 'общие'), ('7', 'универсальные'), ('8', 'специальные')]
        )

        self.fields['content'] = content
