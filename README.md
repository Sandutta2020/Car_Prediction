<h1 align ="center">  Car-Price-Prediction </h1>

```
Base Folder ----
        |conf : For storing all the configuration file
        |data : The Input data src file
        |model : For Storing the model
        |report For generating the output
        |src : For src code/Business logic	
        |static : For storing all the css and js file
        |template : for storing all the template html file
        |app.py  : FastAPI logic written file and starting point of FastAPI 
        |main.py : Main logic while running from background
        |params.yaml : for storing Necessary parameter file
        |procfile : necessary file for cloud deployment
        |Readme.md :For Git Documentation
        |requirements.txt : All the necessary packages
```

### to install Dependency ,Please run the following commands

```
conda create -n envName python =3.7
conda activate envName
pip install -r requirements.txt
```

## to run Flask server 

``` python app.py ```

On successful run it Flask will serve 

``` http://127.0.0.1:8000/ ```

## Code lynting using black

``` black app.py```


### To run application 
``` python app.py ```

[Inspired by Krish Naik](https://github.com/krishnaik06/Car-Price-Prediction)