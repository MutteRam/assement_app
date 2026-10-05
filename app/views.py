from django.shortcuts import render
from django.http import JsonResponse
from .models import CodingQuestion
from .run_code import execute_code


def home(request):
    return render(request, "home.html")


def assessment(request):
    questions = CodingQuestion.objects.filter(is_active=True)

    for question in questions:
        question.visible_examples = question.test_cases.filter(
            is_hidden=False
        )[:2]

    return render(request, "assessment.html", {
        "questions": questions
    })


def run_code(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"}, status=400)

    code = request.POST.get("code", "")
    question_id = request.POST.get("question_id")

    if not code.strip():
        return JsonResponse({"error": "Write code first."})

    try:
        question = CodingQuestion.objects.get(id=question_id)

        results = execute_code(
            code,
            question.test_cases.all()
        )

        correct = all(result["passed"] for result in results)

        return JsonResponse({
            "correct": correct,
            "results": results
        })

    except Exception as e:
        return JsonResponse({
            "error": str(e)
        }, status=500)

