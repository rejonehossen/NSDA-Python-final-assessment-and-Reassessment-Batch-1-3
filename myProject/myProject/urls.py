from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentication
    path('signin/',signin,name="signin"),
    path('signup/',signup,name="signup"),
    path('signout/',signout,name="signout"),
    
    
    # common
    path('index/',index,name="index"),
    path('',dashboard,name="dashboard"),
    
    # Job Crud
    path('editjob/<str:myid>',editjob,name="editjob"),
    path('jobdetails/<str:myid>',jobdetails,name="jobdetails"),
    path('deletejob/<str:myid>',deletejob,name="deletejob"),
    path('addjob/',addjob,name="addjob"),
    
    path('postedjob/',postedjob,name="postedjob"),
    # Job List
    path('joblistforall/',joblistforall,name="joblistforall"),
    
    
    # Job Apply Seeker
    path('appliedjob/',appliedjob,name="appliedjob"),
    path('applyjobpage/<str:myid>',applyjobpage,name="applyjobpage"),
    path('canceljob/<str:myid>',canceljob,name="canceljob"),
    
    
    # Job Section Recruiter
    path('viewapplicant/<str:myid>',viewapplicant,name='viewapplicant'),
    path('reject/<str:myid>',reject,name='reject'),
    path('approve/<str:myid>',approve,name='approve'),
    
    # Profile
    path('profile/',profile,name="profile"),
    path('editprofile/',editprofile,name="editprofile"),
    
    # Search
    path('searchpagetitle/',searchpagetitle,name="searchpagetitle"),
    path('searchpageskills/',searchpageskills,name="searchpageskills"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




