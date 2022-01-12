# FastAPI-Deploy-ML-model

API -
API stands for Application Programming Interface. An intermediary between two independent applications that communicate with each other.
Want to make your application available for other developers to use and integrate with, you build an API that acts as an entry point to your app.
Therefore have to communicate with this API through HTTP requests to consume and interact with your service.

Deployment - 

Many popular frameworks that can be used to do this task like Flask and Django. Django is usually used for large scale application and takes quite a bit time to set up that while Flask is usually your go-to for quickly deploying your model on a web app. Apart from the two mentioned there is another framework that is becoming quite popular, so much so that companies like Netflix and Uber are using it, and that framework is FastAPI. 

Flask VS FastAPI -

1. FastAPI is way faster than Flask, not just that it’s also one of the fastest python modules out there.
2. FastAPI provides an easier implementation for Data Validation to define the specific data type of the data you send.
3. Automatic Docs to call and test your API(Swagger UI and Redoc).
4. FastAPI comes with built-in support for Asyncio, GraphQL and Websockets.

FastAPI - 
FastAPI is currently the go-to framework for building robust and high-performance APIs that scale in production environments.
FastAPI's syntax is simple and this makes it fast to use. It actually resembles Flask’s syntax

To build a REST API to service an NLP model which can be queried via GET request and can dole out responses to those queries.