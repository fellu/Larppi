
def ip_address_processor(request):
    return {'ip_address': request.META['REMOTE_ADDR']}

def logged_user_processor(request):
    user = request.user
    return { 'logged_user': user }
