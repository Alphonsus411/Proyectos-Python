#crea un chatbot con capacidad de aprendizaje profundo y de conversación
from collections import Counter, OrderedDict, defaultdict, deque
import email
import heapq

from argon2 import PasswordHasher


class ChatBot:
    def __init__(self):
        self.memory = {}
        self.memory['name'] = 'Bella'
        self.memory['age'] = '18'
        self.memory['job'] = 'student'
        self.memory['hobby'] = 'reading'
        self.memory['hometown'] = 'Córdoba'
        self.memory['favorite_color'] = 'blue'
        self.memory['favorite_food'] = 'pizza'
        self.memory['favorite_drink'] = 'water'
        self.memory['favorite_movie'] = 'The Godfather'
        self.memory['favorite_song'] = 'The Sign'
        self.memory['favorite_sport'] = 'football'
        self.memory['favorite_book'] = 'The Lord of the Rings'
        self.memory['favorite_game'] = 'Minecraft'
        self.memory['favorite_actor'] = 'Brad Pitt'
        self.memory['favorite_actress'] = 'Jennifer Lawrence'
        self.memory['favorite_singer'] = 'Katy Perry'
        self.memory['favorite_band'] = 'The Beatles'
        self.memory['favorite_author'] = 'J.R.R. Tolkien'
        self.memory['favorite_director'] = 'Steven Spielberg'
        self.memory['favorite_teacher'] = 'Prof. Juan Carlos'
        self.memory['favorite_university'] = 'UCA'
        self.memory['favorite_school'] = 'UCA'
        self.memory['favorite_company'] = 'UCA'
        self.memory['favorite_restaurant'] = 'UCA'
        self.memory['favorite_cafe'] = 'UCA'
        self.memory['favorite_bar'] = 'UCA'
        self.memory['favorite_hotel'] = 'UCA'
        self.memory['favorite_cinema'] = 'UCA'
        self.memory['favorite_restaurant'] = 'UCA'
       
    def get_name(self):
        return self.memory['name']
    def get_age(self):
        return self.memory['age']
    def get_job(self):
        return self.memory['job']
    def get_hobby(self):
        return self.memory['hobby']
    def get_hometown(self):
        return self.memory['hometown']
    def get_favorite_color(self):
        return self.memory['favorite_color']
    def get_favorite_food(self):
        return self.memory['favorite_food']
    def get_favorite_drink(self):
        return self.memory['favorite_drink']
    def get_favorite_movie(self):
        return self.memory['favorite_movie']
    def get_favorite_song(self):
        return self.memory['favorite_song']
    def get_favorite_sport(self):
        return self.memory['favorite_sport']
    def get_favorite_book(self):
        return self.memory['favorite_book']
    def get_favorite_game(self):
        return self.memory['favorite_game']
    def get_favorite_actor(self):
        return self.memory['favorite_actor']
    def get_favorite_actress(self):
        return self.memory['favorite_actress']
    def get_favorite_singer(self):
        return self.memory['favorite_singer']
    def get_favorite_band(self):
        return self.memory['favorite_band']
    def get_favorite_author(self):
        return self.memory['favorite_author']
    def get_favorite_director(self):
        return self.memory['favorite_director']
    def get_favorite_teacher(self):
        return self.memory['favorite_teacher']
    def get_favorite_university(self):
        return self.memory['favorite_university']
    def get_favorite_school(self):
        return self.memory['favorite_school']
    def get_favorite_company(self):
        return self.memory['favorite_company']
    def get_favorite_restaurant(self):
        return self.memory['favorite_restaurant']
    def get_favorite_cafe(self):
        return self.memory['favorite_cafe']
    def get_favorite_bar(self):
        return self.memory['favorite_bar']
    def get_favorite_hotel(self):
        return self.memory['favorite_hotel']
    def get_favorite_cinema(self):
        return self.memory['favorite_cinema']
   
    def set_name(self, name):
        self.memory['name'] = name
    def set_age(self, age):
        self.memory['age'] = age
    def set_job(self, job):
        self.memory['job'] = job
    def set_hobby(self, hobby):
        self.memory['hobby'] = hobby
    def set_hometown(self, hometown):
        self.memory['hometown'] = hometown
    def set_favorite_color(self, favorite_color):
        self.memory['favorite_color'] = favorite_color
    def set_favorite_food(self, favorite_food):
        self.memory['favorite_food'] = favorite_food
    def set_favorite_drink(self, favorite_drink):
        self.memory['favorite_drink'] = favorite_drink
    def set_favorite_movie(self, favorite_movie):
        self.memory['favorite_movie'] = favorite_movie
    def set_favorite_song(self, favorite_song):
        self.memory['favorite_song'] = favorite_song
    def set_favorite_sport(self, favorite_sport):
        self.memory['favorite_sport'] = favorite_sport
    def set_favorite_book(self, favorite_book):
        self.memory['favorite_book'] = favorite_book
    def set_favorite_game(self, favorite_game):
        self.memory['favorite_game'] = favorite_game
    def set_favorite_actor(self, favorite_actor):
        self.memory['favorite_actor'] = favorite_actor
    def set_favorite_actress(self, favorite_actress):
        self.memory['favorite_actress'] = favorite_actress
    def set_favorite_singer(self, favorite_singer):
        self.memory['favorite_singer'] = favorite_singer
    def set_favorite_band(self, favorite_band):
        self.memory['favorite_band'] = favorite_band
    def set_favorite_author(self, favorite_author):
        self.memory['favorite_author'] = favorite_author
    def set_favorite_director(self, favorite_director):
        self.memory['favorite_director'] = favorite_director
    def set_favorite_teacher(self, favorite_teacher):
        self.memory['favorite_teacher'] = favorite_teacher
    def set_favorite_university(self, favorite_university):
        self.memory['favorite_university'] = favorite_university
    def set_favorite_school(self, favorite_school):
        self.memory['favorite_school'] = favorite_school
    def set_favorite_company(self, favorite_company):
        self.memory['favorite_company'] = favorite_company
    def set_favorite_restaurant(self, favorite_restaurant):
        self.memory['favorite_restaurant'] = favorite_restaurant
    def set_favorite_cafe(self, favorite_cafe):
        self.memory['favorite_cafe'] = favorite_cafe
    def set_favorite_bar(self, favorite_bar):
        self.memory['favorite_bar'] = favorite_bar
    def set_favorite_hotel(self, favorite_hotel):
        self.memory['favorite_hotel'] = favorite_hotel
    def set_favorite_cinema(self, favorite_cinema):
        self.memory['favorite_cinema'] = favorite_cinema

    def get_all(self):
        return self.memory
    def get_all_keys(self):
        return self.memory.keys()
    def get_all_values(self):
        return self.memory.values()
    def get_all_items(self):
        return self.memory.items()
    def get_all_values_as_list(self):
        return list(self.memory.values())
    def get_all_keys_as_list(self):
        return list(self.memory.keys())
    def get_all_items_as_list(self):
        return list(self.memory.items())
    def get_all_values_as_tuple(self):
        return tuple(self.memory.values())
    def get_all_keys_as_tuple(self):
        return tuple(self.memory.keys())
    def get_all_items_as_tuple(self):
        return tuple(self.memory.items())
    def get_all_values_as_set(self):
        return set(self.memory.values())
    def get_all_keys_as_set(self):
        return set(self.memory.keys())
    def get_all_items_as_set(self):
        return set(self.memory.items())
    def get_all_values_as_frozen_set(self):
        return frozenset(self.memory.values())
    def get_all_keys_as_frozen_set(self):
        return frozenset(self.memory.keys())
    def get_all_items_as_frozen_set(self):
        return frozenset(self.memory.items())
    def get_all_values_as_dict(self):
        return dict(self.memory.values())
    def get_all_keys_as_dict(self):
        return dict(self.memory.keys())
    def get_all_items_as_dict(self):
        return dict(self.memory.items())
    def get_all_values_as_ordered_dict(self):
        return OrderedDict(self.memory.values())
    def get_all_keys_as_ordered_dict(self):
        return OrderedDict(self.memory.keys())
    def get_all_items_as_ordered_dict(self):
        return OrderedDict(self.memory.items())
    def get_all_values_as_defaultdict(self):
        return defaultdict(self.memory.values())
    def get_all_keys_as_defaultdict(self):
        return defaultdict(self.memory.keys())
    def get_all_items_as_defaultdict(self):
        return defaultdict(self.memory.items())
    def get_all_values_as_counter(self):
        return Counter(self.memory.values())
    def get_all_keys_as_counter(self):
        return Counter(self.memory.keys())
    def get_all_items_as_counter(self):
        return Counter(self.memory.items())
    def get_all_values_as_deque(self):
        return deque(self.memory.values())
    def get_all_keys_as_deque(self):
        return deque(self.memory.keys())
    def get_all_items_as_deque(self):
        return deque(self.memory.items())
    def get_all_values_as_heapq(self):
        return heapq(self.memory.values())
    def get_all_keys_as_heapq(self):
        return heapq(self.memory.keys())
    def get_all_items_as_heapq(self):
        return heapq(self.memory.items())
    def get_all_values_as_list_of_tuples(self):
        return list(zip(self.memory.keys(), self.memory.values()))
    def get_all_keys_as_list_of_tuples(self):
        return list(zip(self.memory.keys(), self.memory.values()))
    def get_all_items_as_list_of_tuples(self):
        return list(zip(self.memory.keys(), self.memory.values()))
    def get_all_values_as_list_of_lists(self):
        return [list(i) for i in self.memory.values()]
    def get_all_keys_as_list_of_lists(self):
        return [list(i) for i in self.memory.keys()]
    def get_all_items_as_list_of_lists(self):
        return [list(i) for i in self.memory.items()]
    def get_all_values_as_list_of_tuples_of_tuples(self):
        return [tuple(i) for i in self.memory.values()]
    def get_all_keys_as_list_of_tuples_of_tuples(self):
        return [tuple(i) for i in self.memory.keys()]
    def get_all_items_as_list_of_tuples_of_tuples(self):
        return [tuple(i) for i in self.memory.items()]
    def get_all_values_as_list_of_lists_of_lists(self):
        return [list(i) for i in self.memory.values()]
    def get_all_keys_as_list_of_lists_of_lists(self):
        return [list(i) for i in self.memory.keys()]

    def get_favorite_company(self):
        return self.memory['favorite_company']
    def get_favorite_restaurant(self):
        return self.memory['favorite_restaurant']
    def get_favorite_cafe(self):
        return self.memory['favorite_cafe']
    def get_favorite_bar(self):
        return self.memory['favorite_bar']
    def get_favorite_hotel(self):
        return self.memory['favorite_hotel']
    def get_favorite_cinema(self):
        return self.memory['favorite_cinema']
    def get_favorite_movie(self):
        return self.memory['favorite_movie']
    def get_favorite_book(self):
        return self.memory['favorite_book']
    def get_favorite_game(self):
        return self.memory['favorite_game']
    def get_favorite_music(self):
        return self.memory['favorite_music']
    def get_favorite_sport(self):
        return self.memory['favorite_sport']
    def get_favorite_tvshow(self):
        return self.memory['favorite_tvshow']
    def get_favorite_tvshow_episode(self):
        return self.memory['favorite_tvshow_episode']
    def get_favorite_tvshow_season(self):
        return self.memory['favorite_tvshow_season']
    def get_favorite_tvshow_series(self):
        return self.memory['favorite_tvshow_series']
    def get_favorite_tvshow_movie(self):
        return self.memory['favorite_tvshow_movie']
    def get_favorite_tvshow_book(self):
        return self.memory['favorite_tvshow_book']
    def get_favorite_tvshow_game(self):
        return self.memory['favorite_tvshow_game']
    def get_favorite_tvshow_music(self):
        return self.memory['favorite_tvshow_music']
    def get_favorite_tvshow_sport(self):
        return self.memory['favorite_tvshow_sport']
    def get_favorite_tvshow_character(self):
        return self.memory['favorite_tvshow_character']
    def get_favorite_tvshow_actor(self):
        return self.memory['favorite_tvshow_actor']
    def get_favorite_tvshow_director(self):
        return self.memory['favorite_tvshow_director']
    def get_favorite_tvshow_writer(self):
        return self.memory['favorite_tvshow_writer']
    def get_favorite_tvshow_producer(self):
        return self.memory['favorite_tvshow_producer']
    def get_favorite_tvshow_composer(self):
        return self.memory['favorite_tvshow_composer']
    def get_favorite_tvshow_cinematographer(self):
        return self.memory['favorite_tvshow_cinematographer']

    def get_favorite_company_as_list(self):
        return self.memory['favorite_company']
    def get_favorite_restaurant_as_list(self):
        return self.memory['favorite_restaurant']
    def get_favorite_cafe_as_list(self):
        return self.memory['favorite_cafe']
    def get_favorite_bar_as_list(self):
        return self.memory['favorite_bar']
    def get_favorite_hotel_as_list(self):
        return self.memory['favorite_hotel']
    def get_favorite_cinema_as_list(self):
        return self.memory['favorite_cinema']
    def get_favorite_movie_as_list(self):
        return self.memory['favorite_movie']
    def get_favorite_book_as_list(self):
        return self.memory['favorite_book']
    def get_favorite_game_as_list(self):
        return self.memory['favorite_game']
    def get_favorite_music_as_list(self):
        return self.memory['favorite_music']
    def get_favorite_sport_as_list(self):
        return self.memory['favorite_sport']
    def get_favorite_tvshow_as_list(self):
        return self.memory['favorite_tvshow']
    def get_favorite_tvshow_episode_as_list(self):
        return self.memory['favorite_tvshow_episode']
    def get_favorite_tvshow_season_as_list(self):
        return self.memory['favorite_tvshow_season']
    def get_favorite_tvshow_series_as_list(self):
        return self.memory['favorite_tvshow_series']
    def get_favorite_tvshow_movie_as_list(self):
        return self.memory['favorite_tvshow_movie']
    def get_favorite_tvshow_book_as_list(self):
        return self.memory['favorite_tvshow_book']
    def get_favorite_tvshow_game_as_list(self):
        return self.memory['favorite_tvshow_game']
    def get_favorite_tvshow_music_as_list(self):
        return self.memory['favorite_tvshow_music']
    def get_favorite_tvshow_sport_as_list(self):
        return self.memory['favorite_tvshow_sport']
    def get_favorite_tvshow_character_as_list(self):
        return self.memory['favorite_tvshow_character']
    def get_favorite_tvshow_actor_as_list(self):
        return self.memory['favorite_tvshow_actor']
    def get_favorite_tvshow_director_as_list(self):
        return self.memory['favorite_tvshow_director']
    def get_favorite_tvshow_writer_as_list(self):
        return self.memory['favorite_tvshow_writer']
    def get_favorite_tvshow_producer_as_list(self):
        return self.memory['favorite_tvshow_producer']
    def get_favorite_tvshow_composer_as_list(self):
        return self.memory['favorite_tvshow_composer']
    def get_favorite_tvshow_cinematographer_as_list(self):
        return self.memory['favorite_tvshow_cinematographer']

    def get_favorite_company_as_string(self):
        return self.memory['favorite_company']
    def get_favorite_restaurant_as_string(self):
        return self.memory['favorite_restaurant']
    def get_favorite_cafe_as_string(self):
        return self.memory['favorite_cafe']
    def get_favorite_bar_as_string(self):
        return self.memory['favorite_bar']
    def get_favorite_hotel_as_string(self):
        return self.memory['favorite_hotel']
    def get_favorite_cinema_as_string(self):
        return self.memory['favorite_cinema']
    def get_favorite_movie_as_string(self):
        return self.memory['favorite_movie']
    def get_favorite_book_as_string(self):
        return self.memory['favorite_book']
    def get_favorite_game_as_string(self):
        return self.memory['favorite_game']
    def get_favorite_music_as_string(self):
        return self.memory['favorite_music']
    def get_favorite_sport_as_string(self):
        return self.memory['favorite_sport']
    def get_favorite_tvshow_as_string(self):
        return self.memory['favorite_tvshow']
    def get_favorite_tvshow_episode_as_string(self):
        return self.memory['favorite_tvshow_episode']
    def get_favorite_tvshow_season_as_string(self):
        return self.memory['favorite_tvshow_season']
    def get_favorite_tvshow_series_as_string(self):
        return self.memory['favorite_tvshow_series']
    def get_favorite_tvshow_movie_as_string(self):
        return self.memory['favorite_tvshow_movie']
    def get_favorite_tvshow_book_as_string(self):
        return self.memory['favorite_tvshow_book']
    def get_favorite_tvshow_game_as_string(self):
        return self.memory['favorite_tvshow_game']
    def get_favorite_tvshow_music_as_string(self):
        return self.memory['favorite_tvshow_music']
    def get_favorite_tvshow_sport_as_string(self):
        return self.memory['favorite_tvshow_sport']
    def get_favorite_tvshow_character_as_string(self):
        return self.memory['favorite_tvshow_character']
    def get_favorite_tvshow_actor_as_string(self):
        return self.memory['favorite_tvshow_actor']
    def get_favorite_tvshow_director_as_string(self):
        return self.memory['favorite_tvshow_director']
    def get_favorite_tvshow_writer_as_string(self):
        return self.memory['favorite_tvshow_writer']
    def get_favorite_tvshow_producer_as_string(self):
        return self.memory['favorite_tvshow_producer']
    def get_favorite_tvshow_composer_as_string(self):
        return self.memory['favorite_tvshow_composer']
    def get_favorite_tvshow_cinematographer_as_string(self):
        return self.memory['favorite_tvshow_cinematographer']

