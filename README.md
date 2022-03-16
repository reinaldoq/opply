# Opply tech assignment
We decided to build a mobile application for our customers, so that they can order our products using their phones. Your goal is to build the backend for this application.

## Requirements
-   Customers may exchange their username and password for an authentication token
-   Customers may see a paginated list of products. Each product in the list should have the following details:  `id`,  `name`,  `price`, and  `quantity in stock`
-   Customers may order the products they need
-   Number of products in stock should decrease after an order is made
-   Customers may see their history of orders.

## Quick start

This is the simplest way to have the project up and running in your local environment.
 - Clone this repository.
 - Create an `.env` file following the `example.env`, for a basic local setup the default values of this file could be use as it is provided.
 - Execute `make build` to create the docker images of the main django app and its db.
 - Execute `make up` to run the server on port `8000`

## Endpoints
1.  GET docs/ Provide a swagger doc of the public endpoints. 
2. GET admin/ Django admin
3.  GET api/v1/products/ Provide a list of all products in the store.
4. GET api/v1/orders/ Provide a list of all orders made by a user. Needs login.
5. GET api/v1/orders/ Create a new order for specific user. Needs login.
6.  api/token/ JWT token generation.
7.  api/token/refresh/ JWT token refresh.

## TODO
Specific to do could be found on the code, this is a summarised version:

 - [ ] Improve test adding products and orders factories, negative cases, multiple user cases.
 - [ ] Solve an error in the swagger doc that prevent it from rendering. This error is related to the `validators` in the `quantity_in_stock` field of `Product` model.
 - [ ] Improve `Product` and `Order` models to make it more realistic, for instance a model for `OrderProduct` could be a good idea to represent how is a specific product in an order (quantity, color, taxes, etc.)

## Deployment
One way to deploy this project into production could be use AWS Fargate since our app is containerized and with this service we don't need to worry about the server.
We are also going to need RDS to deploy the database.
We need to create instances in both services and wired it up together. 
After that we need to change all default values in django for the app and the db, them we are ready to provide this containerized app to our cloud provider. 
