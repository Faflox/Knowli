from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from learn.models import Test
from learn.forms import AdditionTestForm

# Create your views here.
def Index(request):
    return render(request, 'learn/index.html')

@login_required
def addition_test(request):
    if request.method == 'POST':
        form = AdditionTestForm(request.POST)
        if form.is_valid():
            score = 0
            correct_answers = {
                'answer_1': 12,
                'answer_2': 8,
                'answer_3': 0,
                'answer_4': -7,
                'answer_5': 3,
                'answer_6': 2,
                'answer_7': 1,
                'answer_8': -15,
                'answer_9': 2,
                'answer_10': 55,
            }
            for field_name, correct_answer in correct_answers.items():
                if form.cleaned_data.get(field_name) == correct_answer:
                    score += 1

            Test.objects.create(
                user=request.user,
                test_name="1. klasa, Test: dodawanie",
                score=score
            )
            return redirect('wyniki_testow')
    else:
        form = AdditionTestForm()

    return render(request, 'learn/test_dodawanie.html', {'form': form})

@login_required
def test_results(request):
    latest_test = Test.objects.filter(user=request.user).order_by('-id').first()

    if latest_test:
        total_questions = 10  # Assuming you have a fixed number of questions
        correct_answers = latest_test.score # Adjust based on your model fields
        incorrect_answers = total_questions - correct_answers
        score = (correct_answers / total_questions) * 100  # Calculate score percentage

        context = {
            'total_questions': total_questions,
            'correct_answers': correct_answers,
            'incorrect_answers': incorrect_answers,
            'score': score,
        }
        return render(request, 'learn/wyniki_testow.html', context)
    else:
        # Handle case where there are no test results for the current user
        return render(request, 'learn/wyniki_testow.html', {})