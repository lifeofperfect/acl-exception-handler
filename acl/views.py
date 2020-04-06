from django.shortcuts import render, get_object_or_404, redirect
from .models import Alert
import datetime
from django.views.generic import ListView
from .forms import Alert_update_form, SearchForm, CreateUserForm, UpdateFalsePositive, UpdateTruePositive, CreateAlertForm
from .filters import AlertFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .decorators import allowed_users





# Create your views here.

def loginPage(request):
    groups = request.user.groups.all()
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('index')
            

    else:
        messages.info(request, 'Username OR password is incorrect')
        

    template_name = 'registration/login.html'
    context = {
        
    }
    return render(request, template_name, context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@staff_member_required()
@allowed_users(allowed_roles=['camt'])
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():

            user = form.save()
            
            username = form.cleaned_data.get('username') 

            group = Group.objects.get(name='camt')
            user.groups.add(group)
            messages.success(request, "Account was created for " +username)
            return redirect('index')


    template_name = 'alerts/register.html'
    context = {
        'form':form,
        "role_camt":"camt"
    }
    return render(request, template_name, context)


@login_required()
@allowed_users(allowed_roles=['camt'])
def alertUnreactedView(request):
    userOrder = Alert.objects.filter(CAMT_Reveiewer=request.user)
    closedQuery = userOrder.filter(statusCheck='Closed').filter(Date_Regularised__gte=datetime.date.today())
    total_closed_query = closedQuery.count()
    #closedQuery = Alert.objects.filter(Status_REGULARIZED_UNREGULARIZED__in=['3', '1']).filter(Date_Regularised__gte=datetime.date.today())
    

    
    pendingQuery_today = userOrder.filter(statusCheck='Pending').filter(Date_Regularised__gte=datetime.date.today())

    #pendingQuery_today = userOrder.filter(Status_REGULARIZED_UNREGULARIZED__in=['8','7','2']).filter(Date_Regularised__gte=datetime.date.today())
    pending_count = pendingQuery_today.count()
    pending_query = userOrder.filter(statusCheck='Pending')

    #pending_query = userOrder.filter(Status_REGULARIZED_UNREGULARIZED__in=['8','7','2'])

    treated = userOrder.filter(CAMT_Reveiewer=request.user).filter(Date_Regularised__gte=datetime.date.today())
    total_treated = treated.count()
    
    queryset = Alert.objects.exclude(statusCheck__in=['Pending','Closed']).exclude(role='Branch')
    

    myFilter = AlertFilter(request.GET, queryset=queryset)
    queryset = myFilter.qs

    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 500)

    queryset = paginator.get_page(page)

    template_name='alerts/unreacted.html'
    context = {
        'queryset':queryset,
        'myFilter':myFilter,
        'total_closed_query':total_closed_query,
        'pending_count':pending_count,
        'total_treated':total_treated,
        'pending_query':pending_query,
        "role_camt":"camt"
        }

    return render(request, template_name, context)

@login_required()
@allowed_users(allowed_roles=['camt'])
def alertPending(request):
    userOrder = Alert.objects.filter(CAMT_Reveiewer=request.user)
    closedQuery = userOrder.filter(statusCheck='Closed').filter(Date_Regularised__gte=datetime.date.today())
    total_closed_query = closedQuery.count()
    #closedQuery = Alert.objects.filter(statusCheck='Closed').filter(Date_Regularised__gte=datetime.date.today())
    #closedQuery = Alert.objects.filter(Status_REGULARIZED_UNREGULARIZED__in=['3', '1']).filter(Date_Regularised__gte=datetime.date.today())
    #total_closed_query = closedQuery.count()

    userOrder = Alert.objects.filter(CAMT_Reveiewer=request.user)
    pendingQuery = userOrder.filter(statusCheck='Pending').order_by('Date_Regularised')
    
    
    pendingQuery_today = userOrder.filter(statusCheck='Pending').filter(Date_Regularised__gte=datetime.date.today())
    #pendingQuery = userOrder.filter(Status_REGULARIZED_UNREGULARIZED__in=['8','7','2']).order_by('Date_Regularised')

    #pendingQuery_today = userOrder.filter(Status_REGULARIZED_UNREGULARIZED__in=['8','7','2']).filter(Date_Regularised__gte=datetime.date.today())
    pending_count = pendingQuery_today.count()

    treated = userOrder.filter(CAMT_Reveiewer=request.user).filter(Date_Regularised__gte=datetime.date.today())
    total_treated = treated.count()

    template_name = 'alerts/pending.html'
    context = {
        'pendingQuery':pendingQuery,
        'total_closed_query':total_closed_query,
        'pending_count':pending_count,
        'total_treated':total_treated,
        "role_camt":"camt"
        }
    return render(request, template_name, context)


