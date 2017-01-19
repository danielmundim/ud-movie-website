# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 12:16:05 2017

@author: daniel.mundim
"""
import webbrowser

# Movies class


class Movie():
"""
Movie class used to instantiate movie objects to be used on creating the movies page
"""

    def __init__(self, movie_title, movie_storyline, poster_image, url_trailer):
        """
        Init function, runs once an instance is made, with all the correspondent parameters, sets the parameters passed through arguments to itself
        movie_title: title of the movie
        movie_storyline: description about the movie
        poster_image: url of poster image of the movie, to be shown on the website
        url_trailer: url of movie trailer, to be opened once clicked on the website
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = url_trailer

    def show_trailer(self):
        """
        show_trailer: Opens the browser with the URL informed on it's "trailer" property
        """
        webbrowser.open(self.trailer)
