# Concept Check

## 1. What is a Resource Group in Azure, and why do we use one?

A Resource Group is a container that holds related Azure resources such as virtual machines, storage accounts, and databases. We use it to organize, manage, and monitor resources for a project in one place.

## 2. What is the difference between a virtual environment and a global Python installation?

A global Python installation is shared by all projects on a computer. A virtual environment creates an isolated Python environment for a specific project, allowing different projects to use different package versions without conflicts.

## 3. Why is version control important from Day 1 of a project?

Version control helps track changes in code, enables collaboration among team members, provides backup of project history, and allows developers to revert to previous versions if mistakes occur.

# Concept Check

## 1. What does CO2e mean and why is it used as the standard unit for carbon accounting?

CO2e (Carbon Dioxide Equivalent) is a standard unit used to measure the impact of greenhouse gases. It allows different gases to be compared using a common measurement.

## 2. Why is it important to separate emission factors by resource type rather than using a single flat rate?

Different resources consume different amounts of energy. Using separate emission factors provides more accurate carbon calculations and helps identify the biggest emission sources.

## 3. What is the most carbon-intensive service type in your dataset?

The most carbon-intensive service type in the dataset is Networking.

# Hurdle 2 Concept Check

## What is the difference between Azure Blob Storage and Azure SQL Database? When would you choose each?

Azure Blob Storage is used for storing files such as CSVs, images, videos, backups, and model artifacts. Azure SQL Database is used for structured relational data that requires querying with SQL. Blob Storage is best for large files, while SQL Database is best for transactional and structured application data.

## What is LRS replication and what are its limitations vs GRS?

LRS (Locally Redundant Storage) keeps three copies of data within a single Azure data center. It is cheaper but does not protect against regional outages. GRS (Geo-Redundant Storage) replicates data to another geographic region, providing better disaster recovery.

## Why is it a security risk to hardcode a connection string in source code?

Hardcoding a connection string can expose sensitive credentials if the code is shared or pushed to GitHub. Attackers could gain access to cloud resources. Environment variables or .env files provide a safer way to store secrets.

# Hurdle 3 Concept Check

## What is RMSE and what does a lower value indicate?

RMSE (Root Mean Squared Error) measures the average prediction error of a model. A lower RMSE indicates that the model's predictions are closer to the actual values and therefore more accurate.

## Why do we create lag features for time-series prediction instead of using the date directly?

Lag features use past values to predict future values. Time-series patterns are usually dependent on historical observations, so lag features provide useful information that dates alone cannot capture.

## What are the risks of using Linear Regression for this task? What assumptions does it make?

Linear Regression assumes a linear relationship between features and the target variable. It may not capture complex seasonal patterns, sudden spikes, or nonlinear trends in carbon emissions, which can reduce forecasting accuracy.

# Hurdle 4 Concept Check

## What is REST and why is it the standard for building APIs?

REST is an architectural style for building web APIs using standard HTTP methods. It is widely used because it is simple, scalable, and works across different platforms and programming languages.

## What is the difference between a GET and a POST request? Which would you use to submit new billing data?

GET is used to retrieve data from a server, while POST is used to send or create new data. To submit new billing data, a POST request should be used.

## Why run the API and dashboard as two separate processes rather than one combined script?

Separating the API and dashboard improves scalability, maintainability, and flexibility. The backend can serve multiple clients while the dashboard focuses only on visualization.

