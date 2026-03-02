from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import Moods
from .models.mood import mood as modelsMood
from .models.action import action as modelsAction
from datetime import datetime
import time
from dateutil import parser
from django.conf import settings
from django import forms



# Create your views here.
class mood():
    # liczba = forms.FloatField(min_value=0.0, max_value=100.0)
    # form = mood(request.GET)
    # if form.is_valid():
    # # Dane są poprawne, zamienione na float
    #     wartość = form.cleaned_data['liczba']
    #     print(type(wartość))  # <class 'float'>
    # else:
    #     # Błąd walidacji, np. użytkownik wpisał tekst
    #     print(form.errors)
    def __init__(self):

        self.dateAddMoodStart :str
        self.timeAddMoodStart :str
        self.dateAddMoodEnd :str
        self.timeAddMoodEn :str
        self.dateStart :str
        self.dateEnd :str
        self.errors = []
        self.exception =[]
        self.moodsVariable = []
        self.moodLevel :float
        self.anxietyLevel   :float
        self.voltageLevel :float
        self.stimulationLevel :float
        self.epizodesPsychotic :int
        # self.levelMood = [
        # 0 =>  ["from" => -20, "to" => -18],
        # 1 =>  ["from" => -18, "to" => -16],
        # 2 =>  ["from" => -16, "to" => -14],
        # 3 =>  ["from" => -14, "to" => -12],
        # 4 =>  ["from" => -12, "to" => -10],
        # 5 =>  ["from" => -10, "to" => -8],
        # 6 =>  ["from" => -8, "to" => -6],
        # 7 =>  ["from" => -6, "to" => -2],
        # 8 =>  ["from" => -2, "to" => -1],
        # 9 =>  ["from" => -1, "to" => 0],
        # 10 =>  ["from" => 0, "to" => 1],
        # 11 =>  ["from" => 1, "to" => 2],
        # 12 =>  ["from" => 2, "to" => 4],
        # 13 =>  ["from" => 4, "to" => 6],
        # 14 =>  ["from" => 6, "to" => 8],
        # 15 =>  ["from" => 8, "to" => 10],
        # 16 =>  ["from" => 10, "to" => 12],
        # 17 =>  ["from" => 12, "to" => 14],
        # 18 =>  ["from" => 14, "to" => 16],
        # 19 =>  ["from" => 16, "to" => 18],
        # 20 =>  ["from" => 18, "to" => 20],
        
        # ];
    # def convertValue(self,request):
    #     # forms.FloatField(min_value=0.0, max_value=100.0)
    #     self.moodLevel = float(request.GET.get('moodLevel'))
    #     self.anxietyLevel = float(request.GET.get('anxietyLevel'))
    #     self.voltageLevel = float(request.GET.get('voltageLevel'))
    #     self.stimulationLevel = float(request.GET.get('stimulationLevel'))
    #     self.epizodesPsychotic = int(request.GET.get('epizodesPsychotic'))

    def selectLastMoods(self, request,):
        ModelsMood = modelsMood()
        result = ModelsMood.selectLastMoods(request);
        if (result == None):
            self.exception.append("dateError");
            return 0;
        return (result);


    def saveMood(self, request, dateStart,dateEnd):
        ModelsMood = modelsMood()
        id = ModelsMood.saveMood( request, dateStart, dateEnd);
        return id;


    
    # def setVariableMood(self,request) {
    #     if (request.GET.get('moodLevel') != ""):
    #         self.moodsVariable["mood"] = $request->get("moodLevel");
    #     else {
    #         self.moodsVariable["mood"] = 0;
    #     }
    #     if ($request->get("anxietyLevel") != "") {
    #         self.moodsVariable["anxiety"] = $request->get("anxietyLevel");
    #     }
    #     else {
    #         self.moodsVariable["anxiety"] = 0;
    #     }
    #     if ($request->get("voltageLevel") != "") {
    #         self.moodsVariable["voltage"] = $request->get("voltageLevel");
    #     }
    #     else {
    #         self.moodsVariable["voltage"] = 0;
    #     }
    #     if ($request->get("stimulationLevel") != "") {
    #         self.moodsVariable["stimulation"] = $request->get("stimulationLevel");
    #     }
    #     else {
    #         self.moodsVariable["stimulation"] = 0;
    #     }
    #     if ($request->get("epizodesPsychotic") != "" ) {
    #         self.moodsVariable["epizodesPsychotic"] = $request->get("epizodesPsychotic");
    #     }
    #     else {
    #         self.moodsVariable["epizodesPsychotic"] = 0;
    #     }
    # }
    # @login_required
    # def checkErrorLevelMood(request):
        

    #     for i in range(-10,10):

    #     for ($i = -10;$i <= 10;$i++) {
    #         if (i == 10):
    #             if ($request->get("valueMood10From") >=  20) {
    #                 array_push($this->errors,"Formularz o numerze "  . ($i + 11) . " Jest mniejszy bądź równy od -20" );
    #             }
    #         }
    #         if ($i == -10 ) {

    #             if ($request->get("valueMood-9From") <= -20) {
    #                 array_push($this->errors,"Formularz o numerze "  . ($i + 11) . " Jest mniejszy bądź równy od -20" );
    #             }
    #         }
    #         else {
    #             if ($request->get("valueMood" . $i . "From") == "") {
    #                 array_push($this->errors,"Formularz o numerze "  . ($i + 11) . " 'Od' musi być uzupełniony");
    #             }
 
    #             if (!is_numeric($request->get("valueMood" . $i . "From") ) or $request->get("valueMood" . $i . "From") < -20 or $request->get("valueMood" . $i . "From") > 20) {
    #                 array_push($this->errors,"Formularz o numerze "  . ($i + 11) . " 'Od' być w zakresie od -20 do +20");
    #             }

    #             if ($request->get("valueMood" . $i . "From") <= $request->get("valueMood" . ($i-1) . "From")) {
    #                 array_push($this->errors,"Formularz o numerze "  . ($i + 11) . " Jest mniejszy bądź równy od Formularza  o numerze " .  (($i - 1 ) + 11));
    #             }

    #         }
    #     }

    # @login_required
    # def saveMood(Request $request,string $dateStart,string $dateEnd,array $arrayMood) {
    #     $Mood = new MoodModel;
    #     $id = $Mood->saveMood( $request, $dateStart, $dateEnd, $arrayMood);
    #     return $id;
    # }
        
 
    def checkError(self,dateStart ,dateEnd ,request):
        ModelsMood = modelsMood()
        dateStart = str(dateStart)
        dateEnd = str(dateEnd)
        # dateStart = parser.parse(dateStart)
        # dateStart = datetime.strptime(dateStart, '%Y-%m-%d %H:%M')
        # dateStartText = dateStart.strftime("%Y-%m-%d %H:%M")
        # dateEnd = datetime.strptime(dateEnd, '%Y-%m-%d %H:%M')
        # dateEndText = dateEnd.strftime("%Y-%m-%d %H:%M")
        dateStart2 = datetime.strptime(dateStart, "%Y-%m-%d %H:%M:%S")
        dateEnd2 = datetime.strptime(dateEnd, "%Y-%m-%d %H:%M:%S")
        # dateStart =  dateStart.split(" ");
        # dateEnd  = dateEnd.split(" ");
        
        # dateStart1 =  dateStart[0].split("-");
        # dateStart2 =  dateStart[1].split(":");
        # # self.errors.append(dateStart2[1]);
        # dateEnd1 =  dateEnd[0].split("-");
        # dateEnd2 =  dateEnd[1].split(":");
        # dateStart = datetime(int(dateStart1[0]), int(dateStart1[1]), int(dateStart1[2]), int(dateStart2[0]), int(dateStart2[1]), 0)
        # dateEnd = datetime(int(dateEnd1[0]), int(dateEnd1[1]), int(dateEnd1[2]), int(dateEnd2[0]), int(dateEnd2[1]), 0)
        if (not dateStart ):
            self.errors.append("Uzupełnij datę zaczęcia");                   
        if (dateEnd2 == ""):
            self.errors.append("Uzupełnij datę zakończenia");
            
        if (ModelsMood.checkTimeExist(request,str(dateStart) , str(dateEnd) )):
            self.errors.append("Godziny nastroju  nachodza na inne nastroje");
       
        if (dateStart2.timestamp() >= dateEnd2.timestamp()):
            self.errors.append("Godzina zaczęcia jest wieksza bądź równa godzinie skończenia");
        
        if (int(time.time())  < (dateEnd2.timestamp())):
            self.errors.append("Data skończenia nastroju jest wieksza od teraźniejszej daty");
    
            
        if (  dateEnd2.timestamp() - dateStart2.timestamp() > settings.LONG_MOOD):
            self.errors.append("Nastroj nie może mieć takiego dużego przedziału czasowego");
        
        if (  dateEnd2.timestamp() - dateStart2.timestamp() < settings.SHORT_MOOD):
            self.errors.append("Nastroj nie może mieć takiego krótkiego przedziału czasowego");
        
       
    
    def checkAddMood(self,request):
        # data = self.cleaned_data['price']
        field = forms.FloatField(min_value=-20.00, max_value=20.00)
        try:
            mood_level = field.clean(request.GET.get('moodLevel'))
        except forms.ValidationError:
            self.errors.append("Nastroj musi mieścić się w zakresie od -20 do +20");
        try:
            mood_level = field.clean(request.GET.get('anxietyLevel'))
        except forms.ValidationError:
            self.errors.append("Lęk musi mieścić się w zakresie od -20 do +20");
        try:
            mood_level = field.clean(request.GET.get('voltageLevel'))
        except forms.ValidationError:
            self.errors.append("Napięcie musi mieścić się w zakresie od -20 do +20");
        try:
            mood_level = field.clean(request.GET.get('stimulationLevel'))
        except forms.ValidationError:
            self.errors.append("Pobudzenie musi mieścić się w zakresie od -20 do +20");
        field = forms.IntegerField(required=False,min_value=0)
        try:
            mood_level = field.clean(request.GET.get('epizodesPsychotic'))
        except forms.ValidationError:
            self.errors.append("Liczba Epizodów psychotycznych musi być wieksza lub równa 0");
        # if f.is_valid():
        #     mood_value = f.cleaned_data['moodLevel']
        # if ( self.moodLevel < -20 or self.moodLevel> 20):
        #     self.errors.append("Nastroj musi mieścić się w zakresie od -20 do +20");
        
        
        # if (self.anxietyLevel  < -20 or self.anxietyLevel   > 20 ):
        #     self.errors.append("Lęk musi mieścić się w zakresie od -20 do +20");
        
        
        # if (self.voltageLevel  < -20 or self.voltageLevel > 20):
        #     self.errors.append("Napięcie musi mieścić się w zakresie od -20 do +20");
        
        
        # if (self.stimulationLevel < -20 or self.stimulationLevel  > 20):
        #     self.errors.append("Pobudzenie musi mieścić się w zakresie od -20 do +20");
        
        
        # if ( self.epizodesPsychotic < 0):
        #     self.errors.append("Liczba Epizodów psychotycznych musi być wieksza lub równa 0");
        

    

    #     public function checkErrorAction(Request $request,int $minute) {
    #     if (empty($request->get("idActions")  )) {
    #         return;
    #     }
    #     for ($i = 0;$i < count($request->get("idActions"));$i++) {
    #         if ($request->get("idActions")[$i] != "" and $request->get("idActions")[$i] != NULL and ($request->get("idActions")[$i] < 1 or $request->get("idActions")[$i] > 100)) {
    #             array_push($this->errors,"Procent musi być w zakresie od 1 do 100 lub pole ma być puste");
    #         }
    #         if ($request->get("idActionMinute")[$i] != NULL and $request->get("idActions")[$i] != NULL) {
    #             array_push($this->errors,"Nie może być dla jednej akcji obie wartości procesntu i minut wykonania różne od NULL");
    #         }
    #         if ($request->get("idActionMinute")[$i] != NULL and $request->get("idActionMinute")[$i] > $minute) {
    #             array_push($this->errors,"Wartośc minut wykracza za wartośc czasowa nastroju");
    #         }
            
    #     }
    # }



    def selectAction(self,idUser):
        Action = modelsAction()
        return Action.selectAction(idUser);
