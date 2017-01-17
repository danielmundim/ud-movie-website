# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 12:16:05 2017

@author: daniel.mundim
"""
import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, url_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = url_trailer
        
    def show_trailer(self):
        webbrowser.open(self.trailer)