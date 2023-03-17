# Rest API Global Sale Game
***

## Project setup


### Setting up a virtual environment
At the root of the project, create a virtual environment using the command:
```shell
python -m venv venv
```
Activate it:
```shell
venv\Scripts\activate
```

Then we install all the dependencies from the `req.txt` file into the virtual environment:

```shell
pip install -r req.txt
```

### Migrations
**Postgres must be enabled for migration**

If all the previous steps are completed successfully, all that remains for you is to apply the migrations, for this we use this command:

```shell
python manage.py migrate
```

### Launch of the project
After successful configuration, you need to write the following command to run the django app:
Write the data from the file to your database
```shell
python.exe -Xutf8 manage.py loaddata api/fixture/game.json
```
Create superuser
```shell
python manage.py createsuperuser
```
Launch of the project
```shell
python manage.py runserver
```
***
## Endpoints

### Games

`api/v1/games/`

Allowed methods: GET, POST, HEAD, OPTIONS

1. GET
    + Description:    
        Getting all games        
    + Authorization: Not required
    + Permissions: Allow any
2. POST
    + Description:    
        Creating a new game   
    + Authorization: Required
    + Permissions: Admin Only
   
    + Data:
        + required:
        
            name: string,
            
            platform: string,
            
            genre: string,
            
            global_sales: integer
        + not required:
        
            year: integer
                



`api/v1/games/{id}/`

Allowed methods: GET, PUT, PATCH, DELETE, HEAD, OPTIONS

1. GET
    + Description:
    
        Getting information about a game by ID
        
    + Authorization: Not required
    + Permissions: Allow any  
    
2. PUT, PATCH:
    + Description:
    
        Full or partial change of information about the game
        
    + Authorization: Required
    + Permissions: Admin only 
    
    + Data:
        + required:
        
            name: string,
            
            platform: string,
            
            genre: string,
            
            global_sales: integer
        + not required:
        
            year: integer
3. DELETE:
    + Description:
    
        Delete information about the game
        
    + Authorization: Required
    + Permissions: Admin only    
    
`api/v1/games/genres/`

Allowed methods: GET, HEAD, OPTIONS

1. GET
    + Description:    
        Getting a list of the number of games for each genre       
    + Authorization: Required
    + Permissions: Admin only    

`api/v1/games/platforms/`

Allowed methods: GET, HEAD, OPTIONS

1. GET
    + Description:    
        Getting a list of the number of games for each platform       
    + Authorization: Required
    + Permissions: Admin only  

`api/v1/games/{id}/sales/`

Allowed methods: GET, PUT, PATCH, HEAD, OPTIONS

1. GET
    + Description:    
        Getting information about a game by ID    
    + Authorization: Not required
    + Permissions: Allow any

1. PUT, PATCH
    + Description:    
        Update the global_sale variable      
    + Authorization: Required
    + Permissions: Authenticated


## Other endpoints
1. Filtering enabled
   + Behind the platform:    
           `/api/v1/games/?platform=ps`

   + Behind the genre:    
           `/api/v1/games/?genre=racing`
   + By year of publication:  
           `/api/v1/games/?year_min=1998&year_max=2020`
   
It is also possible to use all filters at once:

`api/v1/games/?genre=racing&platform=ps&year_min=1998&year_max=2020`
            


Of course, in addition to the endpoints I created, there are endpoints of libraries that I use, such as  [swagger](https://drf-yasg.readthedocs.io/en/stable/). You can get acquainted with it on the official website with documentation.

[Test server](https://kotes613.pythonanywhere.com/api/v1/games/)