# from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

# def home(request):
# return render(request, 'screenshot.html')


from django.http import HttpResponse
from django.views.generic.edit import FormView
from .forms import TestForm
 
 
class Test(FormView):
    template_name = "screenshot.html"
    form_class = TestForm
 
    def form_valid(self, form, *args, **kwargs):
        form.save_screenshot()
        return HttpResponse("Screenshot Saved")