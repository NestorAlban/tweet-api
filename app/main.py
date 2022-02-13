#Python
import json

from typing import List


#FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body

#App
from .models import User, Tweet, UserRegister

app= FastAPI()

#Path Operations

##Users

###Register a User
@app.post(
    path="/singup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
    )
def singup(user: UserRegister=Body(...)):
    """
    Sing up

    This path operation register a user in the app

    Parameters: 
        - Request body parameter
            - user: UserRegister
    
    Returns a json with the basic user information: 
        - user_id: UUID
        - email: Emailstr
        - first_name: str
        - last_name: str
        - birth_date: str
    """
    with open("users.json", "r+", encoding="utf-8") as f:
        results= json.loads(f.read())
        user_dict=user.dict()
        user_dict["user_id"]=str(user_dict["user_id"])
        user_dict["birth_date"] =str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
    return user



###Login a User

@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
    )
def login():
    pass

###Show all Users

@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all Users",
    tags=["Users"]
    )
def show_all_users():
    """
    Show users

    This path operation shows all users in the app

    Parameters: 
        -

    Returns a json list with all users in the app, with the following keys: 
        - user_id: UUID
        - email: Emailstr
        - first_name: str
        - last_name: str
        - birth_date: datetime
    """
    print("===USERS===")
    with open("app/users.json", "r", encoding="utf-8") as f: 
        print(f)
        results = json.loads(f.read())
        print(results)
        return results

###Show a User

@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
    )
def show_a_user():
    pass

###Delete a User

@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
    )
def delete_a_user():
    pass

###Update a User

@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=["Users"]
    )
def update_a_user():
    pass

## Tweets

###Show all Tweets

@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
    tags=["Tweets"]
    )
def home():
    print("HOME")
    with open("app/tweets.json", "r", encoding="utf-8") as f:
        
        print(f)
        results=json.loads(f.read())
        print(results)

        return results

###Post a tweet

@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=["Tweets"]
    )
def post(tweet: Tweet=Body(...)):
    """
    Post a Tweet

    This path operation post a tweet in the app

    Parameters: 
        - Request body parameter
            - tweet: Tweet
    
    Returns a json with the basic tweet information: 
        - tweet_id: UUID
        content: str
        created_at: datetime
        update_at: Optional datetime
        by: User
    """
    with open("tweets.json", "r+", encoding="utf-8") as f:
        results= json.loads(f.read())
        tweet_dict=tweet.dict()
        tweet_dict["tweet_id"]=str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] =str(tweet_dict["created_at"])
        tweet_dict["update_at"] =str(tweet_dict["update_at"])
        tweet_dict["by"]["user_id"]=str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birth_date"]=str(tweet_dict["by"]["birth_date"])
        results.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(results))
    return tweet

###Show a tweet

@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a tweet",
    tags=["Tweets"]
    )
def show_a_tweet():
    pass

### Delete a tweet

@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet",
    tags=["Tweets"]
)
def delete_a_tweet(): 
    pass

### Update a tweet

@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet",
    tags=["Tweets"]
)
def update_a_tweet(): 
    pass