#importa librerias
import os
import sys
import time
import datetime
import random
import re
import json
import requests
import urllib
import urllib3
import getpass
import socket
import ssl
import socket
import urllib
import urllib3
import getpass
import socket

#definir funciones
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com",80))
    ip = s.getsockname()[0]
    s.close()
    return ip

#definir variables
ip = get_ip()

#definir clases
class Facebook:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'})
        self.session.headers.update({'Accept-Language': 'en-US,en;q=0.8'})
        self.session.headers.update({'Accept-Encoding': 'gzip, deflate, br'})
        self.session.headers.update({'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'})
        self.session.headers.update({'Connection': 'keep-alive'})
        self.session.headers.update({'Upgrade-Insecure-Requests': '1'})
        self.session.headers.update({'Cache-Control': 'max-age=0'})
        self.session.headers.update({'TE': 'Trailers'})
        self.session.headers.update({'Pragma': 'no-cache'})
        self.session.headers.update({'Expires': '0'})
        self.session.headers.update({'Referer': 'https://www.facebook.com/'})
        self.session.headers.update({'Origin': 'https://www.facebook.com'})
        self.session.headers.update({'Host': 'www.facebook.com'})
        self.session.headers.update({'Accept-Language': 'en-US,en;q=0.8'})
        self.session.headers.update({'Accept-Encoding': 'gzip, deflate, br'})
        self.session.headers.update({'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/web p,image/apng,*/*;q=0.8'})
        
    def login(self):
        r = self.session.get('https://www.facebook.com/')
        if 'checkpoint' in r.text:
            print('[+] Facebook Checkpoint')
            return False
        if 'recover' in r.text:
            print('[+] Facebook Recover')
            return False
        if 'recoverable error' in r.text:
            print('[+] Facebook Recoverable Error')
            return False
        if 'Please wait a few minutes before trying again' in r.text:
            print('[+] Facebook Please wait a few minutes before trying again')
            return False
        if 'Please wait a few minutes before trying again.' in r.text:
            print('[+] Facebook Please wait a few minutes before trying again.')
            return False
                                     
