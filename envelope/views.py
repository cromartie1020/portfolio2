from django.shortcuts import render, redirect
#from .models import Envelope
#from .forms import EnvelopeForm
'''
def envelope_view(request):
    
    form= EnvelopeForm()
    if request.method =='POST':
        form=EnvelopeForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('todo')
    
        
    return render (request,'envelope/envelope_form.html',{'form':form})            
'''