from django.shortcuts import render, redirect
from .models import Category, Flashcard
from django.contrib.messages import constants
from django.contrib import messages

def new_flashcard(request):
    if not request.user.is_authenticated:
        return redirect('/users/login')
    
    if request.method == 'GET':
        categories = Category.objects.all()
        difficulties = Flashcard.DIFFICULTY_CHOICES
        flashcards = Flashcard.objects.filter(user = request.user)

        category_filter = request.GET.get('category')
        difficulty_filter = request.GET.get('difficulty')

        if category_filter:
            flashcards = flashcards.filter(category__id = category_filter)

        if difficulty_filter:
            flashcards = flashcards.filter(difficulty = difficulty_filter)

        return render(request, 'new_flashcard.html', {'categories': categories, 'difficulties': difficulties, 'flashcards': flashcards})

    elif request.method == 'POST':
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        category = request.POST.get('category')
        difficulty = request.POST.get('difficulty')

        if len(question.strip()) == 0 or len(answer.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Fill both Question and Answer fields.')
            return redirect('/flashcard/new_flashcard/')
        
        flashcard = Flashcard(
            user = request.user,
            question = question,
            answer = answer,
            category_id = category,
            difficulty = difficulty,
        )

        flashcard.save()

        messages.add_message(request, constants.SUCCESS, 'Flashcard registered with Success!')
        return redirect('/flashcard/new_flashcard')