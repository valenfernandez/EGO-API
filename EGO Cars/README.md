
## Starting the API

To run the API, follow these steps:

### 1. Create and Activate a Virtual Environment

```bash
# Create a virtual environment
python -m venv myenv

# Activate the virtual environment on Windows
myenv\Scripts\activate

# Activate the virtual environment on macOS/Linux
source myenv/bin/activate
```

### 2. Install Required Packages

Install the necessary Python packages using the provided `requirements.txt` file:

```bash
   pip install -r requirements.txt
```

### 3. Start the Django Development Server
Run the Django development server to start the API:

```bash
    # Navigate to where 'manage.py' is located
    cd /path/to/project/

    # Start the Django development server
    python manage.py runserver
```
This will launch the development server at http://127.0.0.1:8000/

## Databese info

### Django admin 

- **User**: egoadmin
- **Password**: cars2023

### Populating a Test Database

For ease of showcasing the functionality of the API, a test database has been populated with sample data. This data allows quick demonstrations of various API endpoints and functionalities.

#### Making a new database

If needed, the test database can be deleted, ensuring a fresh start without the sample data. To do this, follow these steps:

1. **Delete the current database** (db.sqlite3 file)
2. **Create new database** by running `python manage.py makemigrations` and `python manage.py migrate`
3. **Create new superuser** running `python manage.py createsuperuser`

## Endpoints

### Vehicles

#### Retrieving Vehicles (GET):
- URL: http://127.0.0.1:8000/vehicles/
- Method: GET
- Description: Retrieves a list of vehicles with all fields except associated features.
- Response: Returns details of all vehicles without their associated features.

#### Creating a Vehicle (POST):
- URL: http://127.0.0.1:8000/vehicles/
- Method: POST
- Description: Creates a new vehicle.
- Request Body: Requires data for creating a new vehicle, including fields like type, model_name, brand, year, price, description, tagline, image, etc.
- Response: Returns the details of the newly created vehicle or a success message.

#### Retrieving a Vehicle (GET):
- URL: http://127.0.0.1:8000/vehicles/{id}
- Method: GET
- Description: Retrieves details of a specific vehicle by its ID.
- Response: Returns the details of the vehicle including all fields.

#### Updating a Vehicle (PUT):
- URL: http://127.0.0.1:8000/vehicles/{id}
- Method: PUT
- Description: Updates all fields of the vehicle with ID {id}.
- Request Body: Requires data for updating all fields of the vehicle.
- Response: Returns the updated details of the vehicle.

#### Partially Updating a Vehicle (PATCH):
- URL: http://127.0.0.1:8000/vehicles/{id}
- Method: PATCH
- Description: Updates specific fields of the vehicle with ID {id}.
- Request Body: Requires data for updating specific fields of the vehicle.
- Response: Returns the updated details of the vehicle.

#### Deleting a Vehicle (DELETE):
- URL: http://127.0.0.1:8000/vehicles/{id}
- Method: DELETE
- Description: Deletes the vehicle with ID {id}.
- Response: Returns a success message or status code indicating the deletion was successful.

#### Retrieving Vehicle Summary List (GET):
- URL: http://127.0.0.1:8000/vehicles_summary/
- Method: GET
- Description: Retrieves a list of vehicles with only specific fields displayed in 'Home modelos'.
- Query Parameters:
    - ordering=price: Orders the vehicles by price (ascending).
    - ordering=year: Orders the vehicles by year (ascending).
    - ordering=-price: Orders the vehicles by price (decending).
    - ordering=-year: Orders the vehicles by year (decending).
    - type={Pickups+y+Comerciales|Auto|SUVs+y+Crossovers}: Filters vehicles by types
- Response: Returns a summary list of vehicles with the specified fields and optional ordering/filtering.


#### Retrieving Vehicle Details with Associated Features (GET):
- URL: http://127.0.0.1:8000/vehicle_detail/{id}/
- Method: GET
- Description: Retrieves all fields of a specific vehicle along with its associated features.
- Response: Returns the complete details of the vehicle including all its fields and a list of associated features.

### Features

#### Retrieve All Features of Vehicle (GET):
- URL: http://127.0.0.1:8000/vehicle_features/{id}/
- Method: GET
- Description: Retrieves all features associated with the vehicle.
- Response: Returns a list of all features linked to the vehicle.

#### Retrieve Key Features of Vehicle (GET):
- URL: http://127.0.0.1:8000/vehicle_key_features/{id}/
- Method: GET
- Description: Retrieves only the key features of the vehicle.
- Response: Returns a list of key features associated with the vehicle.

