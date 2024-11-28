from Commands.command import Command
from Core.api_client import APIClient
from Core.user_interface import UserInterface
from colorama import Fore

class LoadDataCommand(Command):
    def __init__(self, user_interface, history, posts, albums):
        self.user_interface = user_interface
        self.history = history
        self.posts = posts
        self.albums = albums

    def execute(self):
        self.posts.clear()
        self.albums.clear()

        posts_data = APIClient.get_data("posts")
        if posts_data:
            self.posts.extend(posts_data)
            self.history.log_request("GET /posts", posts_data)
            self.user_interface.display_message("Пости завантажено успішно!", color=Fore.GREEN)

        albums_data = APIClient.get_data("albums")
        if albums_data:
            self.albums.extend(albums_data)
            self.history.log_request("GET /albums", albums_data)
            self.user_interface.display_message("Альбоми завантажено успішно!", color=Fore.GREEN)
