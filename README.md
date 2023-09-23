# Easy Sell
## Description
This repository is the backend for the Easy Sell project. It is a REST API built with FastAPI and MongoDB. It is a simple project that allows users to create accounts, login, and post items for sale. It also allows users to view items for sale and contact the seller of an item.
## Usage
### 1. Setup Poetry
This project uses [Poetry](https://python-poetry.org/) for dependency management. To install the dependencies of the project, run the following command:
```js
poetry install
```
### 2. Environment Variables
This project uses environment variables for configuration. The following environment variables are required:

```javascript
SECRET=mysecretkey
CONNECTION_STRING=mongodb://localhost:27017
DB_NAME=mydatabase
```

### 3. Run the Project
To run the project, run the following command:
```bash
poetry run uvicorn src.main:app --reload
```
