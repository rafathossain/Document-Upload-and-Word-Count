# Document Upload and Word Count TODO

The task involves building two services:

1. A document uploader service and
2. A worker service.

The document uploader service will be responsible for uploading documents, while the worker service will process the documents asynchronously and count the number of words with a specified length, denoted by "k". Redis will be used as the message broker for communication between the services.

### To complete the task, we require the following deliverables:

1. <b>Source Code:</b> Please provide a link to your GitHub repository containing the complete source code of the document uploader service and the worker service. We appreciate well-structured and documented code that follows best practices.

2. <b>Video Demonstration:</b> Along with the source code, we request a small video demonstrating the working of your solution. The video should showcase the interaction between the document uploader service and the worker service, highlighting the asynchronous processing and the accurate counting of words with the specified length. Please limit the video duration to a maximum of five minutes.

3. <b>Basic Jinja UI:</b> Implement a basic Jinja UI for the document uploader service to provide a user-friendly interface for uploading documents. The UI should allow users to select a document file and specify the desired word length for counting. Please ensure that the UI is clean, intuitive, and visually appealing.

### Instructions:

1. <b>Use Flask:</b> Implement the document uploader service and the worker service using the Flask web framework. Flask provides a lightweight and flexible approach to building web applications.
2. <b>Redis as Broker:</b> Utilize Redis as the message broker for communication between the services. Redis will enable the asynchronous processing of documents and facilitate efficient task distribution.
3. <b>Code Documentation:</b> Include clear and concise comments in your code to explain the functionality, major steps, and any important considerations.

### Readme File:
Include a Readme file in your GitHub repository that provides clear instructions on how to set up and run your application, including any necessary dependencies.