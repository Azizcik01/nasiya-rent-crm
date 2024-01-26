from django.forms import ModelForm
from core.models.cars import Car, Category, Brand, Arenda
from core.models.auth import User
from core.models.monitoring import Card



class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'

class CtgForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ArendForm(ModelForm):
    class Meta:
        model = Arenda
        fields = ['pay_type']



