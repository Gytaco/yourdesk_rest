# yourdesk_rest
Your Desk University Setup <br>
Rest example for Vercel and Planetscape setup <br>


This is the dataset for the following Youtube Video on YourDesk University in June 2023.
You can watch the video here https://www.youtube.com/watch?v=3A6w-lKPec8 <br>
This is based on Windows users using Visual Studio Code

# Initial Things
Sign up to Vercel & PlanetScale <br>
Vercel https://vercel.com/ <br>
PlanetScale https://planetscale.com/ <br>
Clone the Repo

# Setup Environment from scratch
To create the environment, dont clone the repo. <br>
Create a new Python Environment open Powershell or Windows terminals

python -m venv yourdesk <br>
yourdesk\Scripts\activate.ps1 <br>
python.exe -m pip install --upgrade pip <br>
pip install FastAPI <br>
pip install uvicorn <br>
pip install PyMySQL <br>
pip freeze > requirements.txt <br>

This will have a full setup environment. <br>
You can then run the webserver with the following code. <br>
uvicorn main:app --reload <br>
To look at the documented API <br>
http://YOURURL/docs#/default/

# Setup Environment from fork
If you want to grab the current version. <br>
Fork the Repo to your Repository <br>
Install packages <br>
Setup your python environment <br>
pip install -r requirements.txt <br>

Run uvicorn to run local or run in debug mode
uvicorn main:app --reload

# Notes
I have included an excel file and dynamo DynaWeb script so you can see some examples of how this works.
Please make sure you update the URLs of the queries with your own.
