GUI
https://kivy.org/doc/stable/gettingstarted/installation.html

Create virtual environment¶
Create a new virtual environment for your Kivy project. A virtual environment will prevent possible installation conflicts with other Python versions and packages. It’s optional but strongly recommended:

Create the virtual environment named kivy_venv in your current directory:

python -m virtualenv kvenv
Activate the virtual environment. You will have to do this step from the current directory every time you start a new terminal. This sets up the environment so the new kvenv Python is used.

For Windows default CMD, in the command line do:

kvenv\Scripts\activate
If you are in a bash terminal on Windows, instead do:

source kvenv/Scripts/activate
If you are in linux or macOS, instead do:

source kvenv/bin/activate
Your terminal should now preface the path with something like (kvenv), indicating that the kvenv environment is active. If it doesn’t say that, the virtual environment is not active and the following won’t work.