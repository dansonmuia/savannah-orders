badges
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
![Architecture illustration](https://github.com/dansonmuia/savannah-orders/blob/readme/illustrations/architecture.png)


### API Endpoints

The API endpoints for the aplication are as follows:

|ENDPOINT               | METHOD |AUTHORISATION | DESCRIPTION   |
|-----------------------|--------|--------------|---------------|
|`/`                    | GET    | No           | App status    |
|`/login`               | POST   | No           | Get auth token|
|`/customers`           | POST   | No           | Signup        |
|`/customers/<email>`   | GET    | Yes          | View customer |
|`/orders`              | GET    | Yes          | List orders   |
|`/orders`              | POST   | Yes          | Create order  |
|`/orders/<order_id>`   | GET    | Yes          | View order    |


### Howto:
Let's see how to interact with the application that you are running locally through docker-compose, or accessing online at https://savannah.danson.xyz
In all requests, set the `ContentType` header to `Application/json` beacuse we will be sending all data in json format. In addition, the endpoints that need authorisation require the `Authorization` header to be set as well, as we will see in the 'How to login' subsection.

#### How to Signup
create account

#### How to Login
To access the application's services such as creating orders, a request needs to be authorised. Here's how to get authorisation token:
request /login: send email&pass
token: in response
In subsequent requests, put the token inAUTHORISATION header as follows:
Authorization: Bearer `<token>`
The token will expire after some time, in which case you can generate a new one as described above.

#### How to view your details as a customer
#### How to place an order
#### How to view an order
#### How to list all your orders
