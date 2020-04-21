# MyTPlatformDataProcessingContainer
Docker container for MyT platform data processing container. 

### App
The app directory contains all of the code for the MyT platform data processing container application.

### Database Libraries
The databaseLibs directory contains all of the database connectors for the application. If you are using a mongodb database use the mongodb.py connector.
Add it to the app directory.

```bash
cp ./databaseLibs mongodb.py ./app/.
```

### Docker Compose files
The dockerComposeFiles directory contains all of the docker-compose files for the different databases.
Copy the required file into the projects root directory and run it to start the application.

```bash
docker-compose up
```

### Grafana
Contains the Docker file for grafana which adds the grafana proxy servers required plugin.

### MongoProxy
Contains the Docker file for the grafana proxy server. Used for Mongodb platforms.
