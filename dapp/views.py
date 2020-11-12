from django.shortcuts import render, redirect, HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status


from dapp.models import Dapp
from dapp.serializers import DappSerializer
from rest_framework.decorators import api_view
from .forms import DappForm

# Create your views here.
detail= {}

def index(request):
    if request.method == 'POST':
        form = DappForm(request.POST)

        if form.is_valid():
            redirect('index')
    else:
        form = DappForm()
        context = {'form':form}

    return render(request, 'dapp/index.html', context)

#haaavooooooooo!!!!!!!!!!!!!




def submission(request):
    return render(request, 'dapp/xyz.html')

def desk(request):
    global detail
    return JsonResponse(detail)





def create_user(request):
    if request.method =='POST':
        cname = request.POST['name']
        cemail = request.POST['email']
        cphonenumber = request.POST['phonenumber']
        cdescription = request.POST['description']

        flag=True
        message = {}
        details = {}
        mock = ["!","@","#","$","%","^","&","*","(",")","-","_","=","+","<",",",">",".","?","/",";",":","'","[","{","]","}","\",","|"]

        
        

        for x in mock:
            if x in cname:
                flag=False

        if(not flag):
            message.update({"nInfo": "name not valid"})
        elif len(cname) < 3:
            flag=False
            message.update({"nInfo": "minimum 3 characters"})
        else:
             message.update({"nInfo": ""})
        


        if not "@gmail.com" in cemail:
            flag=False
            message.update({"eInfo": "email not valid"})
        else:
            message.update({"eInfo": ""})


        if len(str(cphonenumber)) < 10:
             flag=False
             message.update({"pInfo": "invalid phone number"})
        else:
            message.update({"pInfo": ""})

        if len(cdescription) < 20:
            flag=False
            message.update({"dInfo": "Minimum 20 characters"})
        else:
            message.update({"dInfo": ""})

        
        
        if flag:
            Dapp.objects.create(
            name=cname,
            email=cemail,
            phonenumber=cphonenumber,
            description=cdescription
            )

        if flag:
            details.update({"name": cname, "email": cemail, "phonenumber": cphonenumber})
            global detail
            detail = details
           

        message.update({"flag": flag})
        
           
    return JsonResponse(message)



   


@api_view(['GET', 'POST'])
def dapp_list(request):
    if request.method == 'GET':
        dapp = Dapp.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            dapp = dapp.filter(name__icontains=name)

        dapp_serializer = DappSerializer(dapp, many=True)
        return JsonResponse(dapp_serializer.data, safe=False)
        # 'safe=false for objects serialization

    elif request.method == 'POST':
        dapp_data = JSONParser().parse(request)
        dapp_serializer = DappSerializer(data=dapp_data)
        if dapp_serializer.is_valid():
            dapp_serializer.save()
            return JsonResponse(dapp_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(dapp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def dapp_detail(request, pk):
    try:
        dapp = Dapp.objects.get(pk=pk)
    except Dapp.DoesNotExit:
        return JsonResponse({'message': 'The data entered doesnot exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
        dapp_serializer = DappSerializer(dapp)
        return JsonResponse(dapp_serializer.data)

    elif request.method =='PUT':
        dapp_data = JSONParser().parse(request)
        dapp_serializer = DappSerializer(dapp, data=dapp_data)
        if dapp_serializer.is_valid():
            dapp_serializer.save()
            return JsonResponse(dapp_serializer.data)
        return JsonResponse(dapp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        dapp.delete()
        return JsonResponse({'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

