from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View
from app.utils import render_to_pdf
# Create your views here.



class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('index.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('index.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

# download the file by typing in url ../?download=true