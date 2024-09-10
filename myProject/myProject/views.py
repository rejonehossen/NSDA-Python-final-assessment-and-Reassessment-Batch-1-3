from django.shortcuts import render, redirect,HttpResponse, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from myProject.forms import *
from myApp.models import *
from django.db.models import Q


def signin(request):
    if request.method == 'POST':
        form=signinform(request, data=request.POST)
        
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect("dashboard")
    else:
        form=signinform()
    return render(request,'signin.html',{'form':form})

def signup(request):
    if request.method == 'POST':
        form=signupform(request.POST, request.FILES)
        
        if form.is_valid():
            user=form.save(commit=False)
            usertype=form.cleaned_data["usertype"]
            user.save()
            if usertype == 'job_recruiter':
                recruiterprofile.objects.create(myuser=user)
            else:
                seekerprofile.objects.create(myuser=user)

            return redirect("signin")
    else:
        form=signupform(request.POST,request.FILES)
    return render(request,'signup.html',{'form':form})

def signout(request):
    logout(request)
    return redirect("signin")



@login_required
def index(request):
    return render(request,'index.html')



def dashboard(request):
    return render(request,'dashboard.html')

@login_required
def addjob(request):
    if request.method == 'POST':
        form=jobform(request.POST,request.FILES)
        if form.is_valid():
            job=form.save(commit=False)
            job.created_by=request.user
            job.save()
            return redirect("joblistforall")
    else:
        form=jobform(request.POST, request.FILES)
    return render(request,'addjob.html',{'form':form})


def joblistforall(request):
    job=jobmodel.objects.all()
    
    return render(request,'joblistforall.html',{'job':job})

@login_required
def postedjob(request):
    job=jobmodel.objects.filter(created_by=request.user)
    return render(request,'postedjob.html',{'job':job})

@login_required
def editjob(request,myid):
    job=get_object_or_404(jobmodel,id=myid)
    if request.method == 'POST':
        form=jobform(request.POST,instance=job)
        if form.is_valid():
            job=form.save(commit=False)
            job.created_by=request.user
            job.save()
            return redirect("joblistforall")
    else:
        form=jobform(instance=job)
    return render(request,'editjob.html',{'form':form})

@login_required
def deletejob(request,myid):
    job=jobmodel.objects.get(id=myid)
    job.delete()
    return redirect("joblistforall")


@login_required
def jobdetails(request,myid):
    
    job=jobmodel.objects.filter(id=myid)
    
    return render(request,'jobdetails.html',{'job':job})




@login_required
def profile(request):
    return render(request,'profile.html')


@login_required
def editprofile(request):
    if request.method == 'POST':
        if request.user.usertype == 'job_recruiter':
            form=editprofileformforrecruiter(request.POST,request.FILES, instance=request.user)
        else:
            form=editprofileformforseeker(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        if request.user.usertype == 'job_recruiter':
            form=editprofileformforrecruiter(instance=request.user)
        else:
            form=editprofileformforseeker(instance=request.user)
    return render(request,'editprofile.html',{'form':form})

@login_required
def applyjobpage(request,myid):
    myjob=get_object_or_404(jobmodel,id=myid)
    # applicant=applyjob.objects.filter(applied_by=request)
    if request.method == 'POST':
        form=jobapplyform(request.POST, request.FILES)
        if form.is_valid():
            application=form.save(commit=False)
            application.applied_by=request.user
            application.apply_to=myjob
            application.save()
            return redirect("appliedjob")
    else:
        form=jobapplyform(request.POST)
    return render(request,'applyjobpage.html',{'form':form,'myjob':myjob})

@login_required
def appliedjob(request):
    appliedjobs=applyjob.objects.filter(applied_by=request.user)
    return render(request,'appliedjob.html',{'appliedjobs':appliedjobs})



@login_required
def viewapplicant(request,myid):
    myjob=get_object_or_404(jobmodel,id=myid)
    applicant=applyjob.objects.filter(apply_to=myjob)
    return render(request,'viewapplicant.html',{'applicant':applicant,'myjob':myjob})


@login_required
def canceljob(request,myid):
    myjob=applyjob.objects.get(id=myid)
    myjob.delete()
    return redirect("appliedjob")

@login_required
def reject(request,myid):
    applicant=get_object_or_404(applyjob,id=myid)
    applicant.status= 'reject'
    applicant.save()
    return redirect("viewapplicant",myid=applicant.apply_to.id)

@login_required
def approve(request,myid):
    applicant=get_object_or_404(applyjob,id=myid)
    applicant.status= 'approve'
    applicant.save()
    return redirect("viewapplicant",myid=applicant.apply_to.id)

@login_required
def searchpagetitle(request):
    query=request.GET.get('query')
    search=jobmodel.objects.filter(title__icontains=query)
    return render(request,'searchpagetitle.html',{'query':query,'search':search})


# @login_required
# def searchpageskills(request):
#     query=request.GET.get('query')
#     search=jobmodel.objects.filter(skills__icontains=query)
    
#     return render(request,'searchpageskills.html',{'query':query,'search':search})

@login_required
def searchpageskills(request):
    query=request.GET.get('query')
    search=jobmodel.objects.filter(skills__icontains=query)
    myDict={
        'query':query,
        'search':search,
    }
    return render(request,'searchpageskills.html',myDict)