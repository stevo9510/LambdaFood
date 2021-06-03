# Lambda Food
Project for S3-statically hosted website that invokes a Lambda Function via API Gateway fetch.  Backend is Aurora database storing "Food" that can be searched.

`src` folder contains the following subfolders
* **db** This contains a script to create the Aurora SQL database, as well as a schema diagram image.
* **Lambda** This includes the Python lambda function that can be invoked via an API (e.g., API Gateway).  This lambda function accepts a food search parameter, queries an Aurora database, and returns JSON  serialized results to the caller.
* **sanderson-project2** This corresponds to an S3 bucket that hosts a static website that can make asynchronous calls to an API and update the display.  It also holds some static image icons for food categories to be displayed based on the search results.
* **sanderson-project2-foodcontent** This corresponds to an S3 bucket that holds binary contents (images) related to data in the database.  The database can contain URLs associated with the food to display on the page.

## Architecture
![Image of Architecture](https://github.com/stevo9510/LambdaFood/blob/main/src/sanderson-project2/images/architecture-diagram.png)

## Database Schema
![Image of Schema](https://github.com/stevo9510/LambdaFood/blob/main/src/db/SchemaDiagram.png)
