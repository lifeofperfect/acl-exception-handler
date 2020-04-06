from django.shortcuts import render, redirect
from acl.models import Alert
from django.contrib.auth.decorators import login_required
from .forms import CreateAlertForm
from django.http import Http404
import datetime
from acl.decorators import allowed_users
# Create your views here.


@login_required()
@allowed_users(allowed_roles=['branch'])
def create_alert(request):
    form = CreateAlertForm()
    if request.method == 'POST':
        form = CreateAlertForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.CAMT_Reveiewer = request.user
            instance.role = "Branch"
            instance.save()

        return redirect('branch_unreact')
    else:
        form = CreateAlertForm()

    template_name = 'branch/create_alert.html'
    context = {
        'form':form,
        'branch_view':'branch_view',
        'role_branch':'branch'
    } 

    return render(request, template_name, context) 


@login_required()   
@allowed_users(allowed_roles=['branch'])
def branch_unreact(request):
    
    #list of all treated alert
    alerts = Alert.objects.filter(CAMT_Reveiewer=request.user)
    
    #status bar 
    userOrder = Alert.objects.filter(CAMT_Reveiewer=request.user) #all alert relating to a user
    closedQuery = userOrder.filter(statusCheck='Closed').filter(Date_Regularised__gte=datetime.date.today()) #all closed query for the day
    total_closed_query = closedQuery.count() #total count or number of closed query for the day

    pendingQuery_today = userOrder.filter(statusCheck='Pending').filter(Date_Regularised__gte=datetime.date.today()) #all alerts that are pending from a user
    pending_count = pendingQuery_today.count() #total number of pending query for the day

    treated = userOrder.filter(CAMT_Reveiewer=request.user).filter(Date_Regularised__gte=datetime.date.today()) #all alerts treated by a particular user
    total_treated = treated.count() #total count of treated alert

    pending_query = userOrder.filter(statusCheck='Pending').count()

    groups = request.user.groups.all()


    template_name = 'branch/branch_unreact.html'
    context = {
        'alerts':alerts,
        'total_treated':total_treated,
        'pending_count':pending_count,
        'total_closed_query':total_closed_query,
        'branch_view':'branch_view',
        'react':'react',
        'pending_query':pending_query,
        'role_branch':'branch'

    }
    return render(request, template_name, context)


@login_required()
@allowed_users(allowed_roles=['branch'])
def branch_alertPending(request):
    userOrder = Alert.objects.filter(CAMT_Reveiewer=request.user)
    closedQuery = userOrder.filter(statusCheck='Closed').filter(Date_Regularised__gte=datetime.date.today())
    total_closed_query = closedQuery.count()
    userOrder = Alert.objects.filter(CAMT_Reveiewer=request.user)
    pendingQuery = userOrder.filter(statusCheck='Pending').order_by('Date_Regularised')
    
    
    pendingQuery_today = userOrder.filter(statusCheck='Pending').filter(Date_Regularised__gte=datetime.date.today())
    pending_count = pendingQuery_today.count()

    treated = userOrder.filter(CAMT_Reveiewer=request.user).filter(Date_Regularised__gte=datetime.date.today())
    total_treated = treated.count()


    template_name = 'branch/branch_pending.html'
    context = {
        'pendingQuery':pendingQuery,
        'total_closed_query':total_closed_query,
        'pending_count':pending_count,
        'total_treated':total_treated,
        'branch_view':'branch',
        'pending':'pending',
        'role_branch':'branch'
        
        }
    return render(request, template_name, context)

@login_required()
@allowed_users(allowed_roles=['branch'])
def branch_alertClosed_user(request):
    userOrder = Alert.objects.filter(CAMT_Reveiewer=request.user)
    closedQuery_alert = userOrder.filter(statusCheck='Closed')

    closedQuery = userOrder.filter(statusCheck='Closed').filter(Date_Regularised__gte=datetime.date.today()) 
    total_closed_query = closedQuery.count()

    pendingQuery_today = userOrder.filter(statusCheck='Pending').filter(Date_Regularised__gte=datetime.date.today())  
    pending_count = pendingQuery_today.count()

    treated = userOrder.filter(CAMT_Reveiewer=request.user).filter(Date_Regularised__gte=datetime.date.today()) 
    total_treated = treated.count()

    pending_query = userOrder.filter(statusCheck='Pending').count()
    

    
    template_name='branch/branch_regularised.html'
    context = {
        'pendingQuery':closedQuery_alert,
        'total_treated':total_treated,
        'pending_count':pending_count,
        'total_closed_query':total_closed_query,
        'branch_view':'branch',
        'pending_query':pending_query,
        'closed':'closed',
        'role_branch':'branch'
        }
    return render(request, template_name, context)