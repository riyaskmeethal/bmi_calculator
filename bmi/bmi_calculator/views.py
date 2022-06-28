import math
from django.shortcuts import render
from django.views.generic import TemplateView,View
from .forms import BmiForm


# Create your views here.
class Home(View):
    template_name="bmi_calculator/home.html"

    def get (self,request,*aurgs,**kwaurgs):
        return render(request,template_name=self.template_name)


class Calculate(View):
    template_name="bmi_calculator/form.html"

    def get (self,request,*aurgs,**kwaurgs):
        context={'form': BmiForm}

        return render(request,template_name=self.template_name,context=context)

    def post (self,request,*aurgs,**kwaurgs):
        form = BmiForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            print(form.cleaned_data )
            scale = form.cleaned_data['scale']
            meters = form.cleaned_data['meters']
            centi_meters = form.cleaned_data['centi_meters']
            foots = form.cleaned_data['foots']
            inches = form.cleaned_data['inches']
            weight = form.cleaned_data['weight']
            weight_kg = weight
            if scale == 'meter':
                height_m2 =self.mtr_to_mtr_sqr(meters,centi_meters)
            elif scale == 'foot':
                height_m2 = self.foot_to_mtr_sqr(foots,inches)
            context={}
            
            bmi = round(self.final_bmi_calculation(weight_kg,height_m2),2)
            if bmi<18.5:
                context['bmi_status'] = 'UNDER WEIGHT'
                context['bmi_img'] = 'bmi_calculator/img/under_weight.gif'
            elif bmi>=18.5 and bmi<=24.9:
                context['bmi_status'] = 'NORMAL WEIGHT'
                context['bmi_img'] = 'bmi_calculator/img/normal.gif'
            elif bmi>=25 and bmi<=29.9:
                context['bmi_status'] = 'OVER WEIGHT'
                context['bmi_img'] = 'bmi_calculator/img/over_weight.gif'
            elif bmi>=30 and bmi<=34.9:
                context['bmi_status'] = 'OBESITY CLASS 1'
                context['bmi_img'] = 'bmi_calculator/img/obisity1.gif'
            elif bmi>=35 and bmi<=39.9:
                context['bmi_status'] = 'OBESITY CLASS 2'
                context['bmi_img'] = 'bmi_calculator/img/obisity2.gif'
            elif bmi>=40:
                context['bmi_status'] = 'OBESITY CLASS 3'
                context['bmi_img'] = 'bmi_calculator/img/over_weight.gif'
            
            if bmi >24.90:
                weight_to_reduce=(bmi-25)*height_m2
                if weight_to_reduce <100:
                    context['weight_to_reduce'] = round(weight_to_reduce,2)
            elif  bmi <18.50:
                weight_to_gain=(18.5-bmi)*height_m2
                if weight_to_gain <100:
                    context['weight_to_gain'] = round(weight_to_gain,2)
            
            context['bmi']=bmi 

            
            self.template_name="bmi_calculator/result.html"

            return render(request,template_name=self.template_name,context=context)

    def final_bmi_calculation (self,weight_kg,height_m2):
        bmi=weight_kg/height_m2
        return bmi

    def mtr_to_mtr_sqr(self,meters,centi_metersm):
        height = meters+(centi_metersm/100) 
        print(height)
        height_m2=height**2        
        return height_m2
    def foot_to_mtr_sqr(self,foots,inches):
        height_inch = (foots*12)+inches
        height_m2 = (height_inch*0.0254)**2
        return height_m2

    