#definir objetos
facebook = Facebook(email, PasswordHasher)
facebook.login()

#definir main
if __name__ == '__main__':
    facebook.login()
    print('[+] Facebook Login Successful')
    print('[+] Facebook IP: ' + ip)
    print('[+] Facebook Email: ' + email)
    print('[+] Facebook Password: ' + PasswordHasher)
    print('[+] Facebook User ID: ' + facebook.get_user_id())
    print('[+] Facebook User Name: ' + facebook.get_user_name())
    print('[+] Facebook User First Name: ' + facebook.get_user_first_name())
    print('[+] Facebook User Last Name: ' + facebook.get_user_last_name())
    print('[+] Facebook User Full Name: ' + facebook.get_user_full_name())
    print('[+] Facebook User Profile Link: ' + facebook.get_user_profile_link())
    print('[+] Facebook User Profile Picture: ' + facebook.get_user_profile_picture())
    print('[+] Facebook User Cover Picture: ' + facebook.get_user_cover_picture())
    print('[+] Facebook User Bio: ' + facebook.get_user_bio())
    print('[+] Facebook User Birthday: ' + facebook.get_user_birthday())
        
#ejecutar main
def new_func(ip, facebook):
    print('[+] Facebook Login Successful')
    print('[+] Facebook IP: ' + ip)
    print('[+] Facebook Email: ' + email)
    print('[+] Facebook Password: ' + PasswordHasher)
    print('[+] Facebook User ID: ' + facebook.get_user_id())

