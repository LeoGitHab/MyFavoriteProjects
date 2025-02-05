import ast
import random

from django.db import transaction
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from .forms import AnswerForm
from .models import Category, Question, ExamManager


def category_list(request: HttpRequest):
    context = {
        'categories': Category.objects.all()
    }

    for category in context['categories']:
        ticks = [tick.id for tick in Question.objects.filter(category_id=category.pk)]
        category.possible_ticket_numbers = str(ticks)
        category.save()

    exam_manager = ExamManager.objects.first()
    exam_manager.right_answers_counter = 0
    exam_manager.current_question_number_in_tests = 0
    exam_manager.save()

    return render (request, 'start.html', context=context)


def ticket_request(request: HttpRequest, pk):
    print('request = ', request.POST)
    category = Category.objects.get(id=pk)
    # При помощи библиотеки 'ast', получаем список из строки со списком
    list_of_possible_tickets_ids = ast.literal_eval(category.possible_ticket_numbers)
    print('list_of_possible_tickets_ids = ', list_of_possible_tickets_ids)

    if not list_of_possible_tickets_ids:
        return render(request, "no_tickets.html", context={"body": "<h1>No Tickets Here !</h1>"})

    # Выбираем случайный билет из предложенного списка, и, удаляем этот билет из списка
    random_ticket_id = random.choice(list_of_possible_tickets_ids)
    list_of_possible_tickets_ids.remove(random_ticket_id)

    # Список - обратно в строку со списком внутри, и - сохраняем в БД
    category.possible_ticket_numbers = str(list_of_possible_tickets_ids)
    category.save()

    ticket = Question.objects.get(category=pk, id=random_ticket_id)
    print('ticket = ', ticket)
    print('ticket.id = ', ticket.id)
    print('ticket.answers = ', ticket.answers.all())

    with transaction.atomic():
        exam_manager = ExamManager.objects.select_for_update().first()
        exam_manager.current_question_number_in_tests = ticket.id
        exam_manager.save()

    if request.method == 'POST':
        # my_instance = Answer.objects.get(id=ticket.id)
        # form = AnswerForm(request.POST, instance=my_instance)

        form = AnswerForm(request.POST)
        # print('form.cleaned_data = ', form.cleaned_data)
        print('data_after_form = ', request.POST)
        print('form.fields_after_form = ', form.fields)
        print(form.errors)
        print(form.non_field_errors)

        if form.is_valid():
            print('form is valid')
            data = {
                'content': form.cleaned_data['content']}
            print('form.cleaned_data = ', form.cleaned_data)
            print('DATA = ', data)
            # form.save(commit=False)
            # form = AnswerForm()
            # return render(request, 'ticket.html', {'ticket': ticket, 'form': form})

            # return http.HttpResponseRedirect('')
            # return render(request, 'ticket.html', {'ticket': ticket, 'form': form})
    else:
        print('form is invalid')
        form = AnswerForm()
    print(40 * '*')
    print()
    print()
    return render(request, 'ticket.html', {'ticket': ticket, 'form': form})
