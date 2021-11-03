from django.urls import path
from . import views 

urlpatterns = [
    path("",views.home,name="home"),
    path("details",views.details,name="details"),
    path("data_get",views.get_data,name="data_get"),
    path("incorrect_data",views.incorrect_dataf,name="incorrect_data"),    
    path("help",views.help,name="please_help"),

    path("feedback",views.feedback,name="feedback"),
    path("get_feedback_data",views.getfeedback_data,name="getfeeddata"),
    path("admin_main_feedback",views.admin_main_feedback,name="admin_main_feedback"),

    path("userinp",views.user_input_details,name="userinp"),
    path("userinput",views.user_inputs,name="userinputs"),

    path("detailquery",views.custom_feedback,name="detailquery"),
    path("detailquery2",views.store_custom_feedback,name="detailquery2"),
    path("adminreply",views.admin_page_to_reply_comments,name="adminreply"),
    path("send_email",views.send_mails,name="sendmail"),

    path("admin_contact_us",views.contact_form_reply,name="admin_contact_us"),#contact_form_reply
    path("contact_us",views.contact_us2,name="conatct_us"),
    path("contact_store",views.save_contacted_info,name="contact_save"),

    path("dump_data",views.dump_data,name="dump_data"),

    path("query_user_help",views.query_details_thank,name="query_user_help"),

    path("reapeated",views.reapeated_data,name="repeated_datas"),
    path("search",views.srch_data,name="search"),

    path("srch_res1",views.src_res,name="srch_res"),
    path("updater",views.up,name="updater")
    
  



  
]
