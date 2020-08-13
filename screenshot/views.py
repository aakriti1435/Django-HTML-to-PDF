from django.shortcuts import render
from django.http import HttpResponse
import pyautogui
from .models import digi_sign
from PIL import ImageGrab

# Create your views here.

def canvas(request):
    return render(request, 'canvas.html')


def take_screenshot(request):
    screenshot = pyautogui.screenshot()
    # ss_save = digi_sign(digital_sign = screenshot)
    # screenshot.save("C:/Users/aakri/OneDrive/Desktop/Django/HTML to PDF/html_to_pdf/static/signatures_complainant/sign1.png")
    # ss_save.save()
    
    image = ImageGrab.grab(bbox=(30,155,640,520))  #left top right bottom
    image.save("C:/Users/aakri/OneDrive/Desktop/Django/HTML to PDF/html_to_pdf/static/signatures_complainant/sign1.png")


    # print(screenshot)
    return HttpResponse('saved')