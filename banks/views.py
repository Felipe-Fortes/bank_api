from django.http import JsonResponse
from .models import Bank
from django.shortcuts import render

def home(request):
    banks = Bank.objects.all()
    bank_data = [bank.to_dict() for bank in banks]
    context = {'bank_data': bank_data}
    return render(request, 'bank_list.html', context)

def show_bank(request, bank_id):
    try:
        bank = Bank.objects.get(pk=bank_id)
    except Bank.DoesNotExist:
        return render(request, 'error_page.html', {'error': 'Bank not found'})
    context = {'bank': bank}
    return render(request, 'code_parameter.html', context)


