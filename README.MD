# Soccer Stats
Creating a blog of cool visualizations and forecasts for the world's greatest sport

## Developer Setup
### Create Virtual Environment
Mac: python3 -m venv env  
Windows: python -m venv c:\repository_path\env

### Startup
source env/bin/activate

### Install Dependencies
pip3 install -r requirements.txt

### Run app
python flask_main.py  
Navigate to http://127.0.0.1:5000/ in a web browser

#### Other things to know
Currentlly I'm not pushing jpeg files to git.  In the future we'll want to put them on s3, but for now we'll keep them local in the static directory.