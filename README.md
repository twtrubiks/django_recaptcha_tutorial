# django-recaptcha-tutorial 📝

今天要教大家使用 [Django](https://github.com/django/django) 結合 [Google's reCAPTCHA](https://developers.google.com/recaptcha/) :smile:

* [Youtube Tutorial](https://youtu.be/nxPY0F59sjM)

建議對 [Django](https://github.com/django/django) 不熟悉的朋友，可以先觀看我之前寫的文章（ 進入 [Django](https://github.com/django/django)  的世界）

* [Django 基本教學 - 從無到有 Django-Beginners-Guide](https://github.com/twtrubiks/django-tutorial)

* [使用 Django 實現一個可以使用社交平台登入並且註冊的網站](https://github.com/twtrubiks/django_social_login_tutorial)

* [使用 Django 建立一個簡易版購物網站](https://github.com/twtrubiks/django-shop-tutorial)

## 前言

相信大家一定有常常輸入驗證碼的經驗，為什麼要用驗證碼呢:question:這樣做不是對使用者而言非常麻煩 :confused:

，使用者登入一次就要輸入一次驗證碼，回覆一篇文章也要驗證碼，使用者一定覺得麻煩死了 :angry:

 不過，我們換個角度思考，其實這是在保護網站避免表單被惡意攻擊，或是被爬蟲機器人瘋狂撈資料等等......

目前最常用的，就是 google 的驗證碼，所以，今天我要教大家如何透過 [Django](https://github.com/django/django) 使用 Google's reCAPTCHA :grinning:

## 教學

透過 [django-recaptcha](https://github.com/praekelt/django-recaptcha) 完成 Google's reCAPTCHA，

安裝，請在 cmd ( 命令提示字元 ) 輸入以下指令，

```python
pip install django-recaptcha
```

也可以直接安裝 requirements.txt，因為我有用到其他的 Package

```python
pip install -r requirements.txt
```

接著請將 captcha 加入 [settings.py](https://github.com/twtrubiks/django_recaptcha_tutorial/blob/master/django_recaptcha_tutorial/settings.py) 裡的 INSTALLED_APPS

```python
INSTALLED_APPS = [
    ......
    'captcha',
]
```

到這邊我們先停下來，先去 reCAPTCHA admin [https://www.google.com/recaptcha/admin](https://www.google.com/recaptcha/admin) 註冊

(這邊可以選 v3)

![](https://i.imgur.com/10ykpjB.png)

如果要和我一樣在本地端測試，Domains 打 127.0.0.1 即可，

接下來，請將你的 key 設定到 [settings.py](https://github.com/twtrubiks/django_recaptcha_tutorial/blob/master/django_recaptcha_tutorial/settings.py) 裡面

![](https://i.imgur.com/B9M4h31.png)

```python
RECAPTCHA_PUBLIC_KEY = 'Your Captcha_Public_Key'
RECAPTCHA_PRIVATE_KEY = 'Your Captcha_Private_Key'
```

使用的方法也很簡單，直接在 [forms.py](https://github.com/twtrubiks/django_recaptcha_tutorial/blob/master/comments/forms.py) 裡面加上 `ReCaptchaField` field  即可

```python
......

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

......
```

(這邊我把各種 reCAPTCHA 類型 的都註解起來, 大家可以自行嘗試, 要注意版本)

前端 render 的部份也很簡單，底下有加上 bootstrap

```python
<form action="/comments/" method="post">
        {% csrf_token %}
        {% bootstrap_form form %}
        {% buttons %}
            <button type="submit" class="btn btn-success btn-product">
                <i class="fa fa-check" aria-hidden="true"></i> POST
            </button>
        {% endbuttons %}
</form>
```

假如你想要使用  new No CAPTCHA reCAPTCHA，請在  [settings.py](https://github.com/twtrubiks/django_recaptcha_tutorial/blob/master/django_recaptcha_tutorial/settings.py) 裡增加

```python
NOCAPTCHA = True
```

有些人可能不懂這是什麼，先試著回想以前我們在輸入驗證碼的時候，是不是都曾經看過

連我看了都怕的驗證碼:fearful:，像是這樣

`NOCAPTCHA = False`

![](https://i.imgur.com/0l1xPGC.png)

現在 google 提供更方便的方法，我們直接點一下即可，是不是方便很多:blush:

`NOCAPTCHA = True`

![](https://i.imgur.com/6oy7HCn.png)

## 執行畫面

直接瀏覽 [http://127.0.0.1:8000/comments/](http://127.0.0.1:8000/comments/)

![](https://i.imgur.com/7v0lCnr.png)

相信大部分的使用者都很懶，甚至連點都不想點一下，

所以 google 又增加了 Invisible reCAPTCHA

[https://developers.google.com/recaptcha/docs/invisible](https://developers.google.com/recaptcha/docs/invisible)

可以讓點擊一下的這個動作被原本的 submit 送出，

簡單講，就是在背景幫你處理，

對使用者來說，也不用點擊額外的按鈕(操作),

是不是超級貼心:laughing:

但如果你仔細看, 它其實有把資訊放在 console log 中,

![](https://i.imgur.com/WIkYRLQ.png)

## 後記

整體操作完，相信大家應該覺得不難，蠻好上手的，透過 Google's reCAPTCHA 我們可以解決像

是前面所說的各種攻擊，也可以用來減輕表單頁面上的暴力攻擊，剩下的 Invisible reCAPTCHA 就

留給大家研究 :stuck_out_tongue_closed_eyes:

## 執行環境

* Python 3.8

## Reference

* [Django](https://www.djangoproject.com/)
* [django-recaptcha](https://github.com/praekelt/django-recaptcha)
* [google-recaptcha](https://www.google.com/recaptcha/intro/android.html)

## License

MIT licens
