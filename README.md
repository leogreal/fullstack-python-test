## How to develop

1. Clone the repository.
2. Create a virtualenv with Python 3.7
3. Activate virtualenv.
4. Install the dependencies.
5. Configure the instance with .env
6. Run migrations
7. Run the tests.

```console
git clone https://github.com/leogreal/fullstack-python-test.git
cd fullstack-python-test
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py migrate
python manage.py test
```

# Full-stack Test for candidates

We expect the candidate create a Web API based on the following requisites.

## Web API Technical Requisites

The usage of the following are demanded

- Language Python 3

The usage of the following are considered a plus

- Django
- Flask or Django REST Framework
- Docker

## Web Client Technical Requisites

The front-end must be separated from the Web API Solution and you are free to choose the tools used in the implementation

- Your HTML and CSS will be checked within the following implementation:

## WEB API Main Tasks

> 1. Create the following unauthenticated service endpoints
>
> - `/signin` - _POST_ - receiving an user name and a password
> - `/signup` - _POST_ - receiving an user full display name, an user name, a password and e-mail address. Upon save time, add the current date and time to the database.
>
> 2. Create the following authenticated service endpoints
>
> - `/products` - _POST_ - insert a new product to the product table with the following fields: id, name, description, price, creation date
> - `/products/{id}` - _DELETE_ - delete a product sending a product id
> - `/products/{id}` - _PUT_ - update all passed fields in its appropriate record
> - `/orders` - _POST_ - inserts an order receiving an user id and a list of products id with the current price and quantity
> - `/orders` - _GET_ - returns all orders from the logged user. The search must accept optional filters by price range and date interval of creation date
> - `/orders/{orderId}` - _GET_ - returns details from a specific order. Details are the total value of the order and a list of products with their individual quantity and the price.
> - `/orders/search` - _GET or POST_ - return orders filtered by a interval of price and interval of creation date

## Frontend Technical Requisites

The front-end must be separated from the API and you are free to choose the tools used in the implementation

> 1. Account
>
> - `Register` - The user must be able to register account
> - `Login` - The user must be able to log in into the application
>
> 2. Products
>
> - `Create/Update/Delete` - The user must be able to create, update and delete products
>
> 3. Orders
>
> - `Search` - The user must be able to filter orders by a interval of price and interval of creation date
> - `List` - The user must be able to see a list of orders
> - `Details` - The user must be able to see order details (product name, quantity, price)

## Services Requisites

- All endpoints must have automated tests that will prove the requisites are implemented
- Use as many design patterns and best practices as you see fit
- Use async methods anywhere you find it is needed

## Running and Executing Requisites

- Make your project running with the minimum needed interactions will be considered important in the analysis of your performance.
- Make it as easy as possible
- The ideal scenario will be to clone your repository and execute it through a single command such as `./INSTALL` or `./RUN`

## Documentation Requisites

- It can be done in portuguese although being in english will also be considered a plus
- Should be easy to read and understand the usage (from a client developer's perspective) of your services
- It should be easy to undertand how to execute your tests

## Last Requisites

- You can use your Github, GitLab or BitBucket to deliver this test
- You can fork from here to get started
- Try to keep your commits to a reasonable atomic capacity (We want to be able to understand your line of thinking. Do not be afraid to make really small commits.)
- Use as much best practices you see fit to address the commits and/or branch naming
- Publishing the API and the client in the cloud will be considered a PLUS

Feel free to ask us any question.
_Nicholas Drabowski_ - **nicholas@portaltelemedicina.com.br** or _Luiz Roberto Lethang Rodolpho_ - **luiz@portaltelemedicina.com.br**

You have 5 days counting from tomorrow to finish and deliver us the address of your github repository. Please, let us know if you need more time.

_Thank you for giving us this opportunity to get to know you and your work._

```

```
