This repository is about creating simple python scripts and using Task Scheduler to automate those scripts which will automatically attend your classes according to your time table.
By understanding this concept, you can use to automate your other stuffs too.

**What is this project about and why did I make this?**

This project is about a script that would attend your classes and you just need to have your computer started for it and connected to the Internet. That’s it! Isn’t that exciting? I’ll show you how I did that.
So, I was looking for some python language courses on youtube and I came across a video, titled as ‘Web automation in python for beginners’ by Hitesh Choudhary. I find this youtube channel to be amazing and I recommend you to check it out. This title excited me and I thought to have a watch. I found that to be amazing and thought to have a shot at it, though I was looking to start with python. 

 ![image](https://user-images.githubusercontent.com/55484263/109388618-3c2d7280-792e-11eb-9263-ae2d0d91c08a.png)

I watched that video completely and thought ‘what if I do the same that would attend my University classes and add the scripts to cronjobs to automatically run the scripts according to my time table?’. And this is what I did. (if you don’t know what’s a cronjob, don’t worry, I’ve talked about it below in this blog.)


**Let’s jump in and start building our script.**

First let’s download all the necessary things-
1.	First things first, you need to have to python installed on your computer. (obviously because we are building python script.)
    If you do not have python installed, go and download the currently latest version of python from here. -->  https://www.python.org/downloads/
Install it and store it on any disk you want.

2.	Now it’s time to download the webdriver. Webdrivers are the tools to test web automations.

![image](https://user-images.githubusercontent.com/55484263/109389183-6e8c9f00-7931-11eb-8646-85c95719d011.png)

  a.	You can download webdrivers either using CMD or POWERSHELL. The link to the cmd and powershell commands is here. 
     If you are a windows user, you need to download a package manager first. To download chocolatey package manager, go to           ‘https://chocolatey.org/install’ and copy the powershell command and run it in powershell and your choco package manager will       be installed. 

![image](https://user-images.githubusercontent.com/55484263/109389195-7c422480-7931-11eb-9c4d-4141a176d32f.png)

Now run ‘choco install chromedriver’ in powershell.
After doing this, and compiling your python script, it may ask to set the path of chrome drivers. At this point, I was confused and looked on google for help and I used that method and that was simple for me. It is discussed in the next point. 

b.	If you are using chrome, then download the chrome webdriver from here.  https://chromedriver.chromium.org/downloads	
Just download the required web driver and place it in the python folder. (folder where your python files are installed.)

![image](https://user-images.githubusercontent.com/55484263/109389208-895f1380-7931-11eb-818b-f51b2cfed268.png)

This was fairly simple. 

3.	And now, the final thing. Now you have to install a module- ‘selenium’. I don’t know much about the modules in python, because I have just started learning python, and this project is just for fun. But, what I read about this module is, this module is used for web automation testing.

To install selenium, open your terminal and-
        i.	If you are a windows user, type – ‘pip install selenium’
        ii.	If you are a mac or linux user type – ‘pip3 install selenium’ 
        
 ![image](https://user-images.githubusercontent.com/55484263/109389221-a0056a80-7931-11eb-8d6d-bbd7c7315264.png)


Now we have everything installed and it’s time to write our script.


**Writing our python script-**

(the scripts are available under ‘SCRIPTS’ folder)
What’s the important thing to keep in mind is, that this program will find a specific element and will click it. That’s it. No rocket science. Just find element and click it.




**The final script will look something like this- **

![image](https://user-images.githubusercontent.com/55484263/109389239-bf9c9300-7931-11eb-8ac7-21b12978a932.png)

This script is for Chandigarh University’s collaboration with BlackBoard platform.
But I hope, you have got the idea, how to build the related script.



**Now automating the script to run on its own on the desired time-**

For this we will use ‘Task Scheduler’. Here, we will create our cronjobs. 
I know its time to talk a bit about cronjobs. So, cronjobs are the tasks that are run automatically on the time which you set. Yes, that’s it! So, if you set a script to run at 10:00 pm, it would run at 10:00 pm and you don’t need to do anything. You still need to have your computer turned on though, duh.



**Setting our python scripts as cronjobs-**

1.	Search for ‘Task Scheduler’ at the taskbar and select that option.
2.	
![image](https://user-images.githubusercontent.com/55484263/109389260-e22eac00-7931-11eb-9be6-c8cdbae5c805.png)
2.	Though its not necessary but create a folder for your cronjobs, because it will organize your cronjobs and you can tweak them, modify them or even remove them easily. You don’t have to search through a number of cronjobs already running by your system. Our computer system already has a number of cronjobs running.
Create a folder below ‘Task Scheduler Library’ by right-clicking on it and selecting ‘New Folder’ option.

![image](https://user-images.githubusercontent.com/55484263/109389267-ea86e700-7931-11eb-9fe3-d2f2ee905b20.png)

![image](https://user-images.githubusercontent.com/55484263/109389274-ee1a6e00-7931-11eb-85db-6393e53eaa53.png)
3.	Now under the newly created folder, we have to create a new task.
We can do this by selecting ‘Create Task…’ option under the ‘Actions’ category which is at the right panel of our screen.

![image](https://user-images.githubusercontent.com/55484263/109389287-f8d50300-7931-11eb-99c5-14ea60761ce0.png)


**4.	Now we have to set the required options for our cronjob to run.**

    i.	Under ‘General’ tab, fill the name and the description about your task, and select correct windows version In the ‘Configure for:’ dropdown menu. 
    
![image](https://user-images.githubusercontent.com/55484263/109389303-09857900-7932-11eb-9cbe-7fe1aa43aa28.png)

   ii.	Now come to the ‘Triggers’ tab. Select the ‘New’ button and fill the ‘Start date and time’ for your cronjob, and select the ‘Daily’ option if you want your cronjob to run daily.
   
![image](https://user-images.githubusercontent.com/55484263/109389311-14d8a480-7932-11eb-8028-f0ba0666c805.png)

  iii.	Its time for the ‘Actions’ tab where you have to select which python script to run.
  
![image](https://user-images.githubusercontent.com/55484263/109389321-1a35ef00-7932-11eb-950d-2dc2604952b3.png)

  iv.	now come to the ‘Conditions’ tab. This time is important and it had cost me around half an hour, because it has some options which decides when to run your script and when not to.
So, what necessary is, just uncheck everything.

![image](https://user-images.githubusercontent.com/55484263/109389324-20c46680-7932-11eb-8fe7-2c6b3b4ab69b.png)



**And that’s it! Our cronjobs are also set up.**
**So I think, its pretty much for today.**
**I’ll try my best to keep this updated and will some more cool things to you very soon.**
**Till then, bye-bye.**
