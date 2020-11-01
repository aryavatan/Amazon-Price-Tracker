# Amazon Price Tracker
 A light-weight python script that can be scheduled to run in the background to send you email notifications when your favourite (Canadian) Amazon items go on sale. This application currently only works on Windows with Canadian Amazon (amazon.ca) items. Additionally, the email notifications only work with gmail accounts at this time.


## Installation Instructions
Follow the steps below to correctly install the application on your Windows computer:

1. Make sure you have Python (Version 3.8 or higher) installed in your system. You can install Python from the Microsoft Store on your Windows computer.

2. Download or clone the Amazon-Price-Tracker folder to your preferred installation location.

3. Open the Amazon-Price-Tracker folder in CMD or terminal and type `pip install -r requirements.txt`

4. In the `Settings.json` file, find the `email-login` field and add your gmail username and password in the empty quotations (Do not remove the quotations).

5. Google search "My user agent" and copy the response from Google. In the `Settings.json` file, find the `User-Agent` field and paste the response from Google in the empty quotations.
Example: `{"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'}`

6. In order to receive email notifications from the Amazon-Price-Tracker, you have to give access to the application. If you DO NOT have 2-Step Verification enabled on your Google account, go to your Google Account settings and enable `Less secure app access`. If you DO have 2-Step Verification enabled on your Google account, go to your `App passwords` in your Google Account settings and generate a new password for 'Mail' on 'Windows Computer'. Copy the generated password, and paste it in the `password` field in the `Settings.json` file.

7. To track the prices of your favourite items, copy the URL of the product on Amazon.ca and paste it in quotations in the `watchlist` field in the `Settings.json` file. This field is a list, therefore, you need to add a comma (,) inbetween each entry (Note: do NOT add a comma on the final entry). When you are finished, it should look something like this: `"watchlist" : ["https://www.amazon.ca/gp/product/...", ...]`


In order to schedule this application to run everyday (or on any custom schedule you like) follow the steps below:

1. Open `Task Scheduler` on your Windows computer.

2. In the 'Actions' menu, select the option `Create Task...`

3. In the 'General' tab, enter 'Amazon-Price-Tracker' as the name, and (optionally) give a description.

4. Open CMD and enter the command `python -c "import sys; print(sys.executable)"`. Copy the outputted path to your python executable.

5. Back in the new Task dialog of Task Scheduler, go to the 'Actions' tab and press 'New...'. Paste the copied path from the previous step in the `Program/script` field. Add the argument `Scraper.py` in the `Add arguments (optional)` field. Lastly, copy the installation folder path (i.e., the folder containing Scraper.py) and paste it in the `Start in (optinal)` field. And press OK.

6. Now go to the 'Triggers' tab and press 'New...'. In this dialog, you can set how often you want this application to run. One important thing to note is that the application cannot run if your computer is asleep or shut down. I suggest setting a daily trigger during a time when your computer is normally turned on.

7. Go to the 'Settings' tab and make sure `Stop the task if it runs longer than` is enabled and set to 1 hour. Also make sure the option `If the running task does not end when requested, force it to stop` is enabled.

8. You are finished, you can press OK and close Task Scheduler.


## Manually Running Application
In order to manually run the application, open the Amazon-Price-Tracker folder in CMD or terminal and type `python Scraper.py`