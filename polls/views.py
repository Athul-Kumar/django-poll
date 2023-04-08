from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.urls import reverse
# Create your views here.
from django.db.models import F
from django.views import generic
from django.utils import timezone

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list' : latest_question_list,
#     }
#     return render (request,'polls/index.html',context )


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
        ]



# def detail(request, question_id):

#     try:
#         question = Question.objects.get(pk=question_id)
#         # print(question)

#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
    
#     return render(request, 'polls/details.html',{'question':question})


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/details.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/details.html', {'question': question})
    

# def results(request, question_id):
#     question =get_object_or_404(Question, pk = question_id)
#     print(question)
#     return render(request, 'polls/results.html', {'question': question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"




def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:

        selected_choice = question.choice_set.get(pk=request.POST["choice"])

    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/details.html",
            {
                "question":question,
                "error_message": "you didn't select a choice ",
            },


        )

    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()


    return HttpResponseRedirect(reverse("polls:results",args=(question.id,)))