# Test Webhook-Sentry and Django Integration.

To run the test, follow these steps:


1. **Launch the containers:**
```
docker-compose up
```


2. **Once the containers are up and running, open a new terminal and execute the following command:**
```
docker exec -it webhook-client python send-request.py
```

- This command sends a request to the Django webhook client at: http://webhook-client:8081/webhook/testing/ using Webhook-Sentry.

3. **View the logs:**
Return to the docker-compose up console, where you'll be able to see logs related to the webhook-client.
