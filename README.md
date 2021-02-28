[![Maintainability](https://api.codeclimate.com/v1/badges/5f4a732a5ce721049edc/maintainability)](https://codeclimate.com/github/dansonmuia/savannah-orders/maintainability)
[![Build Status](https://travis-ci.com/dansonmuia/savannah-orders.svg?branch=main)](https://travis-ci.com/dansonmuia/savannah-orders)


# savannah-orders
Savannah Customer Orders App. Running on https://savannah.danson.xyz

### Running locally
#### Setup
To run this application locally, you need to have the following installed: 
 - docker and docker-compose
 - git

#### Download source code
On your terminal, run the following command to clone the services code from this github repository:

`$ git clone https://github.com/dansonmuia/savannah-orders.git`
#### Set environment variables
The flask application and databases require some environment variables to be set during image creation and running. To enable docker to pick them up easily, create a `.env` file at the `savannah-orders` root directory, with the following content:

`SECRET_KEY=<yours secret>`

`AT_API_KEY=<yourapikey>`

`AT_USERNAME=sandbox`

`POSTGRES_DB=<db name>`

`POSTGRES_USER=<db user>`

`POSTGRES_PASSWORD=<db password>`

##### A note about `AT_API_KEY`:
This value is provided by africas talking. Signup at `africastalking.com` and generate a key for the sandbox app
#### Running the application
If you are not in the `savannah-orders` folder:

`$ cd savannah-orders`

And then to finally spin up the containers:

`$ docker-compose up`

If everything went successfully, you should see that in the logs. And the service should be available at `http://127.0.0.1:5000/`

### Running tests

To run the application's unit tests inside a container, run the following command:

`$ docker-compose build`

`$ docker run --rm savannah-orders_orders_app pytest`

### Architecture
This is a service based application. For the instance running on `savannah.danson.xyz`, The main application sits behind an nginx proxy server. There is an sms sending worker, which gets messages to send from the main application through a redis queue:
![Architecture illustration](https://github.com/dansonmuia/savannah-orders/blob/main/illustrations/architecture.png)


### API Endpoints

The API endpoints for the aplication are as follows:

|ENDPOINT               | METHOD |AUTHORISATION | DESCRIPTION   | Response code |
|-----------------------|--------|--------------|---------------|---------------|
|`/`                    | GET    | No           | App status    | 200           |
|`/login`               | POST   | No           | Get auth token| 201           |
|`/customers`           | POST   | No           | Signup        | 201           |
|`/customers/<email>`   | GET    | Yes          | View customer | 200           |
|`/orders`              | GET    | Yes          | List orders   | 200           |
|`/orders`              | POST   | Yes          | Create order  | 201           |
|`/orders/<order_id>`   | GET    | Yes          | View order    | 200           |


## Howto:
Let's see how to interact with the application that you are running locally through docker-compose, or accessing online at https://savannah.danson.xyz
In all requests, set the `ContentType` header to `Application/json` beacuse we will be sending all data in json format. In addition, the endpoints that need authorisation require the `Authorization` header to be set as well, as we will see in the 'How to login' subsection.

#### How to Signup
To create an account, you need to post: `full_name`, `email`, `phone`, and `password`. Method is `POST`, sent to endpoint `/customers`.
A request would look like:

![Sign up request](https://github.com/dansonmuia/savannah-orders/blob/main/illustrations/signup_request.png)

And the response should look like:

![Sign up response](https://github.com/dansonmuia/savannah-orders/blob/main/illustrations/signup_response.png)


#### How to Login
To access the application's services such as creating orders, a request needs to be authorised. Here's how to get authorisation token:
`POST` a request to `/login` url, with `email` and `pass` in json data:

![Login data](https://github.com/dansonmuia/savannah-orders/blob/main/illustrations/login_request.png)

If you've provided the right values, a you'll receive a response containing the access token:

![Login response](https://github.com/dansonmuia/savannah-orders/blob/main/illustrations/login_response.png)

In subsequent requests, put the token in the `Authorization` header as follows:

![Headers](https://github.com/dansonmuia/savannah-orders/blob/main/illustrations/headers.png)

The token will expire after some time, in which case you can generate a new one as described above.

#### How to view your details as a customer
You can get your details using your signup email. This requires authorization, so have the `Authorization` header set properly.
Send a `GET` request to `/customers/<your_email>`. Youll get a response with your account details.

![Customer details](https://github.com/dansonmuia/savannah-orders/blob/main/illustrations/view_customer.png)

#### How to place an order
To place an order, send a `POST` request to `/orders`. This request authorization so that the order can be associated with your account.

![Order data](https://github.com/dansonmuia/savannah-orders/blob/main/illustrations/create_order_request.png)

On successful creation, the orders details will be sent back in rthe response:

![Order details](https://github.com/dansonmuia/savannah-orders/blob/main/illustrations/create_order_response.png)

#### How to view an order
To view the details of the order you've just created, sent a `GET` request with the order id to `/orders/<order_id>`. This request needs the `Authorization` header. The details in the response will resemble:

![View order](https://github.com/dansonmuia/savannah-orders/blob/main/illustrations/view_order_response.png)

#### How to list all your orders
You may place multiple orders. To view all the orders you've created, send a `GET` request to `/orders`, and a list of the same will be sent back:

![Order list](https://github.com/dansonmuia/savannah-orders/blob/main/illustrations/list_orders_response.png)

#### All done
Once you've placed your orders, you may sit back and relax, and the good people of earth will process your requests. Maybe.
