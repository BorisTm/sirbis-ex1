from django.shortcuts import render, redirect

from .models import Greeting
from .models import TodoList, Category


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


# def index(request):
#     # r = requests.get('http://httpbin.org/status/418')
#     # print(r.text)
#     # return HttpResponse('<pre>' + r.text + '</pre>')
#     times = int(os.environ.get('TIMES',3))
#     return HttpResponse('Hello! ' * times)

def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


def base(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "base.html")


def bulb(request):
    return render(request, "bulb.html")


def google_map_location(request):
    return render(request, "google_map_location.html")


def osm_leaf_map(request):
    return render(request, "osm_leaf_map.html")


def simple_todo(request):
    todos = TodoList.objects.all() #quering all todos with the object manager
    categories = Category.objects.all() #getting all categories with object manager

    if request.method == "GET":
        return render(request, "simple_todo.html", {"todos": todos, "categories":categories})
    if request.method == "POST":
        if "taskAdd" in request.POST: #checking if there is a request to add a todo
            title = request.POST["description"] #title
            due_date = str(request.POST["dueDate"]) #date
            category = request.POST["category_select"] #category
            content = title + " -- " + due_date + " " + category #content
            todo = TodoList(title=title, content=content, due_date=due_date, category=Category.objects.get(name=category))
            todo.save() #saving the todo
            return redirect("/simple_todo/") #reloading the page
        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedId = int(request.POST["hiddenId"]) #checked todo to be deleted
            if checkedId == "unknown":
                return redirect("/simple_todo/")
            todo = todos.get(id=checkedId)
            todo.delete() #deleting todo
            return redirect("/simple_todo/")
        if "taskComplete" in request.POST:
            completedId = int(request.POST["hiddenId"])
            if completedId == "unknown":
                return redirect("/simple_todo/")
            todo = todos.get(id=completedId)
            completed = request.POST["hiddenCompleted"]
            todo.completed = completed == 'True'
            todo.save(force_update=True)
            return redirect("/simple_todo/")
        if "taskUpdate" in request.POST:
            checkedId = int(request.POST["hiddenId"]) #checked todo to be deleted
            if checkedId == "unknown":
                return redirect("/simple_todo/")
            todo = todos.get(id=checkedId)
            todo.title = request.POST["description"]
            todo.due_date = str(request.POST["dueDate"])
            category = request.POST["category_select"]
            todo.category=Category.objects.get(name=category)
            todo.content = todo.title + " -- " + todo.due_date + " " + category
            todo.save(force_update=True)  # saving the todo
            return redirect("/simple_todo/")
