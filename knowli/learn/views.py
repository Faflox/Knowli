from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from learn.models import MathTest, MathTask, Score
from learn.forms import MathTaskForm

# Create your views here.
def Index(request):
    return render(request, 'learn/index.html')

@login_required
def test_list(request, level):
    tests = MathTest.objects.filter(level=level)
    context = {
        'tests': tests,
        'level': level
    }
    return render(request, 'tests_temps/test_list.html', context)

@login_required
def take_test(request, slug):
    test = get_object_or_404(MathTest, slug=slug)
    tasks = MathTask.objects.filter(test=test)
    current_user = request.user

    if request.method == 'POST':
        total_score = 0

        for task in tasks:
            user_choice = request.POST.get(f'task_{task.id}')
            if user_choice == task.correct_choice:
                total_score += 1

        existing_score = Score.objects.filter(user=current_user, test=test).first()
        
        if existing_score is None or total_score > existing_score.score:
            if existing_score:
                existing_score.delete() 
            Score.objects.create(user=current_user, test=test, score=total_score)
            
        highest_score = Score.objects.filter(user=current_user, test=test).order_by('-score').first()

        return render(request, 'tests_temps/test_completed.html', {'test': test, 'score': total_score, 'highest_score': highest_score})

    else:
        task_forms = [MathTaskForm(instance=task) for task in tasks]
        context = {
            'test': test,
            'task_forms': task_forms,
        }
        return render(request, 'tests_temps/take_test.html', context)


