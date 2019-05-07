import requests


def sign_in():
    """
        Sign into httpbins basic auth testing website
    """
    response = requests.get(
        "https://httpbin.org/basic-auth/user/psswd", auth=("user", "psswd")
    )
    print(response)


if __name__ == "__main__":
    sign_in()
