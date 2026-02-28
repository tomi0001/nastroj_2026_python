from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ...models import Sleep_types


# Create your views here.
class sleepType():
    def addSleepPercent(self,request,idSleep:int):
        Sleep =  Sleep_types();
        Sleep.id_moods_id = idSleep;
        if (  request.GET.get("percentFlat") ):
            Sleep.sleep_flat = request.GET.get("percentFlat");
        if (  request.GET.get("percentDeep") ):
            Sleep.sleep_deep = request.GET.get("percentDeep");
        if (  request.GET.get("percentRem") ):
            Sleep.sleep_rem = request.GET.get("percentRem");
        if (  request.GET.get("percentWorking") ):
            Sleep.sleep_working = request.GET.get("percentWorking");
        Sleep.save();

    

    # public function deleteSleep(int  $id) {
    #     $Mood = new self;
    #     $Mood->where("id_moods",$id)->delete();
    # }
    # public static function showSleepType(int $moods) {
    #     return self::selectRaw("sleep_flat")->selectRaw("sleep_deep")->selectRaw("sleep_rem")->selectRaw("sleep_working")->where("id_moods",$moods)->first();
    # }
    # public function updateSleep( $request) {
    #     $Mood = new self;
    #     $Mood->where("id_moods",$request->get("id"))
    #             ->update(["sleep_flat"=> $request->get("sleepFlatEdit"),"sleep_deep"=> $request->get("sleepDeepEdit"),
    #             "sleep_rem"=> $request->get("sleepRemEdit"),"sleep_working"=> $request->get("sleepWorkingEdit")]);
    
    # }