@staff_member_required()
@allowed_users(allowed_roles=['camt'])
def alertClosed_staff(request):
    userOrder = Alert.objects.filter(CAMT_Reveiewer=request.user)
    closedQuery = Alert.objects.filter(camtDecision='TruePositive').filter(statusCheck='Closed').filter(role='camt').filter(Date_Regularised__gte=datetime.date.today()).order_by('Date_Regularised')


    treated = userOrder.filter(CAMT_Reveiewer=request.user).filter(Date_Regularised__gte=datetime.date.today())
    total_treated = treated.count()


    
    pendingQuery_today = userOrder.filter(statusCheck='Pending').filter(Date_Regularised__gte=datetime.date.today())
    pending_count = pendingQuery_today.count()

    #closedQuery = Alert.objects.filter(statusCheck='Closed').filter(Date_Regularised__gte=datetime.date.today())
    #total_closed_query = closedQuery.count()
    userOrder = Alert.objects.filter(CAMT_Reveiewer=request.user)
    closedQuery_count = userOrder.filter(statusCheck='Closed').filter(Date_Regularised__gte=datetime.date.today())
    total_closed_query = closedQuery_count.count()

    pending_query = userOrder.filter(statusCheck='Pending')
    


    template_name='alerts/regularised_staff.html'
    context = {
        'pendingQuery':closedQuery,
        'total_treated':total_treated,
        'pending_count':pending_count,
        'total_closed_query':total_closed_query,
        'pending_query':pending_query,
        "role_camt":"camt"
        }
    return render(request, template_name, context)

@login_required()
@allowed_users(allowed_roles=['camt'])
def alertClosed_user(request):
    userOrder = Alert.objects.filter(CAMT_Reveiewer=request.user)
    closedQuery = userOrder.filter(statusCheck='Closed').filter(camtDecision='TruePositive').filter(Date_Regularised__gte=datetime.date.today())
    #userOrder = Alert.objects.filter(CAMT_Reveiewer=request.user)
    #closedQuery = userOrder.filter(statusCheck='Closed').filter(Date_Regularised__gte=datetime.date.today()).order_by('Date_Regularised')
    total_closed_query = closedQuery.count()


    treated = userOrder.filter(CAMT_Reveiewer=request.user).filter(Date_Regularised__gte=datetime.date.today())
    total_treated = treated.count()

    
    pendingQuery_today = userOrder.filter(statusCheck='Pending').filter(Date_Regularised__gte=datetime.date.today())
    pending_count = pendingQuery_today.count()

    #closedQuery = Alert.objects.filter(statusCheck='Closed').filter(Date_Regularised__gte=datetime.date.today())
    #total_closed_query = closedQuery.count()
    pending_query = userOrder.filter(statusCheck='Pending')


    template_name='alerts/regularised.html'
    context = {
        'pendingQuery':closedQuery,
        'total_treated':total_treated,
        'pending_count':pending_count,
        'total_closed_query':total_closed_query,
        'pending_query':pending_query,
        "role_camt":"camt"
        }
    return render(request, template_name, context)


def alertDetail(request, pk):
    alertDetail = get_object_or_404(Alert, id=pk)

    template_name = 'alerts/alertDetail.html'
    context = {
        'alertDetail':alertDetail
    }
    return render(request, template_name, context)


