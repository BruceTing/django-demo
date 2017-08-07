from django.http import HttpResponseRedirect
import logging

# logger = logging.getLogger('common_logger')

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # logger.info('simple middleware is called...')
        response = self.get_response(request)
        # logger.info(response)
        # logger.info('simple middleware is called end.')
        return response
