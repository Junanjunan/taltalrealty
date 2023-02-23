from django import forms
from .models import Apartment, Shop, Building


only_number = forms.TextInput(attrs={'oninput': 'this.value = this.value.replace(/[^0-9]/g, "")'})
date_widget = forms.DateInput(attrs={'type': 'date'})


class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'
        widgets = {
            'price': only_number,
            'deposit': only_number,
            'floor': only_number,
            'total_floor': only_number,
            'room': only_number,
            'bath': only_number,
            'owner_phone': only_number,
            'tenant_phone': only_number,
            'birth': date_widget,
        }


class RoomForm(ApartmentForm):
    pass


class OfficetelForm(ApartmentForm):
    pass


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'
        widgets = {
            'price': only_number,
            'deposit': only_number,
            'floor': only_number,
            'total_floor': only_number,
            'owner_phone': only_number,
            'tenant_phone': only_number,
            'birth': date_widget,
        }
        
        
class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = '__all__'
        widgets = {
            'price': only_number,
            'deposit': only_number,
            'total_floor': only_number,
            'under_floor': only_number,
            'owner_phone': only_number,
            'parking_number': only_number,
            'birth': date_widget,
        }