
import django
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from django.core.mail import send_mail


from django.db.models import Q
from django.contrib.auth import get_user_model

from django.apps import apps
from allauth.account.signals import user_logged_in
from .icreated import wordcorrect,filterpage,filter_un_data
from .models import incorrect_data as inc
from .models import liked_data
from .models import images
from django.contrib.auth.decorators import login_required
from  .models import data_given_by_user
from .models import detailquery,feeback_data,save_contact_inf
user=get_user_model
from .forms import userdatain

# Create your views here.
def home(request):
    return render(request,"bus_templ/home.html")


#user_input_details
def user_inputs(request):
    return render(request,"bus_templ/user_input_form2.html")

def srch_data(request):
    return render(request,"bus_templ/search_update/search.html")

def src_res(request):
    town_name=request.POST["tab_name"]
    town_id=request.POST["townid"]
    data=filterpage.updater.fetch_data(town_name,town_id)
    return render(request,"bus_templ/search_update/resultupdate.html",{"data":data,"table_name":town_name,"town_id":town_id})
def up(request):
    print("helo world")
    mid_r=request.POST["middle_route"]
    src=request.POST["source"]
    dest=request.POST["dest"]
    arrive_t=request.POST["arrive_t"]
    leave_t=request.POST["leave_t"]
    bus_name=request.POST["busname"]
    tow_id=request.POST["twn_id"]
    filterpage.updater.update_pls(mid_r,src,dest,arrive_t,leave_t,bus_name,tow_id)
    return HttpResponse("<h1 style='font-size:50px ;margin-top:300px '><center>______updated______</center><br><a href='http://127.0.0.1:8000/search'  %}'>Back</a></h1>")

def user_input_details(request):
     print(request)
     source1=request.GET["source"]
     dest=request.GET["destination"]
     middleroot=request.GET["middleroot"]
     arrive_t1=request.GET["arrive_t"]
     leavet1=request.GET["depart"]
     bus_name1=request.GET["busnamesid"] #depart
     
     data_given_by_user.objects.create(Middle_route=middleroot,source=source1 ,destination=dest, arrive_t=arrive_t1 ,leave_t=leavet1, Busname=bus_name1)
     return render(request,"bus_templ/thank4feed.html")


#help page
def help(request):
    return render(request,"bus_templ/help.html")

def query_details_thank(request):
    return render(request,"bus_templ/lookur_query.html")



def feedback(request):
    return render(request,"bus_templ/feedback4.html")

def getfeedback_data(request):
    name=request.POST["name"]
    email=request.POST["email"]
    comment=request.POST["comment"]

    print("helo world the donkey")
    #c=apps.get_model("bus","") 
    feeback_data.objects.create(comments=comment,Email=email,user_name=name)
    return render(request,"bus_templ/feedbackthanku.html")

def admin_main_feedback(request):
    all_data=feeback_data.objects.all()
    return render(request,"bus_templ/feedbackuser/adpage.html",{"all_data":all_data})



#@login_required
def custom_feedback(request):
    print(request)
    source=request.POST["source"]
    dest=request.POST["dest"]
    time=request.POST["time"]
    return render(request,"bus_templ/custom_feeback/feed_on_details.html",{"src":source,"dest":dest,"time":time})

def store_custom_feedback(request):
    
   
    return render(request,"bus_templ/custom_feeback/feed_on_details.html")

def dump_data(request):
    print(request.POST)
 
    source1=request.POST["source"]
    dest2=request.POST["dest"]
    time2=request.POST["time"]
    email=request.POST["email"]
    print(email)
    username=request.POST["name"]
    comments2=request.POST["comments"]
    detailquery.objects.create(source=source1,dest=dest2,time=time2,Email=email,comments=comments2,user_name=username)
    return render(request,"bus_templ/lookur_query.html")
    
def admin_page_to_reply_comments(request):
    all=detailquery.objects.all()
    return render(request,"bus_templ/custom_feeback/aminspage.html",{"all_data":all})


def contact_form_reply(request):
    print("____________________________")
    all=save_contact_inf.objects.all()
    return render(request,"bus_templ/contact_form/contactus.html",{"all_data":all})

#comments
def contact_us2(request):
    print("heoo")
    return render(request,"bus_templ/contact_form/usercontact.html")

def save_contacted_info(request):
    name=request.POST["name"]
    email=request.POST["email"]
    comment=request.POST["comments"]
    save_contact_inf.objects.create(user_name=name,comments=comment,Email=email)
    return render(request,"bus_templ/lookur_query.html")



def send_mails(request):
    print(request)
    
    email=request.POST["email"]

    comments=request.POST["comments"]
    ide=request.POST["id"]
    print(email)
    print(comments)
    
    send_mail(
    'BUS_DETAILS_QUERY',
     
     comments,
    'gobuscoorg@gmail.com',#from
    [email],#to
    fail_silently=False,
      )
    
    if 'contact_us' in request.POST:
        save_contact_inf.objects.filter(id=ide).delete()
        all=save_contact_inf.objects.all()
        return render(request,"bus_templ/contact_form/contactus.html",{"all_data":all})

    if 'feedback' in request.POST:
        feeback_data.objects.filter(id=ide).delete()
        all=feeback_data.objects.all()
        return render(request,"bus_templ/feedbackuser/adpage.html",{"all_data":all})

    if  'detailquery' in request.POST:
        detailquery.objects.filter(id=ide).delete()
        all=detailquery.objects.all()
        print("deatil query")
        return render(request,"bus_templ/custom_feeback/aminspage.html",{"all_data":all})

    

