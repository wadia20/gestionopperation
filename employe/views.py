from .models import *
from django.contrib import auth
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .form import *
from employe.models import Client,Operation

from django.views import View
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa

# home page
def home(request):
    return render(request, "home.html")

def base(request):
    return render(request, "dashboard.html")

#login page 
def login_employe(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("employe:base")
        else:
            messages.warning(request, 'something went wrong')
            return redirect('employe:login')
    return render(request,'login.html')

#add client
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from .models import Client

def ADD_CLIENT(request):
    if request.method == 'POST':
        id = request.POST.get('client_id')
        name = request.POST.get('client_name')
        birth = request.POST.get('client_birth')
        phone = request.POST.get('client_phone')
        email = request.POST.get('client_email')
        gender = request.POST.get('client_gender')
        address = request.POST.get('client_Address')

        if not all([id, name, birth, phone, email, gender, address]):
            messages.error(request, 'All fields are required.')
            return render(request, 'client/add_client.html')

        client = Client(
            client_id=id,
            client_Name=name,
            Date_Of_Birth=birth,
            Phone=phone,
            Email=email,
            Gender=gender,
            Address=address,
        )

        try:
            client.save()
            messages.success(request, 'Client added successfully!')
            return redirect('employe:add_client')
        except IntegrityError:
            messages.error(request, 'Client ID already exists.')
            return render(request, 'client/add_client.html')

    return render(request, 'client/add_client.html')



#add operation
from django.shortcuts import render, redirect


from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib import messages
from .form import OperationForm
from django.views.generic import ListView

def ADD_OPERATION(request):
    if request.method == 'POST':
        form = OperationForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Operation added successfully!')
                return redirect('employe:add_operation')
        except IntegrityError:
            messages.error(request, 'Operation ID already exists.')
            return render(request, 'client/add_operation.html', {'form': form})
    else:
        form = OperationForm()  # Ensure form is initialized for GET request

    return render(request, 'client/add_operation.html', {'form': form})


from django.views.generic import ListView
#showing list of operations

from django.shortcuts import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
class OperationListView(ListView):
    model = Operation
    template_name = 'client/operation_list.html'
    context_object_name = 'operations'

def operation_list_pdf(request):
    query = request.GET.get('query')
    if query:
        operations = Operation.objects.filter(client_id__icontains=query)
    else:
        operations = Operation.objects.all()
    
    template_path = 'client/operation_list_pdf.html'
    context = {'operations': operations}
    template = get_template(template_path)
    html = template.render(context)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="operations_{query}.pdf"'
    
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
    return response
# afficher les cients avec leurs operations

from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Client, Operation

class Clients_show(View):
    def get(self, request):
        clients = Client.objects.all()
        for client in clients:
            operations_count = Operation.objects.filter(client_id=client.client_id).count()
            client.operations_count = operations_count
            client.operations = Operation.objects.filter(client_id=client.client_id)

        context = {
            'clients': clients
        }
        return render(request, 'client/show_client.html', context)

def search_clients(request):
    query = request.GET.get('query', '').strip()
    clients = Client.objects.filter(client_id=query) if query else Client.objects.none()
    for client in clients:
        operations_count = Operation.objects.filter(client_id=client.client_id).count()
        client.operations_count = operations_count
        client.operations = Operation.objects.filter(client_id=client.client_id)

    context = {
        'clients': clients,
        'query': query
    }
    return render(request, 'client/show_client.html', context)

#pdf

from django.shortcuts import get_object_or_404, HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Operation

def Generate_pdf(request, client_id, operation_id):
    client = get_object_or_404(Client, client_id=client_id)
    operation = get_object_or_404(Operation, id=operation_id, client_id=client_id)
    filename = request.GET.get('filename', 'default_filename.pdf')  # Retrieve filename from query string

    template_path = 'pdf_template.html'
    context = {
        'client': client,
        'operations': [operation],  # Pass only the selected operation
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    template = get_template(template_path)
    html = template.render(context)

    # Create PDF
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

#recherche d'operarion
from django.shortcuts import render
from .models import Operation

def search_operations(request):
    query = request.GET.get('query')
    if query:
        operations = Operation.objects.filter(client_id__icontains=query)
    else:
        operations = Operation.objects.all()
    return render(request, 'client/operation_list.html', {'operations': operations})

from django.views.generic.base import TemplateView


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operations'] = Operation.objects.order_by('-operation_date')[:5]
        context['employees'] = Employee.objects.all()
        return context

    
