badges
# savannah-orders
Savannah Customer Orders App. Running on savannah.danson.xyz

### Running locally
#### Setup
To run this application locally, you need to have the following instaled: 
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

### Authentication

### Architecture

### API Endpoints

### Howto:
-create order,list, etc
Create order
list your orders
Create a customer account
