# Model Deployment Using Flask/Docker

I started this project to apply what I taught myself online about Flask and Docker by deploying a scikit-learn machine learning model.
This project consists of three parts.

### Part 1: Machine Learning Model
Here, I train a machine learning model on the Stock Market data from [Introduction To Statistical Learning](https://www.statlearning.com/). 
For a more in depth analysis of the data, look  at my repo [here](https://github.com/sonuranjitjacob/ISLR-Python/blob/main/Chapter%204%20-%20Classification.ipynb). 

- `train.py` is used to train the model and save it using pickle to `model.bin`. 
- `test.py` contains the code I used to test the model.

The accuracy of the model can probably be improved (it has an accuracy of 52% using Logistic Regression and improves to 58% using Quadratic Discriminant Analysis), 
but the main aim of this project is to learn to deploy models using Flask/Docker. 


### Part 2: Deployment using Docker

The `dockerfile` creates the image and installs the required dependencies within the container. To build the Docker file, use the following command:  

`docker build -f dockerfile -t docker_tutorial`

This creates an image with the name `docker_tutorial`

To run the docker container, use the following command:  

`docker run -v /home/tester/Sonu/docker_data/:/root/src/docker_data -ti docker_tutorial /bin/bash -c "cd src && source activate ml && python train.py"`

Here, 
- `-v` mounts the data on the local system (`/home/Sonu/docker_data/`) to the Docker container (`/root/src/docker_data`)
- `-ti` is used to give a tag to the Docker image
- `-c` indicates the CPU shares 


Once the container is running, we activate the Python environment named `ml` and run the `train.py` file. 

As we've mounted the data on the local machine to folder on the Docker container, once the model is trained it is stored on the local machine 
in the `docker_data` folder.

### Part 3: Deployment using Flask
Here, I deploy the model using Flask.  
`app.py` contains the relevant code for the Flask module.  

The web GUI is yet to be completed. To get a prediction using Flask, run the `app.py` program and the following command:

`curl -X GET 'http://127.0.0.1:9999/predict?Lag1=0.381&Lag2=-0.192&Lag3=-2.64&Lag4=-1.055&Lag5=5.01&Volume=1.19'`

Here, the url is obtained using the port specified in `app.py`. I input the predictor variables for the model through the command line. 

The output should looks like [this](project/img.png)


The `dockerfile` can be used create an image and train a model on any system using a container built using this image. 
This model can be used to make predictions either by modifying the `test.py` or using inputting the predictor variables through Flask. 
 
