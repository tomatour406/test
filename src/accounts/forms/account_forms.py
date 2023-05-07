from django import forms
from ..models import Profile
from bootstrap_datepicker_plus.widgets import DatePickerInput

class ProfileUpdateForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs.update({"class":"form-control"})
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = Profile
        exclude = ["user"]
        
    birthday = forms.DateField(
        label="誕生日",
        widget=DatePickerInput(format='%Y-%m-%d')
    )
    
    date = forms.DateField(
        label="作成日",
        widget=DatePickerInput(format='%Y-%m-%d')
    )
    
    #以下を追記
    def clean_username(self):
        username = self.cleaned_data.get("username")
        user_email = self.instance.user.email
        if username == user_email:
            raise forms.ValidationError("ユーザー名を変更してください")
        elif "@" in username:
            raise forms.ValidationError("ユーザー名にEメールアドレスは使用できません")
        return username