def storefeedback(request):
    pass

def reapeated_data(request):
    arr=filterpage.pan.filt()
    arr_un= filterpage.filter_un_data.filt()
    return render(request,"bus_templ/filtered_data.html",{"array":arr,"unwan":arr_un})


def details(request):
    filterpage.pan.filt()
    print("-___")
    filterpage.filter_un_data.filt()
    filterpage.updater.fetch_data("madikeri2",1)
    source=request.POST["source"]
    dest2=request.POST["dest"]
    user_i=request.user.id
    time=request.POST["time"]
    
    if 'disp_all' in request.POST:
        time="6:00"  
    ur_place="kodagu"
    auth=request.user.is_authenticated
    townsdata=srch_table(source,dest2,time,user_i,auth)
  
    #print("iam printing the:",source)
    #print(townsdata[0][0].leave_t)
    if not townsdata:
        print("hello4")
        return render(request,"bus_templ/not_found.html")

    if auth: # if authenticated 
       return render(
           request,"bus_templ/details1.html",
           {
            "towns":townsdata[0],
           "tempmid":townsdata[1],
           "src1":townsdata[2],
           "dest1":townsdata[3],
           "mid1":townsdata[4],
           "f_id":townsdata[5],
           "auth":auth,
           "f_likecount":townsdata[6],
           "like_post_id":townsdata[7],
           "time":time,
           "noon":"noon"

           }
           )

# return's when user is not autenticated
    return render(
        request,"bus_templ/details1.html",
        {
            "towns":townsdata[0],
            "tempmid":townsdata[1],
            "src1":townsdata[2],
            "dest1":townsdata[3],
            "mid1":townsdata[4],
            "f_id":townsdata[5],
            "auth":auth,
             "f_likecount":townsdata[6],
             "time":time,
             "noon":"noon"
             
            
        }
            )

def srch_table(source,dest,fromtime,user_i,auth):
    #c=apps.get_model("bus","Madikeri")
    
    try:
        c=apps.get_model("bus",source)
    except LookupError:
        return None
    try:
        towns=c.objects.filter(Q(arrive_t__gte=fromtime),Q(arrive_t__lte='22:00')).order_by('arrive_t').order_by("Middle_route").filter(destination=dest)
    except django.core.exceptions.ValidationError:
    
        return None
    #towns=c.objects.filter(Q(arrive_t__gte=fromtime),Q(arrive_t__lte='22:00')).order_by('arrive_t').order_by("Middle_route").filter(destination=dest)
    
    if not  towns:
        return None
        
    tempMid=[]
    f_likecount=towns[0].likes_count
    temp=towns[0].Middle_route
    midt=towns[0].Middle_route
    source=towns[0].source
    destination=towns[0].destination
    f_id=towns[0].id
    for mid in towns:
        #print("if",mid.Middle_route,"!=",temp)
        if mid.Middle_route != temp: # 0 middle route ! = 0 middle route
            #print("pass if",mid.Middle_route,"!=",temp)
            tempMid.append(mid.id)
            #print( "testing now= tempid =",tempMid)
            temp=mid.Middle_route    
            #print("testing now  temp ",temp)
    
    
    if auth: #if authenticated 
        
        liked_post=liked_data.objects.filter(user_id=user_i)
        liked_post_arr=[i.post_id for  i in liked_post] 
        return [towns,tempMid,source,destination,midt,f_id,f_likecount,liked_post_arr]

    return [towns,tempMid,source,destination,midt,f_id, f_likecount]

    
@login_required
def get_data(request):
    
    username=request.user.username
    like=request.POST["likedis"]
    post_i=request.POST["idval"]
    source=request.POST["source"]
    user_i=request.user.id
    counter=apps.get_model("bus",source)
  
    if like in "on":
        print("iam on")
        # create liked data if its does not exists with user id 
        liked=liked_data.objects.filter(Q(user_id=user_i),Q(post_id=post_i))#
        print(liked,"likedata exists")
        # create liked data if its does not exists with user id 
        #like turned on
        if not liked: # createting if user id  & post id doesnot exists 
            liked_data.objects.create(user_id=user_i,post_id=post_i).save()
            
        count=counter.objects.only("likes_count").get(id=post_i)
        count.likes_count= count.likes_count + 1
        count.save()

    else:
        #like turned off
        liked_data.objects.filter(Q(user_id=user_i),Q(post_id=post_i)).delete()
        count=counter.objects.only("likes_count").get(id=post_i)
        count.likes_count= count.likes_count - 1
        count.save() 

    count=counter.objects.only("likes_count").get(id=post_i) 

    return  JsonResponse({ 
            "data":count.likes_count
            })
    


 

#@login_required(redirect_field_name="/")
def incorrect_dataf(request):
    print(request)
    username=request.user.username
    town_id=request.POST["ids"]
    u_comp=request.POST["comp"]
    Source=request.POST["source"]
    
   
    print("__get__data__")
    print(town_id)
    print(Source)
    print(u_comp)
    print(username)
  
    u=inc.objects.create(town_tab_name=Source,post_id=town_id,complaint=u_comp)

    u.save()
 
    return HttpResponse("")

                                                                         