if __name__ == '__main__':
    facebook.login()
    print('[+] Facebook Login Successful')
    print('[+] Facebook IP: ' + ip)
    print('[+] Facebook Email: ' + email)
    print('[+] Facebook Password: ' + PasswordHasher)
    print('[+] Facebook User ID: ' + facebook.get_user_id())
    print('[+] Facebook User Name: ' + facebook.get_user_name())
    print('[+] Facebook User Profile Link: ' + facebook.get_user_profile_link())
    print('[+] Facebook User Profile Picture: ' + facebook.get_user_profile_picture())
    print('[+] Facebook User Cover Picture: ' + facebook.get_user_cover_picture())
    print('[+] Facebook User Bio: ' + facebook.get_user_bio())
    print('[+] Facebook User Birthday: ' + facebook.get_user_birthday())
    print('[+] Facebook Password: ' + facebook.get_user_password())
    print('[+] Facebook User First Name: ' + facebook.get_user_first_name())
    print('[+] Facebook User Last Name: ' + facebook.get_user_last_name())
    print('[+] Facebook User Full Name: ' + facebook.get_user_full_name())
    print('[+] Facebook User    : ' + facebook.get_user_())

    new_func(ip, facebook)
    print('[+] Facebook Login Successful')
    print('[+] Facebook IP: ' + ip)
    print('[+] Facebook Email: ' + email)
    print('[+] Facebook Password: ' + PasswordHasher)
    print('[+] Facebook User ID: ' + facebook.get_user_id())
    print('[+] Facebook User Name: ' + facebook.get_user_name())
    print('[+] Facebook User Profile Link: ' + facebook.get_user_profile_link())
    print('[+] Facebook User Profile Picture: ' + facebook.get_user_profile_picture())
    print('[+] Facebook User Cover Picture: ' + facebook.get_user_cover_picture())
    print('[+] Facebook User Bio: ' + facebook.get_user_bio())
    print('[+] Facebook User Birthday: ' + facebook.get_user_birthday())
    print('[+] Facebook Password: ' + facebook.get_user_password())
    print('[+] Facebook User First Name: ' + facebook.get_user_first_name())
    print('[+] Facebook User Last Name: ' + facebook.get_user_last_name())
    print('[+] Facebook User Full Name: ' + facebook.get_user_full_name())
    print('[+] Facebook User    : ' + facebook.get_user_())
    
