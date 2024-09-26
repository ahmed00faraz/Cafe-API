# Cafe RESTful API

This project provides a RESTful API for managing a list of cafes. You can perform operations such as adding a new cafe, getting a random cafe, updating the coffee price, and deleting cafes with the help of endpoints.

### API documentation : ```https://documenter.getpostman.com/view/30156661/2s9YJaYPpo```
## Features

- Retrieve a random cafe from the database.
- Retrieve all cafes stored in the database.
- Search for a cafe by location.
- Add new cafes to the database.
- Update the coffee price of a specific cafe.
- Delete a cafe from the database using an API key for authentication.

## Technologies Used

- **Python**
- **Flask** for creating the web server.
- **Flask-SQLAlchemy** for handling the SQLite database.
- **SQLite** for local data storage.

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ahmed00faraz/cafe-api.git
   cd cafe-api
   ```

2. **Install dependencies:**

   You need to install the required Python libraries. You can do so by running:

   ```bash
   pip install Flask Flask-SQLAlchemy
   ```

3. **Set up the database:**

   Before running the app, you need to create the SQLite database. Run Python in your terminal and execute the following:

   ```python
   from app import db
   db.create_all()
   ```

   This will create the `cafes.db` SQLite database file.

4. **Running the app:**

   You can start the Flask development server by running:

   ```bash
   python app.py
   ```

   The app will be running in debug mode at `http://127.0.0.1:5000/`.

## API Endpoints

### 1. Get a Random Cafe

- **Endpoint**: `/random`
- **Method**: GET
- **Description**: Returns a random cafe from the database.
- **Response**:

  ```json
  {
      "cafe": {
          "id": 1,
          "name": "Cafe 123",
          "map_url": "http://cafe.map",
          "img_url": "http://cafe.image",
          "location": "New York",
          "seats": "30",
          "has_toilet": true,
          "has_wifi": true,
          "has_sockets": true,
          "can_take_calls": true,
          "coffee_price": "$5"
      }
  }
  ```

### 2. Get All Cafes

- **Endpoint**: `/all`
- **Method**: GET
- **Description**: Returns a list of all cafes in the database.
- **Response**:

  ```json
  {
      "cafes": [
          {
              "id": 1,
              "name": "Cafe 123",
              "map_url": "http://cafe.map",
              "img_url": "http://cafe.image",
              "location": "New York",
              "seats": "30",
              "has_toilet": true,
              "has_wifi": true,
              "has_sockets": true,
              "can_take_calls": true,
              "coffee_price": "$5"
          },
          {
              "id": 2,
              "name": "Cafe 456",
              "map_url": "http://cafe456.map",
              "img_url": "http://cafe456.image",
              "location": "Los Angeles",
              "seats": "50",
              "has_toilet": true,
              "has_wifi": true,
              "has_sockets": false,
              "can_take_calls": true,
              "coffee_price": "$6"
          }
      ]
  }
  ```

### 3. Search for a Cafe by Location

- **Endpoint**: `/search?loc=<location>`
- **Method**: GET
- **Description**: Searches for cafes in the given location.
- **Response**: If a cafe is found in the location, the cafe details will be returned. If not, it will return an error.

  ```json
  {
      "cafe": {
          "id": 1,
          "name": "Cafe 123",
          "map_url": "http://cafe.map",
          "img_url": "http://cafe.image",
          "location": "New York",
          "seats": "30",
          "has_toilet": true,
          "has_wifi": true,
          "has_sockets": true,
          "can_take_calls": true,
          "coffee_price": "$5"
      }
  }
  ```

  If no cafe is found:

  ```json
  {
      "error": {
          "Not Found": "Sorry, we don't have a cafe at that location."
      }
  }
  ```

### 4. Add a New Cafe

- **Endpoint**: `/add`
- **Method**: POST
- **Description**: Adds a new cafe to the database.
- **Request Body**:

  The data should be sent using `form-data` or `application/x-www-form-urlencoded`.

  ```
  name=Cafe ABC
  map_url=http://cafeabc.map
  img_url=http://cafeabc.image
  loc=New York
  sockets=True
  toilet=True
  wifi=True
  calls=True
  seats=50
  coffee_price=$7
  ```

- **Response**:

  ```json
  {
      "success": "Successfully added the new cafe."
  }
  ```

### 5. Update the Coffee Price of a Cafe

- **Endpoint**: `/update-price/<int:cafe_id>?new_price=<new_price>`
- **Method**: PATCH
- **Description**: Updates the coffee price of a specific cafe.
- **Response**:

  If the cafe is found and updated:

  ```json
  {
      "success": "Successfully updated the price."
  }
  ```

  If the cafe is not found:

  ```json
  {
      "error": {
          "Not Found": "Sorry a cafe with that id was not found in the database."
      }
  }
  ```

### 6. Delete a Cafe (Requires API Key)

- **Endpoint**: `/report-closed/<int:cafe_id>?api-key=<API_KEY>`
- **Method**: DELETE
- **Description**: Deletes a cafe from the database if the correct API key is provided.
- **Response**:

  If the cafe is found and deleted:

  ```json
  {
      "success": "Successfully deleted the cafe from the database."
  }
  ```

  If the cafe is not found:

  ```json
  {
      "error": {
          "Not Found": "Sorry a cafe with that id was not found in the database."
      }
  }
  ```

  If the API key is incorrect:

  ```json
  {
      "error": {
          "Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."
      }
  }
  ```

## API Key for Deletion

To delete a cafe, you need to pass an API key with the request. The default key is:

```
TopSecretAPIKey
```

This project is licensed under the MIT License.

---

This README provides all necessary instructions and details for setting up and using the API. You can paste this into your `README.md` file.
