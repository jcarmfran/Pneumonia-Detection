# Pneumonia-Detection
This end-to-end projects culminates in a web application that takes a patient's x-ray of their lungs and detects if they are developing signs of pneumonia. 

## Running Application
### Local Deployment
1. Navigate to folder Clone the repository

```
git clone https://github.com/jcarmfran/Pneumonia-Detection.git
```

2. Create and activate `conda` environment 

```
conda create -n pneu-venv python=3.8 -y
```
```
conda activate pneu-venv
```

3. Install the requirements

```
pip install -r requirements.txt
```

4. Run the application
```
python app.py
```

Navigate to `localhost:8080` in your browser to view the application!

### Utilizing Data Version Control (DVC)
If you decide to modify the model and wish to utilize DVC, you should start by downloading it [here](https://dvc.org). 

DVC needs to be initialized by navigating the application folder and executing the following command.

```
dvc init
```

After modifying the model, you can reinitialize the pipeline.

```
dvc repro
```

Enter the following to view a diagram of the executed pipeline.

```
dvc dag
```

### Deploying to the Cloud via Github Actions
There are a few ways you can deploy this application to the cloud.

#### AWS: ECR
1. Login into your AWS console
2. Create IAM user for deployment and give the following permissions:
    - AmazonEC2ContainerRegistryFullAccess
    - AmazonEC2FullAccess
3. Build the docker image from source
4. Create ECR repo to store docker image
5. Push the docker image to ECR
6. Build and launch EC2 instance
    In our case, we'll build the EC2 with Ubuntu
7. Open EC2 and install docker
```
#optional

sudo apt-get update -y

sudo apt-get upgrade


#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```
7. Configure EC2 as self-hosted runner
    In the projects Github page, navigate to 
    -> Settings 
    -> Actions 
    -> Runner 
    -> New self hosted runner 
    -> choose os 
    -> then run commands one by one
8. Setup your Github secrets
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - AWS_REGION
    - AWS_ECR_LOGIN_URI
    - ECR_REPOSITORY_NAME

#### AZURE
Save pass:

Run from terminal:
```
docker build -t chickenapp.azurecr.io/chicken:latest .
```
```
docker login chickenapp.azurecr.io
```
```
docker push chickenapp.azurecr.io/chicken:latest
```
Deployment Steps:
1. Build the Docker image of the Source Code
2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure
4. Pull the Docker image from the container registry to Web App server and run

### Supporting Github Actions YAML Documentation
AWS: 
    https://docs.github.com/en/actions/deployment/deploying-to-your-cloud-provider/deploying-to-amazon-elastic-container-service

GCP:
    https://docs.github.com/en/actions/deployment/deploying-to-your-cloud-provider/deploying-to-google-kubernetes-engine