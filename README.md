# Pneumonia Detection Web App

This application leverages a deep learning model trained on chest X-rays to assess whether a patient’s X-ray shows signs of pneumonia. Users can easily upload their X-ray images, and the app provides an immediate assessment.

## Features:

- **Chest X-ray Assessment**: Upload your chest X-ray image, and our model will analyze it for pneumonia indicators.
- **Flask-Based Web Interface**: The web app is built using Flask, making it lightweight and easy to deploy.
- **Local Deployment Instructions**: Want to run the app on your local machine? We’ve got you covered! Check out the step-by-step instructions in the repository.
- **AWS Deployment via GitHub Actions**: For those interested in deploying the app on AWS, we provide detailed guidance using GitHub Actions.

Feel free to explore the code, contribute, and help improve pneumonia detection using this powerful tool! 

## Running the Application

### Local Deployment
1. Navigate to the folder you would like to clone the repository to and execute the following:

```
git clone https://github.com/jcarmfran/Pneumonia-Detection.git
```

2. Create and activate `conda` environment.

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

### Deploying to AWS via Github Actions

1. Login into your AWS console
2. Create IAM user for deployment and give the following permissions:
    - AmazonEC2ContainerRegistryFullAccess
    - AmazonEC2FullAccess
3. Build the docker image from source
4. Create ECR repo to store docker image
5. Push the docker image to ECR
6. Build and launch EC2 instance
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
    Then choose the OS of your choice (Ubuntu is suggested). Carefully read and follow the instructions listed on the page.
8. Setup your Github secrets
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - AWS_REGION
    - AWS_ECR_LOGIN_URI
    - ECR_REPOSITORY_NAME

You should be able to view the application by visiting your EC2 instance's IP/URL.