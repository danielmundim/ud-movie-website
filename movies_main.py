# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 12:08:07 2017

@author: daniel.mundim
"""
import fresh_tomatoes
import media

## Instantiate all movies here

lord_of_the_rings = media.Movie("Lord of the Rings: Fellowship of the Ring", 
                                "Story of the lord of the rings",
                                "http://www.theclosetfeminist.ca/wp-content/uploads/2015/09/LOTR-movie-poster.jpeg",
                                "https://www.youtube.com/watch?v=Pki6jbSbXIY")

matrix = media.Movie("Matrix", 
                     "First movie of the trilogy",
                     "https://www.movieposter.com/posters/archive/main/9/A70-4902",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

matrix_reloaded = media.Movie("Matrix Reloaded", 
                              "Second movie of the trilogy",
                              "http://1.bp.blogspot.com/_3N0VetpYvQE/SxWMjZgU6YI/AAAAAAAAA_A/Mqpg7Fiz0a4/s1600/Matrix_Reloaded_4.jpg",
                              "https://www.youtube.com/watch?v=zsgrsiZoymA")


matrix_revolutions = media.Movie("Matrix Revolutions", 
                                 "Third movie of the trilogy",
                                 "https://upload.wikimedia.org/wikipedia/en/3/34/Matrix_revolutions_ver7.jpg",
                                 "https://www.youtube.com/watch?v=NhoaoTZJSX4")

## Create movie array with all instantiated movies
movies = [lord_of_the_rings, matrix, matrix_reloaded, matrix_revolutions]

## Call method on fresh_tomatoes.py file that creates html page based on movies array
fresh_tomatoes.open_movies_page(movies);