import requests


def get_avatar(user):
    """
    Get the avatar of the user on Github

    :param user: str with the name of the user on Github
    :return: str with the link to go on
    """
    r = requests.get(f'https://api.github.com/users/{user}')
    url = r.json()['avatar_url']
    print(url)


if __name__ == '__main__':
    get_avatar('mahteuso')
