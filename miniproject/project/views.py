from django.shortcuts import render #for interpolating the template with context data 
from django.http import HttpResponse #import response section from django
import os   #import operating system
import subprocess #import subprocess of operating system

def table(request):   #define a function
	return render(request,'table.html') #return the value

def index(request):#define a function
	return render(request,'index.html')#return the value

def alarms_clock(request):#define a function
	#response=subprocess.Popen('start explorer "F:\Bollywood\video songs"')
	response=os.popen('start explorer.exe shell:appsFolder\Microsoft.WindowsAlarms_8wekyb3d8bbwe!App')
	return HttpResponse(response) #return the value
# function to return calculator
def calc(request):#define a function
	response=os.system('start calc.exe')
	return HttpResponse(response) #return the value
# function to return camera
def camera(request):#define a function
	response=os.popen('start explorer.exe shell:appsFolder\Microsoft.WindowsCamera_8wekyb3d8bbwe!App')
	return HttpResponse(request) #return the value
# function to return cortana
def cortana(request):#define a function
	response=os.popen('start explorer.exe shell:appsFolder\Microsoft.Windows.Cortana_cw5n1h2txyewy!CortanaUI')
	return HttpResponse(request)
# function to return documents
def documents(request):#define a function
	#response=subprocess.Popen('start explorer "F:\Bollywood\video songs"')
	response=os.popen('start explorer "This PC:\\"')
	return HttpResponse(response)
# function to return facebook
def facebook(request):#define a function
	#response=subprocess.Popen('start explorer "F:\Bollywood\video songs"')
	response=os.popen('start explorer.exe shell:appsFolder\Facebook.Facebook_8xx8rvfyw5nnt!App')
	return HttpResponse(response)
# function to return feedback hub
def fd_hub(request):#define a function
	#response=subprocess.Popen('start explorer "F:\Bollywood\video songs"')
	response=os.popen('start explorer.exe shell:appsFolder\Microsoft.WindowsFeedbackHub_8wekyb3d8bbwe!App')
	return HttpResponse(response)
def Get_help(request):#define a function
	#response=subprocess.Popen('start explorer "F:\Bollywood\video songs"')
	response=os.popen('start explorer.exe shell:appsFolder\Microsoft.GetHelp_8wekyb3d8bbwe!App')
	return HttpResponse(response)
def chrome(request):#define a function
	response=os.system('start chrome.exe"')
	return HttpResponse(response)
def C_drive(request):#define a function
	response=os.popen('start explorer "C:\\"')

# define a function to retutn maps
def maps(request):
	#response=subprocess.Popen('start explorer "F:\Bollywood\video songs"')
	response=os.popen('start explorer.exe shell:appsFolder\Microsoft.WindowsMaps_8wekyb3d8bbwe!App')
	return HttpResponse(response)	
	
def solitaire(request):#define a function
	#response=subprocess.Popen('start explorer "F:\Bollywood\video songs"')
	response=os.popen('start explorer.exe shell:appsFolder\Microsoft.MicrosoftSolitaireCollection_8wekyb3d8bbwe!App')
	return HttpResponse(response)
def movies(request):#define a function
	#response=subprocess.Popen('start explorer "F:\Bollywood\video songs"')
	response=os.popen('start explorer.exe shell:appsFolder\Microsoft.ZuneVideo_8wekyb3d8bbwe!Microsoft.ZuneVideo')
	return HttpResponse(response)
def notepad(request):#define a function
	#response=subprocess.Popen('start explorer "F:\Bollywood\video songs"')
	response=os.system('start notepad.exe')
	return HttpResponse(response)
def Notepad(request):#define a function
	response=os.system('start notepad++.exe')
	return HttpResponse(response)

def photos(request):#define a function
	response=os.popen('start explorer.exe shell:appsFolder\Microsoft.Windows.Photos_8wekyb3d8bbwe!App')
	return HttpResponse(response)
def paint(request):#define a function
	response=os.popen('start explorer.exe shell:appsFolder\Microsoft.MSPaint_8wekyb3d8bbwe!Microsoft.MSPaint')
	return HttpResponse(response)
def explorer(request):#define a function
	response=os.system('start iexplore.exe')
	return HttpResponse(response)

def skype(request):#define a function
	response=os.popen('start explorer.exe shell:appsFolder\Microsoft.SkypeApp_kzf8qxf38zg5c!App')
	return HttpResponse(response)
def sticky(request):#define a function
	response=os.system('start explorer.exe shell:appsFolder\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe!App')
	return HttpResponse(response)
def tips(request):#define a function
	response=os.system('start explorer.exe shell:appsFolder\Microsoft.Getstarted_8wekyb3d8bbwe!App')
	return HttpResponse(response)

def vRecorder(request):#define a function
	response=os.system('start explorer.exe shell:appsFolder\Microsoft.WindowsSoundRecorder_8wekyb3d8bbwe!App')
	return HttpResponse(response)

def wordpad(request):#define a function
	response=os.popen('start wordpad.exe')
	return HttpResponse(response)

def weather(request):#define a function
	response=os.popen('start explorer.exe shell:appsFolder\Microsoft.BingWeather_8wekyb3d8bbwe!App')
	return HttpResponse(response)

def wmplayer(request):#define a function
	response=os.popen('start wmplayer.exe')
	return HttpResponse(response)

def PC(request):#define a function
	response= os.popen('start explorer "This PC:\\"')
	return HttpResponse(response)
