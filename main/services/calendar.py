from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import numpy as np
from datetime import date
import time
import calendar
import requests

"""
 copyright januar 2026 autor tomi0001@gmail.com

"""

class calendar():
    


 
    
    def __init__(self, request,year, month, day):
            self.month :int
            self.day :int
            #action;
            self.year :int
            self.day_week :int
            
            self.back_year = [];
            self.next_year = [];
            self.text_month :str;
            self.next_month = [];
            self.back_month = [];
            self.how_day_month :int
            self.setDate(request,month,day,year);
            self.how_day_month = self.checkMonth(self.month,self.year);
            self.back_month = self.returnBackMonth(self.month,self.year);
            self.next_month = self.returnNextMonth(self.month,self.year);
            self.text_month = self.returnMonthText(self.month);
            self.next_year  = self.returnNextYear(self.year);
            self.back_year  = self.returnBackYear(self.year);
    

    def returnMonthText(self,month):
    
            match(month):
              case 1 : return "Styczeń";
              case 2 : return "Luty";
              case 3 : return "Marzec";
              case 4 : return "Kwiecień";
              case 5 : return "Maj";
              case 6 : return "Czerwiec";
              case 7 : return "Lipiec";
              case 8 : return "Sierpień";
              case 9 : return "Wrzesień";
              case 10 : return "Październik";
              case 11: return "Listopad";
              case 12 : return "Grudzień";
            

    @staticmethod
    def nextMonth(self,year,month):
        if (month == 12):
          year+=1;
          month = 1;
        else:
          month+=1;
        
        return year + "-"  + month;
    
    def returnBackMonth(self,month,year):
        #month = int(month)
        if (month == 1):
          year-=1;
          month = 12;
        
        else:
          month -= 1
        
        return [year,month];
    

    def returnNextMonth(self,month,year):
          #month = int(month)
          if (month == 12):
            year+=1;
            month = 1;
          else:
            month+= 1
          return [year,month];
        

    
    def returnNextYear(self,year):
        #year = int(year)
        return [year+ 1,self.month];
    
    def returnBackYear(self,year):
        #year = int(year)

        return [year -1,self.month];
        
    def setDate(self,request,month,day,year):
        if ( not year):
            self.year = date.today().year
        else:
            self.year = year;
        if (not month):
            self.month = date.today().month
        else:
            self.month = month;
        if (not day):
            self._calculateStartDay(request,date.today().day);
            #self.day = 12;
        else:
            self.day = day;
            
        self.day_week = self._setBeginningDay(self.year, self.month, 1);
            
        if (self.day_week == 0):
            self.day_week = 7;
        
            
    
    
    
    def _setBeginningDay(self,year,month,day):
        # year = int(year)
        # month = int(month)
        # day = int(day)
        data = date(year, month, day)
        return data.weekday() 

      

    @staticmethod
    def checkMonth(month,year):
            if (month == 12):
                return 31;
            
            elif (month == 11):
                return 30;
            
            elif (month == 10):
                return 31;
            
            elif (month == 9):
                return 30;
            
            elif (month == 8):
                return 31;
            
            elif (month == 7):
                return 31;

            elif (month == 6):
                return 30;
            
            elif (month == 5):
                return 31;
            
            elif (month == 4):
                return 30;
            
            elif (month == 3):
                return 31;
            
            elif (month == 2):

                if (  ((year%4 == 0 and year%100 != 0) or year%400 == 0) == 1):
                    return 29;
                
                else:
                    return 28;
                

            
            elif (month == 1):
                return 31;
            
            else:
                return 30;
        
         
    
  
    def _calculateStartDay(self,request, day):
      if (request.user.id - 1):
          second = time.time();
          self.day = date.fromtimestamp((second)).day;
      
      else:
          self.day = date.today().day;
      