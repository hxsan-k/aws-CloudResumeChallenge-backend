# Cloud Resume Challenge - Backend

This repository contains the backend code and infrastructure for my Cloud Resume Challenge project.

## Overview

The backend provides a serverless API that powers the visitor counter on my personal resume website. It is built using AWS Lambda, API Gateway, and DynamoDB.

## Features

- **Visitor Counter API:** Tracks and stores page views in DynamoDB.
- **Serverless Architecture:** Built with AWS Lambda and API Gateway.
- **Infrastructure as Code:** All resources defined and deployed via AWS SAM.
- **CI/CD Pipeline:** Automated testing and deployment using GitHub Actions.

## Tech Stack

- **Language:** Python 3.9 
- **AWS Services:** Lambda, API Gateway, DynamoDB, SAM (Serverless Application Model) 
- **CI/CD:** GitHub Actions

## Setup & Deployment

1. Clone this repo.
2. Configure AWS credentials with appropriate permissions.
3. Use AWS SAM CLI to build and deploy:
   ```bash
   sam build
   sam deploy --guided
4.	CI/CD is configured to automatically run tests and deploy on push to main.

⚠️Notes
	•	Unit tests for the Lambda function were causing issues with mocking DynamoDB, so only integration tests are enabled currently.
	•	The live API URL is output by the CloudFormation stack and used by the frontend site.

Thanks for checking out the backend! Feel free to explore or raise issues if needed.