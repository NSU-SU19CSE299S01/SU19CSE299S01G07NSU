from django.shortcuts import render


def sylhet(request):
    return render(request,'tour/Sylhet.html')



def barisal(request):
    return render(request, 'tour/Barisal.html')


def rajshahi(request):
    return render(request,'tour/Rajshahi.html')