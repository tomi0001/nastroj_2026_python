from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ...models import Moods


# Create your views here.
class mood():    
    def selectLastMoods(self,request):
        user = request.user
        return Moods.objects.filter( id_users = user.id).order_by("-date_end").first()

    def checkTimeExist(self,request,dateStart ,dateEnd):
        user = request.user
        return Moods.objects.filter( id_users = user.id).filter( date_start__lt = dateEnd).filter( date_end__gt = dateStart).order_by("-date_end").first()
        # return Moods.objects.raw(" SUBSTRING((date_end),1,16) as date_end where  date_start < '%s' and date_end > '%s'  and id_users = '%d' limit 1",(dateEnd),(dateStart),user.id)
    def saveMood(self, request, dateStart, dateEnd):
        user = request.user 
        Mood = Moods()
        Mood.date_start = dateStart
        Mood.date_end = dateEnd
# request.GET.get('timeStart')
        Mood.level_mood = request.GET.get('moodLevel')


        Mood.level_anxiety = request.GET.get('anxietyLevel')  
        Mood.type = "mood"


        Mood.level_nervousness = request.GET.get('voltageLevel') 


        Mood.level_stimulation = request.GET.get('stimulationLevel') 


        # Mood.epizodes_psychotik = request.GET.get('epizodesPsychotic')

        Mood.what_work = ""
        Mood.id_users_id =  user.id
        Mood.save();
        return Mood.id;