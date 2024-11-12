from django.shortcuts import render
from.forms import RgistrationForm
# Create your views here.


def viewReg(request):
  form=RgistrationForm(request.POST)
  if form.is_valid():
    try:
        return redirect("")
    except:
       pass
  return render(request,"std/registration.html",{"form":form})
