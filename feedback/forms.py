from django import forms
from feedback.tasks import send_feedback_email_task
from feedback.tasks import download_mp3_task


class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    link = forms.CharField(
        label="Youtube link", widget=forms.Textarea(attrs={'rows': 5}))
    honeypot = forms.CharField(widget=forms.HiddenInput(), required=False)

    def send_email(self):
        # try to trick spammers by checking whether the honeypot field is
        # filled in; not super complicated/effective but it works
        if self.cleaned_data['honeypot']:
            return False
        send_feedback_email_task.delay(
            self.cleaned_data['email'], self.cleaned_data['link'])
    
    def download_mp3(self):
         download_mp3_task.delay(
             self.cleaned_data['link']
         )

