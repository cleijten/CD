## Assignment objectives: ##
* Run a server at Digital Ocean
* Connecting over SSH
* Learn Ubuntu commands
* Deploy Flask app

## Workflow: ##
* Create a flask app and test 
* Write a .yml workflow that tests the Flask app and if the test is successful connect to VPS ands show the latest version of the app

For the Flask app I just used the same set up af for the farm exercise.

The workfow .ym file contains 3 sections:
* It runs from the git push action I execute locally in Visual Studio. It installs requirements.txt (which contains the version of pytest) and runs the test. For deployment of the app first the test needs to be OK.
* For deployment I used appleboy because it looks simple and clean. It picks up the secrets that are stored on Github. 
* The script that is run after you get the connection to the server. In that script you do a git pull to get the latest changes in the app and you do a restart of your .service

## Problems I ran into ##
* Where to store the SSH keys. There is a private and a public SSH key. I had some struggles to put them in the right place.
* I forgot do a git clone on the server, so a git pull would not do anything
* The .service file contained the wrong path to the gunicorn bin