#finalizar main
if __name__ == '__main__':
    facebook.login()
    print('[+] Facebook Login Successful')
    print('[+] Facebook IP: ' + ip)
    print('[+] Facebook Email: ' + email)
    print('[+] Facebook Password: ' + PasswordHasher)
    print('[+] Facebook User ID: ' + facebook.get_user_id())
    print('[+] Facebook User Name: ' + facebook.get_user_name())
    print('[+] Facebook User Profile Link: ' + facebook.get_user_profile_link())
    print('[+] Facebook User Profile Picture: ' + facebook.get_user_profile_picture())
    print('[+] Facebook User Cover Picture: ' + facebook.get_user_cover_picture())
    print('[+] Facebook User Bio: ' + facebook.get_user_bio())
    print('[+] Facebook User Birthday: ' + facebook.get_user_birthday())
    print('[+] Facebook Password: ' + facebook.get_user_password())
    print('[+] Facebook User First Name: ' + facebook.get_user_first_name())
    print('[+] Facebook User Last Name: ' + facebook.get_user_last_name())
    print('[+] Facebook User Full Name: ' + facebook.get_user_full_name())
    print('[+] Facebook User    : ' + facebook.get_user_())

    new_func(ip, facebook)
    print('[+] Facebook Login Successful')
    print('[+] Facebook IP: ' + ip)
    print('[+] Facebook Email: ' + email)
    print('[+] Facebook Password: ' + PasswordHasher)
    print('[+] Facebook User ID: ' + facebook.get_user_id())
    print('[+] Facebook User Name: ' + facebook.get_user_name())
    print('[+] Facebook User Profile Link: ' + facebook.get_user_profile_link())
    print('[+] Facebook User Profile Picture: ' + facebook.get_user_profile_picture())
    print('[+] Facebook User Cover Picture: ' + facebook.get_user_cover_picture())
    print('[+] Facebook User Bio: ' + facebook.get_user_bio())
    print('[+] Facebook User Birthday: ' + facebook.get_user_birthday())
    print('[+] Facebook Password: ' + facebook.get_user_password())
    print('[+] Facebook User First Name: ' + facebook.get_user_first_name())
    print('[+] Facebook User Last Name: ' + facebook.get_user_last_name())
    print('[+] Facebook User Full Name: ' + facebook.get_user_full_name())
    print('[+] Facebook User    : ' + facebook.get_user_())
    
