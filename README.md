# Cloud Resume Challenge - Backend

This repository contains the backend components for my Cloud Resume Challenge project.

## Overview

The backend is built using AWS Lambda functions (Python) and API Gateway to serve API requests. It handles visitor count tracking and stores data in DynamoDB. The infrastructure is defined as code using AWS SAM (Serverless Application Model).

## Features

- Lambda function to handle API requests
- DynamoDB table for storing visitor counts
- Infrastructure as code using AWS SAM templates
- API Gateway integration with Lambda
- Simple REST API endpoint to increment and retrieve visitor count

## Technologies

- AWS Lambda (Python 3.13)
- Amazon API Gateway
- Amazon DynamoDB
- AWS SAM

## Usage

1. Deploy the stack using SAM CLI:
   ```bash
   sam deploy --guided
2. The API endpoint will be available after deployment.
3. Send GET requests to the /hello endpoint to retrieve and increment the visitor count.

## Repository Structure

- template.yaml – AWS SAM template defining resources
- hello_world/ – Lambda function code directory
- events/ – Sample event files for local testing
