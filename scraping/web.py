"""
    Playing around with API calls in python
"""
import requests


def main():
    # fetch a bunch of posts
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    # Print out our status code, and the first post
    print(response)
    print(response.json()[0])

    # Dictionary of the new post we're creating
    new_post = {
        "userId": 10,
        "title": "OOOOOOOOoOOOOOooooF",
        "body": "This is a new post",
    }

    # Create a new post request
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts", json=new_post
    )

    # Print out the response and our newly created post
    print(response)
    print(response.json())

    # Get a specific post
    response = requests.get("https://jsonplaceholder.typicode.com/posts/2")

    # Print out the response and specific post
    print(response)
    print(response.json())


if __name__ == "__main__":
    main()
