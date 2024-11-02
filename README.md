# REGEX-MATCHER &  EMAIL VALIDATOR
"Regex Matcher and Email Validator: A single web application featuring two tools that enable users to test regular expressions and validate email addresses seamlessly on one page."

 1.The application is built using the Flask framework and is developed in Python, providing a lightweight and easy-to-use environment for creating web applications.

 2.The user interface consists of three HTML files: welcome.html, regex_matcher.html, and email_validator.html, which collectively incorporate the Regex Matcher and Email 
    Validator functionalities, styled using basic CSS.

 3.The project is developed using VS Code, leveraging its features for efficient coding and debugging while ensuring a smooth development workflow.

# Instructions to Run the Application:
   
## Set up your environment:

  1.Make sure you have Flask installed. You can install it via pip if you haven't already:

    "pip install Flask"

## File Structure:
 
1.Ensure your file structure looks like this:
  
    your_project/
     ├── app.py
     ├── templates/
     │   ├── welcome.html
     │   ├── regex_matcher.html
     │   └── email_validator.html

##  Run the application:

1.Navigate to the directory containing app.py and run:

  "python app.py"

2.Open your browser and go to http://127.0.0.1:5000/ to see the application.


# Server Setup and Application Deployment Guide

## Setting Up the Server
1.Start by choosing your server environment (like AWS, DigitalOcean, or your local machine).

2.For AWS, launch an EC2 instance. Select the appropriate operating system and instance type based on your needs.

3.Make sure to configure security groups to allow SSH access for your application.

## Transferring Files
1.Use scp or rsync to transfer your application files from your local machine to the server.

2.Here’s a quick command for scp:

  "scp -r /path/to/local/files username@server_ip:/path/to/remote/directory".

3.If you prefer a GUI, consider using tools like FileZilla for easier file transfers.

## Update and Upgrade the Server

1.To ensure the server is up-to-date, run the following commands:

  "sudo apt update"
  "sudo apt upgrade"

## Install Python and Pip

1.If Python and pip are not already installed on the server, install them with:

    "sudo apt install python3-pip"

## Save Current Environment Packages

1.If you need to create a requirements.txt file listing all packages in your current environment, use:

   "pip freeze > requirements.txt"

## Install Application Dependencies

1.After transferring the application files to the server, install the required Python packages listed in requirements.txt.

   "pip install -r requirements.txt"

# Running and Managing the Application

## Run the Application in the Background

1.To run the Python application in the background, use the nohup command:

   "nohup python3 app.py &"
  
2. The & allows the process to run in the background, and nohup prevents it from stopping when you disconnect from the server.

## Check Background Processes

1. To see all background processes for the current user, run:

    "top -u $USER"

## Terminate a Process by PID

1. If you need to stop a specific process, use the kill command with the Process ID (PID):

   "kill <PID>"

## Forcefully Terminate a Process

1.To forcefully terminate a process, use:

  "kill -9 <PID>"

2.Replace <PID> with the actual Process ID of the application you want to terminate.



 


