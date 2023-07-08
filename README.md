# Document Uploader and Word Count

This repository contains a Flask application that allows users to upload documents and counts the number of words in each document matching with length "k"

## Prerequisites

<ul>
  <li>Python 3.6 or higher</li>
  <li>Flask</li>
  <li>Docker</li>
  <li>Docker Compose</li>
</ul>

## Setup

Clone this repository to your local machine:

```
git clone https://github.com/rafathossain/Document-Upload-and-Word-Count.git
```

Navigate to the project directory:

```
cd Document-Upload-and-Word-Count
```

Create a `.env` file by copying the contents from <code>sample.env</code> provided in the repository. This file will contain the required parameters for the application.

Build and run the application using Docker Compose:

```
docker-compose up --build -d
```

Once the application is up and running, you can access it in your browser at <a href="http://127.0.0.1:8080">http://127.0.0.1:8080</a>
<em>Note: The port number (<code>8080</code>) may vary depending on the configuration specified in your <code>docker-compose.yml</code> file.</em>

You can also access the database via phpMyAdmin. To access it you can go to your browser at <a href="http://127.0.0.1:5525">http://127.0.0.1:5525</a>

For persisting the data of docker, uncomment the lines mentioned in `docker-compose.yml`

Thank you.