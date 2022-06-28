from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible, ReCaptchaV2Checkbox, ReCaptchaV3
from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=20)
    text = forms.CharField(required=True, max_length=200)

    # captcha = ReCaptchaField()

    # captcha = ReCaptchaField(
    #     widget=ReCaptchaV2Checkbox(
    #         attrs={
    #             # 'data-theme': 'dark',
    #             "data-size": "compact",
    #         }
    #     )
    # )
    # captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)

    captcha = ReCaptchaField(
        widget=ReCaptchaV3(
            attrs={
                "required_score": 0.85,
            }
        )
    )

    class Meta:
        model = Comment
        fields = ("name", "text", "captcha")
