from django import forms
from crispy_forms.helper import FormHelper
import re
import base64


class TestForm(forms.Form):
    """
    Form to upload the screenshot of a webpage
    """

    image_data = forms.CharField(widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = "agreement_form"
        self.helper.form_method = 'post'

        super(TestForm, self).__init__(*args, **kwargs)
    
    def save_screenshot(self):
        dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
        image_data = self.cleaned_data['image_data']
        image_data = dataUrlPattern.match(image_data).group(2)
        image_data = image_data.encode()
        image_data = base64.b64decode(image_data)
 
        with open('name.jpg', 'wb') as f:
            f.write(image_data)