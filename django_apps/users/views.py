import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import auth
from .models import User
from .github_login import GH_AUTHORIZE_URL, GH_LOGIN_BASE_URL, GH_ID_LOCAL, GH_SECRET_LOCAL, GH_OATH_API_URL


def add_header(view_func):  # ChatGPT example
    def wrapper(request, *args, **kwargs):
        response = view_func(request, *args, **kwargs)
        response['X-Header'] = 'My custom header'
        response['Custom-Header'] = 'It is my own'
        return response
    return wrapper


def loggedout_only_view(view_func): # My own example
    def wrapper(request):
        if request.user.is_authenticated:
            return JsonResponse({"status":"This page is only logged_out view"})
        else:
            response = view_func(request)
            return response
    return wrapper


@add_header
@loggedout_only_view
def login(request):
    return render(request, 'users/login.html')


def github_login(request):
    return redirect(GH_AUTHORIZE_URL)


def github_callback(request):
    code = request.GET.get("code")
    if code is None:
        return JsonResponse(request.GET)
    result = requests.post(
        f"{GH_LOGIN_BASE_URL}/access_token?client_id={GH_ID_LOCAL}&client_secret={GH_SECRET_LOCAL}&code={code}",
        headers={"Accept": "application/json"}
    )
    if result.status_code != 200:
        return JsonResponse({"status": "call back fail"})
    result_json = result.json()
    access_token = result_json.get("access_token")
    profile_request = requests.get(
        GH_OATH_API_URL,
        headers={
            "Authorization": f"token {access_token}",
            "Accept": "application/json"
        }
    )
    profile_json = profile_request.json()
    github_id = profile_json.get("login")
    if profile_json.get("message"):
        return JsonResponse(profile_json)
    user = User.objects.filter(username=github_id, login_method="Github").first()
    if user is None:
        user = User.objects.create(
            username = github_id,
            email = profile_json.get('email'),
            login_method = 'github'
        )
        user.set_unusable_password()
        user.save()
    auth.login(request, user)
    return redirect('/')