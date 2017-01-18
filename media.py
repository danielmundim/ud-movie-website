# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 12:16:05 2017

@author: daniel.mundim
"""
import webbrowser

## Movies class 

class Movie():

## Init function, runs once an instance is made, with all the correspondent parameters, sets the parameters passed through arguments to itself
    def __init__(self, movie_title, movie_storyline, poster_image, url_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = url_trailer
        
## Method that opens the browser with URL informed on it's "trailer" property
    def show_trailer(self):
        webbrowser.open(self.trailer)