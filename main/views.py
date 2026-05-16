from django.shortcuts import render,redirect
from .models import Register,BloodDonation,BloodRequest
from django.contrib import messages
from .models import *


def home(request):

    return render(request,'index.html')


def about(request):

    return render(request,'about.html')


def contact(request):

    return render(request,'contact.html')


def donor_dashboard(request):

    if not request.session.get('user_id'):

        return redirect('login')

    user_id=request.session.get('user_id')

    donor=Register.objects.get(id=user_id)

    total_donations=BloodDonation.objects.filter(
        donor_name=donor.name
    ).count()

    context={

        'donor':donor,

        'total_donations':total_donations

    }

    return render(request,'donor_dashboard.html',context)
def update_profile(request):

    if 'user_id' not in request.session:

        return redirect('login')

    user = Register.objects.get(
        id=request.session['user_id']
    )

    if request.method == "POST":

        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        user.blood_group = request.POST.get('blood_group')

        user.save()

        messages.success(
            request,
            'Profile Updated Successfully'
        )

        if user.role == "Donor":

            return redirect('donor_dashboard')

        elif user.role == "Patient":

            return redirect('patient_dashboard')

    context = {

        'user':user

    }

    return render(
        request,
        'update_profile.html',
        context
    )


def donate_blood(request):

    if not request.session.get('user_id'):

        return redirect('login')

    user_id=request.session.get('user_id')

    donor=Register.objects.get(id=user_id)

    if request.method=="POST":

        donor_name=donor.name

        blood_group=request.POST.get('blood_group')

        hospital=request.POST.get('hospital')

        city=request.POST.get('city')

        donation_date=request.POST.get('donation_date')

        data=BloodDonation(

            donor_name=donor_name,
            blood_group=blood_group,
            hospital=hospital,
            city=city,
            donation_date=donation_date

        )

        data.save()

        messages.success(request,'Blood Donation Submitted')

        return redirect('donor_dashboard')

    context={

        'donor':donor

    }

    return render(request,'donate_blood.html',context)

def patient_dashboard(request):

    if 'user_id' not in request.session:

        return redirect('login')

    patient = Register.objects.get(
        id=request.session['user_id']
    )

    context = {

        'patient':patient

    }

    return render(
        request,
        'patient_dashboard.html',
        context
    )

def blood_request(request):

    if not request.session.get('user_id'):

        return redirect('login')

    user_id=request.session.get('user_id')

    patient=Register.objects.get(id=user_id)

    if request.method=="POST":

        patient_name=patient.name

        blood_group=request.POST.get('blood_group')

        hospital=request.POST.get('hospital')

        city=request.POST.get('city')

        contact=request.POST.get('contact')

        data=BloodRequest(

            patient_name=patient_name,
            blood_group=blood_group,
            hospital=hospital,
            city=city,
            contact=contact

        )

        data.save()

        messages.success(request,'Blood Request Submitted')

        return redirect('blood_request')

    context={

        'patient':patient

    }

    return render(request,'blood_request.html',context)


def blood_availability(request):

    blood_group=request.GET.get('blood_group')

    donors=Register.objects.filter(role='Donor')

    if blood_group:

        donors=donors.filter(
            blood_group=blood_group
        )

    context={

        'donors':donors

    }

    return render(request,'blood_availability.html',context)


def admin_dashboard(request):

    total_donors=Register.objects.filter(role='Donor').count()

    total_requests=BloodRequest.objects.count()

    total_donations=BloodDonation.objects.count()

    context={

        'total_donors':total_donors,

        'total_requests':total_requests,

        'total_donations':total_donations,

    }

    return render(request,'admin_dashboard.html',context)


def manage_donors(request):

    search=request.GET.get('search')

    donors=Register.objects.filter(role='Donor')

    if search:

        donors=donors.filter(name__icontains=search)

    context={

        'donors':donors

    }

    return render(request,'manage_donors.html',context)


def manage_requests(request):

    requests=BloodRequest.objects.all()

    context={

        'requests':requests

    }

    return render(request,'manage_requests.html',context)

def register(request):

    if request.method=="POST":

        name=request.POST.get('name')

        email=request.POST.get('email')

        phone=request.POST.get('phone')

        age=request.POST.get('age')

        blood_group=request.POST.get('blood_group')

        role=request.POST.get('role')

        password=request.POST.get('password')

        check_email=Register.objects.filter(email=email)

        if check_email:

            messages.error(request,'Email Already Exists')

            return redirect('register')

        if len(phone) != 10:

            messages.error(
                request,
                'Phone Number Must Be 10 Digits'
            )

            return redirect('register')

        Register.objects.create(

            name=name,
            email=email,
            phone=phone,
            age=age,
            blood_group=blood_group,
            role=role,
            password=password

        )

        messages.success(request,'Registration Successful')

        return redirect('login')

    return render(request,'register.html')


def login(request):

    if request.method=="POST":

        email=request.POST.get('email')

        password=request.POST.get('password')

        # Admin Login

        if email=="admin@gmail.com" and password=="admin123":

            messages.success(request,'Admin Login Successful')

            return redirect('admin_dashboard')

        # User Login

        user=Register.objects.filter(

            email=email,
            password=password

        ).first()

        if user:

            request.session['user_id']=user.id

            messages.success(request,'Login Successful')

            if user.role=="Donor":

                return redirect('donor_dashboard')

            elif user.role=="Patient":

                return redirect('patient_dashboard')

        else:

            messages.error(request,'Invalid Email Or Password')

            return redirect('login')

    return render(request,'login.html')

def delete_donor(request,id):

    donor=Register.objects.get(id=id)

    donor.delete()

    return redirect('manage_donors')


def edit_donor(request,id):

    donor=Register.objects.get(id=id)

    if request.method=="POST":

        donor.name=request.POST.get('name')

        donor.phone=request.POST.get('phone')

        donor.blood_group=request.POST.get('blood_group')

        donor.save()

        messages.success(request,'Donor Updated Successfully')

        return redirect('manage_donors')

    context={

        'donor':donor

    }

    return render(request,'edit_donor.html',context)


def approve_request(request,id):

    blood=BloodRequest.objects.get(id=id)

    blood.status='Approved'

    blood.save()

    return redirect('manage_requests')


def reject_request(request,id):

    blood=BloodRequest.objects.get(id=id)

    blood.status='Rejected'

    blood.save()

    return redirect('manage_requests')


def delete_request(request,id):

    blood=BloodRequest.objects.get(id=id)

    blood.delete()

    return redirect('manage_requests')


def logout(request):

    request.session.flush()

    return redirect('home')