#### Add Feature to Vehicle (PUT):
- URL: http://127.0.0.1:8000/vehicles/{id}/add-feature/
- Method: PUT
- Description: Allows adding a new feature to the vehicle with ID=id.
- Request Body: Include the details of the feature to be added to the vehicle: name, description, image, and if it is a primary feature.
- Response: Returns the newly added feature.

#### Retrieve All Features (GET):
- URL: http://127.0.0.1:8000/features/
- Method: GET
- Description: Retrieves all features associated with all vehicle.
- Response: Returns a list of all features.

#### Retrive Feature (GET)
- URL : http://127.0.0.1:8000/features/{feature_id}
- Method: GET
- Description: Retrieves details of the feature with ID {id}.
- Response: Returns details of the feature.

#### Update Feature (PUT, PATCH)
- URL : http://127.0.0.1:8000/features/{feature_id}
- Method: PUT, PATCH
- Description: Updates details of the feature identified by {id}.
- Request Body: Include the details of the feature to be changed to the vehicle: name, description, image, and if it is a primary feature.
- Response: Updates and returns the modified feature details.

#### Delete Feature (DELETE)
- URL : http://127.0.0.1:8000/features/{feature_id}
- Method: DELETE
- Description: Removes the feature with ID {id}.
- Response: Removes the feature and returns a success message.


### Test drives

#### Request Test drive (PUT, PATCH)
- URL: http://127.0.0.1:8000/request_test_drive/{vehicle-id}/
- Method: PUT, PATCH
- Description: Allows adding a request for a test drive on the vehicle with ID=id.
- Request body: Include the details of the test drive: vehicle, client name, client email (optional), client phone, requested date(optional) and requested time(optional). 
- Response: Returns the newly added test drive request.

#### Approve Test drive (PUT, PATCH)
- URL: http://127.0.0.1:8000/approve_test_drive/{test_drive_id}/
- Method: PUT, PATCH
- Description: Allows approving a request for a test drive with ID=id.
- Request body: Include the field approved.
- Response: Returns the approved test drive request.

#### Retrieve Test Drive Requests List with Filtering and Ordering (GET):
- URL: http://127.0.0.1:8000/test_drive_requests_list/
- Method: GET
- Description: Retrieves a list of test drive requests with filtering and ordering options.
- Query Parameters:
    - vehicle={vehicle_id}: Filters test drive requests by a specific vehicle ID.
    - approved={true|false}: Filters test drive requests based on approval status.
    - ordering=requested_date: Orders the requests by requested date(ascending).
    - ordering=requested_time: Orders the requests by requested time(ascending).
    - ordering=-requested_date: Orders the requests by requested date(descending).
    - ordering=-requested_time: Orders the requests by requested time(descending).
- Response: Returns a list of test drive requests filtered and ordered as per the query parameters.


### Reviews

#### Add Review for a Vehicle (PUT, PATCH):
- URL: http://127.0.0.1:8000/make_review/{vehicle_id}
- Methods: PUT, PATCH
- Description: Allows adding a review for a specific vehicle identified by {vehicle_id}.
- Request Body: Include the details of the review to be added: client name, client email, description.
- Response: Returns the review.

#### Retrieve Reviews List (GET):
- URL: http://127.0.0.1:8000/reviews_list
- Method: GET
- Description: Retrieves a list of all reviews.
- Query Parameters:
    - vehicle={id}: Filters reviews by a specific vehicle ID.
    - ordering=created_at: Orders reviews by creation date.(ascending)
    - ordering=-created_at: Orders reviews by creation date.(descending).
- Response: Returns a list of reviews based on applied filters and ordering.


### Others 

#### Concessionaires List (GET):
- URL: http://127.0.0.1:8000/concessionaires
- Method: GET
- Description: Retrieves a list of concessionaires.
- Response: Returns a list of concessionaires available.

#### Concessionaires (POST):
- URL: http://127.0.0.1:8000/concessionaires
- Method: POST
- Description: Adds a concessionaire.
- Requested data: name, adress phone.
- Response: Returns a new concessionairy.

#### Manage Specific Concessionaire (GET, PUT, PATCH, DELETE):
- URL: http://127.0.0.1:8000/concessionaires/{id}/
- Methods:
    - GET: Retrieves details of the concessionaire with ID {id}.
    - PUT, PATCH: Updates details of the concessionaire identified by {id}.
    - DELETE: Removes the concessionaire with ID {id}.
- Description: Allows managing a specific concessionaire identified by {id}.
- Response:
    - GET: Returns details of the specific concessionaire.
    - PUT, PATCH: Updates and returns the modified concessionaire details.
    - DELETE: Deletes the concessionaire and returns a success message.

#### Services List (GET):
- URL: http://127.0.0.1:8000/services
- Method: GET
- Description: Retrieves a list of available services.
- Response: Returns a list of services provided.

