from urllib.request import urlopen
import telepot
import requests
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from pprint import pprint
import time
import folium
from folium.plugins import MarkerCluster
import pandas as pd
import json
import csv
import numpy as np

TOKEN="6255269129:AAFmX03HehvmbA2DzJ6u9DD2mLrVWB2XJ6Q" 

def on_chat_message(msg):
  content_type, chat_type, chat_id = telepot.glance(msg)
 
  keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Bussolengo', callback_data='bussolengo'),
                InlineKeyboardButton(text='Castelnuovo', callback_data='castelnuovo')],
                [InlineKeyboardButton(text='Lazise', callback_data='lazise'),
                InlineKeyboardButton(text='Mozzecane', callback_data='mozzecane')],
                [InlineKeyboardButton(text='Pastrengo', callback_data='pastrengo'),
                InlineKeyboardButton(text='Pescantina', callback_data='pescantina')],
                [InlineKeyboardButton(text='Sommacampagna', callback_data='sommacampagna'),
                InlineKeyboardButton(text='Sona', callback_data='sona')],
                [InlineKeyboardButton(text='Valeggio', callback_data='valeggio'),
                InlineKeyboardButton(text='Vigasio', callback_data='vigasio')],
                [InlineKeyboardButton(text='Villafranca', callback_data='villafranca')]])
  
  bot.sendMessage(chat_id, 'Ciao, mi chiamo MonuVeronaBot!🤖 Ti aiuterò nella ricerca dei monumenti  più interessanti dell\'ovest veronese!🧭\nScegli il comune tra l\'elenco:', reply_markup=keyboard) 
 
def on_callback_query(msg):
  query_id, chat_id, query_data = telepot.glance(msg, flavor='callback_query')
  print('Callback Query:', query_id, chat_id, query_data)
  
  if query_data == 'bussolengo':
    bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Bussolengo!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:\n\nChiesa:\n📍Chiesa di San Rocco; Via Mazzini\n📍Chiesa di San Valentino; Via S. Valentino, 30\n📍Chiesa di San Salvar; Via S. Salvar, 20\n📍Chiostro della Chiesa dei Padri Redentoristi; Via Ospedale, 12\n\nEdificio storico:\n📍Villa Spinola; Via Citella, 50\n\nMonumento:\n📍Monumento ai Caduti; Piazza della Vittoria, 20A\n📍Capitello delle quattro gambe; Via Verona, 65\n\nParco faunistico:\n📍Parco Natura Viva; Località Quercia')
    
    url = ("https://raw.githubusercontent.com/python-visualization/folium/main/examples/data")
    vis1 = json.loads(requests.get(f"{url}/vis1.json").text)
    vis2 = json.loads(requests.get(f"{url}/vis2.json").text)
    vis3 = json.loads(requests.get(f"{url}/vis3.json").text)
    m = folium.Map(location=[46.3014, -123.7390], zoom_start=7, tiles="Stamen Terrain")

    folium.Marker(location=[47.3489, -124.708], popup=folium.Popup(max_width=450).add_child(folium.Vega(vis1, width=450, height=250)),).add_to(m)

    folium.Marker(location=[44.639, -124.5339], popup=folium.Popup(max_width=450).add_child(folium.Vega(vis2, width=450, height=250)),).add_to(m)

    folium.Marker(location=[46.216, -124.1280], popup=folium.Popup(max_width=450).add_child(folium.Vega(vis3, width=450, height=250)),).add_to(m)

    m
    
  elif query_data == 'castelnuovo':
    bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Castelnuovo!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:\n\nChiesa:\n📍Chiesa dei Santi Filippo e Giacono; Via Belfiore,2\n📍Chiesa di Santa Maria Assunta; Via Bandiera\n📍Chiesa di Santa Maria;Via Castello, 25\n📍Chiesa di Sant\'Andrea apostolo; Via Pastrengo, 78\n📍Chiesa di San Martino; Via San Martino, 1\n\nEdificio storico:\n📍Villa Mosconi Negri; Via Zamboni\n📍Villa Cossali Ridolfi Sella; Via Milano, 56\n📍Villa Arvedi d\'Emilei; Via Palazzo, 2\n📍Villa Bagolini; Via Cà Brusà, 20A\n📍Palazzo Angelini; Piazza degli Alpini, 4\n📍Tricolore di Oliosi; Via Custoza, 15\n📍Torre Viscontea; Via Castello\n\nMonumento:\n📍Monumento ai Martiri; Via Castello, 6\n📍Monumento al Generale Rey di Villarey; Via Zenati, 11A\n\nParco faunistico:\n📍Colle San Lorenzo; Via San Lorenzo')
    
  elif query_data == 'lazise':
    bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Lazise!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:')
 
  elif query_data == 'mozzecane':
    bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Mozzecane!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:')
      
  elif query_data == 'pastrengo':
    bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Pastrengo!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:')
    
  elif query_data == 'pescantina':
    bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Pescantina!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:')
 
  elif query_data == 'sommacampagna':
    bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Sommacampagna!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:')
  
  elif query_data == 'sona':
    bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Sona!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:')
    
  elif query_data == 'valeggio':
    bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Valeggio!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:')
 
  elif query_data == 'vigasio':
    bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Vigasio!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:')
  
  elif query_data == 'villafranca':
    bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Villafrancaa!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:')
      
bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,'callback_query': on_callback_query}).run_as_thread() 
          
print('Avviando ...')

while 1:
  time.sleep(2)
  