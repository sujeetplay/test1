
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm,SnippetForm

# Create your views here.

def contact(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            email=form.cleaned_data["email"]
            category = form.cleaned_data["category"]
            subject=form.cleaned_data["subject"]
            body=form.cleaned_data["body"]
            print("the name is "+name)
            print("the email is "+email)
            print("the category is "+category)
            print("the subject is "+subject)
            print("the body is "+body)

    form=ContactForm()
    return render(request,"form.html",{"form":form})
    #return HttpResponse("contact view")

def snippet_detail(request):
    if request.method=="POST":
        form=SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            name=form.cleaned_data["name"]
            body=form.cleaned_data["body"]
            print("WORKING!!!!")
            print("The name is "+name)
            
            import time, datetime, sys, os
            from datetime import datetime
            from selenium import webdriver
            from selenium.webdriver.common.keys import Keys
            from selenium.common.exceptions import TimeoutException
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            from selenium.webdriver.common.by import By
            from selenium.webdriver.chrome.options import Options

            userID="sgorahava"
            filename="Scripts"
            CHROME_PATH = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
            CHROMEDRIVER_PATH = 'C:\\Users\\'+userID+'\\'+filename+'\\chromedriver.exe'
            WINDOW_SIZE = "1920,1080"

            chrome_options = Options()  
            #chrome_options.add_argument("--headless")  
            chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
            chrome_options.add_argument("disable-gpu")
            chrome_options.add_argument("disable-infobars")
            chrome_options.add_argument("--disable-notifications")
            #chrome_options.add_argument("--kiosk")

            chrome_options.binary_location = CHROME_PATH

            browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,chrome_options=chrome_options)
            browser.get("https://www.google.com")
                
            elements = browser.find_elements_by_css_selector('#lst-ib')
            if not elements:
                print("NO SUCH ELEMENT FOUND!")
                print("Fatal Error:Please perform all tasks manually")
            else:
                browser.execute_script('document.getElementById("lst-ib").onkeypress=function(){return false;}')
                browser.execute_script('document.getElementById("lst-ib").value = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"')
                                       
            ##    item1 = browser.find_element_by_css_selector('#lst-ib')
            ##    item1.send_keys('This is some very long text'+Keys.TAB)
            print("the body is "+body)












            
#---------------------------------------
    form=SnippetForm()
    return render(request,"form.html",{"form":form})
