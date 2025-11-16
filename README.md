# DevGrowth
Web app for new developers to track daily progress - including what they worked on, what they learned, and what they were stuck on. Users can add daily entries about their work. The purpose is to help beginners reflect each day, build consistency, and visualize growth over time.

## Tech Stack
- **Frontend:** Vue.js
- **Backend:** AWS Lambda + API Gateway 
- **Database:** AWS DynamoDB
- **Static Hosting/Storage:** AWS S3

## Frontend Setup (Vue.js)
See frontend/README.md

## Data Model
- **user_id** *(String, Partition Key)* - Unique ID for each user
- **date** *(String, Sort Key)* - Date of the log entry
- **worked_on** *(String)* - What the user worked on
- **learned** *(String)* - What the user learned
- **stuck_on** *(String)* - Issues or blockers

## Team Members
- Allison Coates
- Mai Nguyen
