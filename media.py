import webbrowser

class Movie():
    """This class respreesents informtion about movies in jist to display on a web page"""
    
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']
    def __init__(self, movie_title, storyline,
                 poster_image, youtube_trailer):
        """
        :param movie_title: title of the movie
        :param storyline: story of the movie
        :param post_image: link to poster image of the movie
        :param youtube_trailer: youtube trailer link to the movie
        """
        
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer

    def show_trailer(self):
        """
        opens the youtube trailer in the browser
        """
        
        webbrowser.open(self.trailer_youtube_url)
