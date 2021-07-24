from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
class RegisterForm(UserCreationForm): #상속을 해준다.상속이라는 것은 유저크리에이션에 있는 내용도 사용할 수 있기 때문에
    class Meta:
        model = CustomUser
        fields = ['username','password1', 'password2','nickname', 'location', 'university']