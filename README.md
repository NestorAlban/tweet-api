# tweet-api
tweeter with fastapi

## Run app

1. Run DB:
    - Run with docker
        ```shell
        docker-compose up -d db
        ```

2. Run fastapi
    - Run with uvicorn
        ```shell
        python -m uvicorn app.main:app --host 0.0.0.0
        ```

# Homework

- Create POST endpoint ('createuser')
- Create that receives name, email as parameters(body)
- Connect with Postgresql and creates a new record in user_test table
- Return record created