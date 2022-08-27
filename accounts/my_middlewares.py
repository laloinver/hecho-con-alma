from accounts.models import Statistics


class VisitCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.method == 'GET':
            statistic_object, created = Statistics.objects.get_or_create(id=1)
            statistic_object.number_of_visits += 1
            statistic_object.save()
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        return response
