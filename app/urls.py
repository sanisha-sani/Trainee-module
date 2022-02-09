from . import views
from django.views.generic import TemplateView
from django.urls import path, re_path
urlpatterns = [
    re_path(r'^$', views.index_trainee,name='index_trainee'),
    # re_path(r'^Newtrainees$', views.Newtrainees,name='Newtrainees'),

    ###############################ALTHAF######################################################
    # re_path(r'^trainer$', views.trainer, name='trainer'),
    # re_path(r'^Applyleave$', views.Applyleave, name='Applyleave'),
    # re_path(r'^trainers_leave$', views.trainers_leave, name='trainers_leave'),
    # re_path(r'^trainees_leave$', views.trainees_leave, name='trainees_leave'),
   

    ###################################EMIL#####################################################
    # re_path(r'^team$', views.team, name='team'),
    # re_path(r'^current$', views.current, name='current'),
    # re_path(r'^task$', views.task, name='task'),
    # re_path(r'^ass$', views.ass, name='ass'),
    # re_path(r'^Trainees$', views.Trainees, name='Trainees'),
    # re_path(r'^Empdetails$', views.Empdetails, name='Empdetails'),
    # re_path(r'^TAttendance$', views.TAttendance, name='TAttendance'),
    # re_path(r'^task1$', views.task1, name='task1'),
    # re_path(r'^List$', views.List, name='List'),
    # re_path(r'^tdetails$', views.tdetails, name='tdetails'),

#######################################################KRIPA##############################################

    # re_path(r'^trteam$', views.TRteam, name='trteam'),
    # re_path(r'^prteam$', views.Previous, name='prteam'),
    # re_path(r'^prtask$', views.Previous_Task, name='prtask'),
    # re_path(r'^prass$', views.Previous_Assigned, name='prass'),
    # re_path(r'^prtrainees$', views.Previous_Trainees, name='prtrainees'),
    # re_path(r'^PEmpdetails$', views.PEmpdetails, name='PEmpdetails'),
    # re_path(r'^PAttendance$', views.PAttendance, name='PAttendance'),
    # re_path(r'^Ptask1$', views.Ptask1, name='Ptask1'),
    # re_path(r'^PList$', views.PList, name='PList'),
    # re_path(r'^Ptdetails$', views.Ptdetails, name='Ptdetails'),
    
##################################################SANISHA######################################################## 

    re_path(r'^reportedissue$', views.reportedissue, name='reportedissue'),
    re_path(r'^reportissuetrainers$', views.reportissuetrainers, name='reportissuetrainers'),
    re_path(r'^reportissuetrainees$', views.reportissuetrainees, name='reportissuetrainees'),
    re_path(r'^trainerunsolvedissue$', views.trainerunsolvedissue, name='trainerunsolvedissue'),
    re_path(r'^trainersolvedissue$', views.trainersolvedissue, name='trainersolvedissue'),
    re_path(r'^traineesunsolved$', views.traineesunsolved, name='traineesunsolved'),
    re_path(r'^traineessolved$', views.traineessolved, name='traineessolved'),
    re_path(r'^trainee_topic$', views.trainee_topic, name='trainee_topic'),
    re_path(r'^trainee_currentTopic$', views.trainee_currentTopic, name='trainee_currentTopic'),
    re_path(r'^trainee_previousTopic$', views.trainee_previousTopic, name='trainee_previousTopic'),

####################################################JISHNU######################################################    
    # re_path(r'^reportissue$', views.reportissue, name='reportissue'),
    # re_path(r'^reportedissuesub$', views.reportedissuesub, name='reportedissuesub'),
    # re_path(r'^applyleavesub$', views.applyleavesub, name='applyleavesub'),


######################################################LEYA#######################################################


    # re_path(r'^Trainee$',views.Trainee,name="Trainee"),
    # re_path(r'^notify',views.notify,name="notify"),
    # re_path(r'^details$',views.traineedetails,name="traineedetails"),
    # re_path(r'^Statustable$',views.statusTable,name="statusTable"),
    # re_path(r'^notification$',views.notification,name="notification"),
    # re_path(r'^notverified$',views.notverify,name="notverify"),
    # re_path(r'^verified$',views.verify,name="verify"),
   
##############################SEBIN###########################################################################

    # re_path(r'^Requestedleave$', views.Requestedleave, name='Requestedleave'),
    # re_path(r'^Applyleave$', views.Applyleave, name='Applyleave'),
    # re_path(r'^Attendance$', views.Attendance, name='Attendance'),
    # re_path(r'^Trainees_Calendar$', views.Trainees_Calendar, name='Trainees_Calendar'),
    # re_path(r'^Trainees_Attendancetable$', views.Trainees_Attendancetable, name='Trainees_Attendancetable'),
    # re_path(r'^Trainers_Calendar$', views.Trainers_Calendar, name='Trainers_Calendar'),
    # re_path(r'^Trainers_Attendancetable$', views.Trainers_Attendancetable, name='Trainers_Attendancetable'),
    
###################################################FUAD#####################################################

    # re_path(r'^new_team$', views.new_team, name='new_team'),
    # re_path(r'^new_team1$', views.new_team1, name='new_team1'),
    # re_path(r'^team_update$', views.team_update, name='team_update'),
]   