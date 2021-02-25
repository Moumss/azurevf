from okta_oauth2.decorators import okta_login_required

@okta_login_required
def decorated_view(request):
    return HttpResponse("i am a protected view")