@login_required()
def acl_update(request, id):
    groups = request.user.groups.all()
    queryset = get_object_or_404(Alert, id=id)
    forms = Alert_update_form(request.POST or None, instance=queryset)
    

    if forms.is_valid():
        queryset.CAMT_Reveiewer = request.user
        queryset.Date_Regularised = datetime.datetime.now()
        queryset.role='camt'
        forms.save()
        messages.success(request, "Successfully treated")
        forms = Alert_update_form()

        if groups:
            role = groups[0].name
            if role == 'camt':
                
                return redirect('unreacted')
            elif role == 'branch':
                
                return redirect('branch_unreact')
            else:
                messages.error(request, 'Error updating Alert')     
    else:
        messages.error(request, 'Error updating Alert')

    template_name ='alerts/updateAlert.html'
    context = {
        'alerts': queryset,
        'forms':forms,
    }
    return render(request, template_name, context)
@login_required()
@allowed_users(allowed_roles=['camt'])
def falseUpdate(request, id):
    queryset = get_object_or_404(Alert, id=id)
    forms = UpdateFalsePositive(request.POST or None, instance=queryset)
    header = "False Positive"

    if forms.is_valid():
        queryset.CAMT_Reveiewer = request.user
        queryset.Date_Regularised = datetime.datetime.now()
        queryset.camtDecision = "FalsePositive"
        queryset.statusCheck = "Closed"
        queryset.role='camt'
        forms.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        forms = UpdateFalsePositive()
        

        

    template_name ='alerts/updateAlert.html'
    context = {
        'alerts': queryset,
        'forms':forms,
        'header':header,
        "role_camt":"camt"
    }

    return render(request, template_name, context)
@login_required()
@allowed_users(allowed_roles=['camt'])
def truePositive(request, id):
    queryset = get_object_or_404(Alert, id=id)
    forms = UpdateTruePositive(request.POST or None, instance=queryset)
    header = "True Positive"

    if forms.is_valid():
        queryset.CAMT_Reveiewer = request.user
        queryset.Date_Regularised = datetime.datetime.now()
        queryset.camtDecision = "TruePositive"
        queryset.role='camt'
        forms.save()
        forms = UpdateTruePositive()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    template_name ='alerts/updateAlert.html'
    context = {
        'alerts': queryset,
        'forms':forms,
        'header':header,
        "role_camt":"camt"
    }

    return render(request, template_name, context)


class SearchListView(ListView):
    template_name = 'alerts/num.html'
    def get_queryset(self, *args, **kwargs):
        qs = Alert.objects.filter(camtDecision='TruePositive').filter(statusCheck='Closed').order_by('-Date_Regularised')
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(Acccount_Number__iexact=query) |
                Q(msisdn__icontains = query)
                )
        #print(self.request.GET)
        return qs
    def get_context_data(self, *args, **kwargs):
        context = super(SearchListView, self).get_context_data(*args,**kwargs)
        #context['obj_list'] = Alert.objects.filter(camtDecision='TruePositive').filter(statusCheck='Closed')
        return context


@login_required()

def create_alert(request):
    form = CreateAlertForm()
    queryset = Alert.objects.all()
    if request.method == 'POST':
        form = CreateAlertForm(request.POST)
        if form.is_valid():
            #form.save(commit=False)
            queryset.role = "Branch"
            form.save()


        return redirect('branch_unreact')
    else:
        form = CreateAlertForm()

    template_name = 'alerts/create_alert.html'
    context = {
        'form':form
    } 

    return render(request, template_name, context)   



@login_required()
def index(request):
    groups = request.user.groups.all()
    
    if groups:
        role = groups[0].name
        if role == 'camt':
            print(role)
            context = {'role_camt':"camt",
            'camt_view':'camt_view'}
        elif role =='branch':
            context = {'role_branch':'branch',
            'branch_view':'branch_view'}
    template_name='index.html'
    return render(request, template_name, context)




