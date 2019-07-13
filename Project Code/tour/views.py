from django.shortcuts import render


def sylhet(request):
    return render(request,'tour/Sylhet.html')



def barisal(request):
    return render(request, 'tour/Barisal.html')


def rajshahi(request):
    return render(request,'tour/Rajshahi.html')




def saint_martin(request):
    return render(request, 'tour/Saint Martin.html')

def khulna(request):
    return render(request,'tour/Khulna.html')

def chittagong(request):
    return render(request,'tour/Chittagong.html')

def dhaka(request):
    return render(request,'tour/Dhaka.html')