#### Add Service (POST):
- URL: http://127.0.0.1:8000/services
- Method: POST
- Description: Adds a service.
- Response: Returns new service.

#### Manage Specific Service (GET, PUT, PATCH, DELETE):
- URL: http://127.0.0.1:8000/services/{id}/
- Methods:
    - GET: Retrieves details of the service with ID {id}.
    - PUT, PATCH: Updates details of the service identified by {id}.
    - DELETE: Removes the service with ID {id}.
- Description: Allows managing a specific service identified by {id}.
- Response:
    - GET: Returns details of the specific service.
    - PUT, PATCH: Updates and returns the modified service details.
    - DELETE: Deletes the service and returns a success message.

#### Accessories List (GET):
- URL: http://127.0.0.1:8000/accessories
- Method: GET
- Description: Retrieves a list of available accessories.
- Response: Returns a list of accessories offered.

#### Add Accessory (POST):
- URL: http://127.0.0.1:8000/accessories
- Method: POST
- Description: Adds a new accesory.
- Response: Returns new accesory.

#### Manage Specific Accessory (GET, PUT, PATCH, DELETE):
- URL: http://127.0.0.1:8000/accessories/{id}/
- Methods:
    - GET: Retrieves details of the accessory with ID {id}.
    - PUT, PATCH: Updates details of the accessory identified by {id}.
    - DELETE: Removes the accessory with ID {id}.
- Description: Allows managing a specific accessory identified by {id}.
- Response:
    - GET: Returns details of the specific accessory.
    - PUT, PATCH: Updates and returns the modified accessory details.
    - DELETE: Deletes the accessory and returns a success message.

#### Activities List (GET):
- URL: http://127.0.0.1:8000/activities
- Method: GET
- Description: Retrieves a list of activities.
- Response: Returns a list of available activities.

#### Add Activity (POST):
- URL: http://127.0.0.1:8000/activities
- Method: POST
- Description: Adds a new activity.
- Response: Returns new activity.

#### Manage Specific Activity (GET, PUT, PATCH, DELETE):
- URL: http://127.0.0.1:8000/activities/{id}/
- Methods:
    - GET: Retrieves details of the activity with ID {id}.
    - PUT, PATCH: Updates details of the activity identified by {id}.
    - DELETE: Removes the activity with ID {id}.
- Description: Allows managing a specific activity identified by {id}.
- Response:
    - GET: Returns details of the specific activity.
    - PUT, PATCH: Updates and returns the modified activity details.
    - DELETE: Deletes the activity and returns a success message.

#### Images
- URL: http://127.0.0.1:8000/media/images/{img_name}

## Detailed Documentation with CoreAPI

A more detailed version of this API's documentation has been generated using CoreAPI. To access the detailed API documentation:

1. **Start the Django development server.**
2. **Visit the API documentation URL in your browser at:** `http://127.0.0.1:8000/docs/`

For more information on CoreAPI, visit [CoreAPI Documentation](https://www.coreapi.org/).


## Logging
This project utilizes Python's logging module to record various events and activities occurring within the application.

### Log Configuration
The logging configuration is defined in the Django settings file (`settings.py`) under the `LOGGING` key. The log files are stored in a directory specified within the project's structure.

### Log Levels
The logging levels used in this project are:
- `DEBUG`: Detailed information, typically useful for debugging.
- `INFO`: General information about the application's operations.
- `WARNING`: Indication of potential issues or unexpected behavior.
- `ERROR`: Record of errors that occurred but did not stop the application.
- `CRITICAL`: Severe errors that may have led to an application crash.


## API Endpoint Accessibility Disclaimer

**Note:** This API has been intentionally designed with open endpoints for the purpose of this challenge. It allows unrestricted access to certain functionalities for ease of testing and evaluation. In a production environment we can restrict access.

### Restricting Access:

To restrict access to specific endpoints or functionalities and require users to be logged in, Django provides the `@login_required` decorator. Apply this decorator to views that should only be accessible to authenticated users.

```python
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def restricted_view(request):
    return HttpResponse("This view requires authentication.")
```

User groups with different permissions can also be added using the Django admin interface, and adding validations like `request.user.is_staff` to the views.

Token-Based authentication can also be added by using djangorestframework_simplejwt

```python
# settings.py

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # Add other authentication classes if needed
    ],
}
```

And getting the tokens using:

```bash
POST /token/
{
    "username": "usuario",
    "password": "contraseña"
}
```

## API Performance

While the current version of the API does not include explicit caching mechanisms for frequently accessed data, nor pagination for large datasets, these optimizations can be added for enhanced performance. The decision not to include these features in the current version was made based on the scope of the challenge and the specific requirements provided. 



