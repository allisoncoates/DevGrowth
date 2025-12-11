# DevGrowth
Web app for new developers to track daily progress - including what they worked on, what they learned, and what they were stuck on. Users can add daily entries about their work. The purpose is to help beginners reflect each day, build consistency, and visualize growth over time. *Created for Introduction to Cloud Computing at UNO.*

## Features
- **Daily Logging:** Users can submit a daily entry with fields for "Worked On", "Learned", and "Stuck On"
- **Future Date Protection:** Logic prevents users from logging entries for future dates
- **CRUD Functionality:** Full support to Create, Read, Update, and Delete entries
- **Streak Tracker:** A counter in the header to visualize consecutive days of tracking

## Tech Stack
- **Frontend:** Vue.js (TypeScript, Vite) running locally
- **Backend:** AWS API Gateway (HTTP API) & AWS Lambda (Python 3.12/Boto3)
- **Database:** AWS DynamoDB

## Cloud Services (AWS):
- **Lambda:** 4 functions (Get, Add, Update, Delete)
- **API Gateway:** Exposes Lambda functions via HTTP routes (GET, POST, PUT, DELETE)
  - *CORS is configured in API Gateway to allow cross-origin requests from localhost to enable local development*
- **DynamoDB:** NoSQL database table (DevGrowth)

## Data Model
Table Name: DevGrowth
- **user_id** *(String, Partition Key)* - Unique ID for each user
- **date** *(String, Sort Key)* - Date of the log entry
- **worked_on** *(String)* - What the user worked on
- **learned** *(String)* - What the user learned
- **stuck_on** *(String)* - Issues or blockers

## Setup & Installation
As of 12/11/2025, the AWS cloud services have been turned off. In order to run this app:
- Set up a database in DynamoDB using the Data Model section above
- Set up Lambdas with Python 3.12 using the get.py, add.py, update.py, and delete.py files in the backend folder
  - Ensure each Lambda’s IAM role has permission to the AmazonDynamoDBFullAccess policy
- Set up an API Gateway with GET, POST, PUT, and DELETE /entries routes and integrate each route with the respective Lambda
- Get the API’s Invoke URL and add it to the frontend files App.vue, NewEntry.vue, and PastEntries.vue in the API_URL variable

Prerequisites
- Node.js installed (v18+ recommended)

Running the Frontend
1. Clone or Download the repository
2. Open a terminal in the project root
3. Go to the Frontend folder and install dependencies:
```
cd frontend
npm install
```
4. Start the development server:
```
npm run dev
```
5. Open your browser to the local URL: `http://localhost:5173`

## Future Improvements
- **User Authentication:** Replace the hardcoded DemoUser with Amazon Cognito for real user logins
- **Hosting:** Deploy the frontend to AWS S3 or CloudFront for a full cloud experience

## Team Members
- Allison Coates
- Mai Nguyen
