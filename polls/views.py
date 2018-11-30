from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from polls.forms import *
from .models import *
from django.db import connection
from .classes import *
from django.contrib.auth.decorators import login_required


def add_person(request):
    form = NameForm()
    # A HTTP POST?
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():

            # Have we been provided with a valid form?
            form.save(commit=True)
            return render(request, 'homepage.html', {'names': PersonName.objects.all()})
        # Now that the category is saved
        # We could give a confirmation message
        # But since the most recent category added is on the index page
        # Then we can direct the user back to the index page.
        else:
            print(form.errors)

    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'add_category.html', {'form': form})


def djangoregister(request):
    if request.method == 'POST':
        info = request.POST.dict()
        user, created = User.objects.get_or_create(username=info['username'])
        # user = User(username=info['username'], password=info['pwd'])
        if created:
            user.set_password(info['pwd'])
            user.save()
            login(request, user)
            return redirect('/polls/')
    return render(request, 'register.html')


def djangologin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/polls/')
        else:
            return render(request, 'login.html', {'error': True})
    return render(request, 'login.html', {'error': False})


def ajax_game(request):
    # print("hello", request.POST['rating'])
    if request.POST['authenticated'] == 'True':
        update_gamerating(request.POST['uid'], request.POST['gid'], request.POST['rating'])


def ajax_book(request):
    if request.POST['authenticated2'] == 'True':
        update_bookrating(request.POST['uid'], request.POST['bid'], request.POST['rating'])


def ajax_movies(request):
    if request.POST['authenticated3'] == 'True':
        update_movierating(request.POST['uid'], request.POST['mid'], request.POST['rating'])


def update_bookrating(uid, bid, rating):
    nid = 0
    with connection.cursor() as cursor:
        cursor.execute("Select * from bookrating where userid= %s and bookid=%s", [uid, bid])
        if cursor.fetchone() is None:
            cursor.execute("Insert into bookrating values (%s,%s,%s,%s)", [nid, uid, bid, rating])
        else:
            cursor.execute("update bookrating set rating = %s where userid= %s and bookid= %s", [rating, uid, bid])


def update_movierating(uid, mid, rating):
    nid = 0
    with connection.cursor() as cursor:
        cursor.execute("Select * from movierating where userid= %s and movieid=%s", [uid, mid])
        if cursor.fetchone() is None:
            cursor.execute("Insert into movierating values (%s,%s,%s,%s)", [nid, uid, mid, rating])
        else:
            cursor.execute("update movierating set rating = %s where userid= %s and movieid= %s", [rating, uid, mid])


def comment(request):
    pass


def djangologout(request):
    logout(request)
    return redirect('/polls/')


def update_gamerating(uid, gid, rating):
    nid = 0
    with connection.cursor() as cursor:
        cursor.execute("Select * from gamerating where userid= %s and gameid=%s", [uid, gid])
        if cursor.fetchone() is None:
            cursor.execute("Insert into gamerating values (%s,%s,%s,%s)", [nid, uid, gid, rating])
        else:
            cursor.execute("update gamerating set rating = %s where userid= %s and gameid= %s", [rating, uid, gid])


#
# def login(request):
#     form = RegForm()
#     if request.method == 'POST':
#         form = RegForm(request.POST)
#         if form.is_valid():
#             un, p = form.cleaned_data['username'], form.cleaned_data['pwd']
#             if un is 'exception':
#                 raise Exception('This is exception')
#
#             if len(Register.objects.all().filter(username=un, pwd=p)) != 0:
#                 return HttpResponse('YAY LOGEED IN')
#             else:
#                 return HttpResponse("BOO NOT LOGGED IN")
#         else:
#             print(form.errors)
#     return render(request, 'login.html')
#

def index(request):
    return render(request, 'my_home.html')


def allgames(request):
    obj = GameItem.objects.all()
    obj = sorted(obj, key=lambda x: x.game_rating, reverse=True)
    im = Image.objects.all()
    d = {}
    lst = []
    for i in im:
        d[i.image_name] = i.image_path
    for i in obj:
        if i.game_name in d:
            s = GameImage(i, d[i.game_name])
        else:
            pt = google(i.game_name)
            s = GameImage(i, pt)
            Image.objects.create(image_name=i.game_name, image_path=pt)
        lst.append(s)
    return render(request, 'boot.html', {'games': lst})


def allbooks(request):
    obj = BookItem.objects.all()
    obj = sorted(obj, key=lambda x: x.book_rating, reverse=True)
    im = Image.objects.all()
    d = {}
    lst = []
    for i in im:
        d[i.image_name] = i.image_path
    for i in obj:
        if i.book_name in d:
            s = BookImage(i, d[i.book_name])
        else:
            pt = google(i.book_name)
            s = BookImage(i, pt)
            Image.objects.create(image_name=i.book_name, image_path=pt)
        lst.append(s)
    return render(request, 'boot2.html', {'books': lst})


def allmovies(request):
    obj = MovieItem.objects.all()
    obj = sorted(obj, key=lambda x: x.movie_rating, reverse=True)
    im = Image.objects.all()
    d = {}
    lst = []
    for i in im:
        d[i.image_name] = i.image_path
    for i in obj:
        if i.movie_name in d:
            s = MovieImage(i, d[i.movie_name])
        else:
            pt = google(i.movie_name)
            s = MovieImage(i, pt)
            Image.objects.create(image_name=i.movie_name, image_path=pt)
        lst.append(s)
    return render(request, 'boot3.html', {'movies': lst})


@login_required(login_url='/polls/login')
def add_game(request):
    form = AddGame()
    if request.method == 'POST':
        form = AddGame(request.POST)
        if form.is_valid():
            # rating, id = form.cleaned_data['game_rating'], form.cleaned_data['id']
            # with connection.curson() as cursor:
            #    cursor.execute('insert into gamerating values(1,%s,%s,%s)', [200, id, rating])
            game = form.save(commit=False)
            game.gameid = 1
            game.save()
            return redirect('/polls/all_games')

        else:
            print(form.errors)
        return
    return render(request, 'form_game.html')


@login_required(login_url='/polls/login')
def add_book(request):
    form = AddBook()
    if request.method == 'POST' :
        form = AddBook(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.bookid = 1
            book.save()
            return redirect('/polls/all_books')

        else:
            print(form.errors)
        return
    return render(request, 'form_book.html')


@login_required(login_url='/polls/login')
def add_movie(request):
    form = AddMovie()
    if request.method == 'POST':
        form = AddMovie(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.movieid = 1
            movie.save()
            return redirect('/polls/all_movies')

        else:
            print(form.errors)
        return
    return render(request, 'form_movie.html')


def google(arg):
    from google_images_download import google_images_download  # importing the library

    response = google_images_download.googleimagesdownload()  # class instantiation

    arguments = {"output_directory": "C://Users//TAIYAB//PycharmProjects//untitled1//polls//static//downloaded",
                 "keywords": arg + " high resolution", "limit": 1, "print_urls": False,
                 "print_paths": False}  # creating list of arguments
    paths = response.download(arguments)  # passing the arguments to the function
    st = paths[arg + " high resolution"][0]
    st = st[st.find('downloaded'):]
    st = st.replace('\\', '\\\\')
    return st
