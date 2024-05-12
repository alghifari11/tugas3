from django.shortcuts import render

def item_list(request):
    items = ['Item 1', 'Item 2', 'Item 3']  # Contoh daftar item
    return render(request, 'myapp/list.html', {'items': items})
