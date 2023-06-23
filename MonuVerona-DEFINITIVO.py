from urllib.request import urlopen
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from pprint import pprint
import time
"""
import folium
from folium.plugins import MarkerCluster
import pandas as pd
import umap
import numpy as np
import googlemaps
from telegram.ext import Updater, CommandHandler
 """

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
  
  if query_data == 'bussolengo':
    bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Bussolengo!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:\n\nChiesa:\n📍Chiesa di San Rocco; Via Mazzini\n📍Chiesa di San Valentino; Via S. Valentino, 30\n📍Chiesa di San Salvar; Via S. Salvar, 20\n📍Chiostro della Chiesa dei Padri Redentoristi; Via Ospedale, 12\n\nEdificio storico:\n📍Villa Spinola; Via Citella, 50\n\nMonumento:\n📍Monumento ai Caduti; Piazza della Vittoria, 20A\n📍Capitello delle quattro gambe; Via Verona, 65\n\nParco faunistico:\n📍Parco Natura Viva; Località Quercia')
    bot.sendMessage(chat_id, "Clicca qui per raggiungere la mappa!\n\nhttps://umap.openstreetmap.fr/it/map/mappa-bussolengo_932167?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true#13/45.4769/10.8578")
    
  elif query_data == 'castelnuovo':
    bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Castelnuovo!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:\n\nChiese:\n📍Chiesa dei Santi Filippo e Giacono; Via Belfiore 2\n📍Chiesa di Santa Maria Assunta; Via Bandiera\n📍Chiesa di Santa Maria;Via Castello 25\n📍Chiesa di Sant\'Andrea apostolo; Via Pastrengo 78\n📍Chiesa di San Martino; Via San Martino 1\n\nEdifici storici:\n📍Villa Mosconi Negri; Via Zamboni\n📍Villa Cossali Ridolfi Sella; Via Milano 56\n📍Villa Arvedi d\'Emilei; Via Palazzo, 2\n📍Villa Bagolini; Via Cà Brusà 20\n📍Palazzo Angelini; Piazza degli Alpini 4\n📍Tricolore di Oliosi; Via Custoza 15\n📍Torre Viscontea; Via Castello\n\nMonumenti:\n📍Monumento ai Martiri; Via Castello 6\n📍Monumento al Generale Rey di Villarey; Via Zenati 11A\n\nParchi faunistici:\n📍Colle San Lorenzo; Via San Lorenzo')
    bot.sendMessage(chat_id, "Clicca qui per raggiungere la mappa!\n\nhttps://umap.openstreetmap.fr/it/map/mappa-bussolengo_932167?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true#13/45.4769/10.8578")
    
  elif query_data == 'lazise':
    bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Lazise!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:\n\nChiese:\n📍Chiesa dei Santi Zenone e Martino; Via Chiesa 2\n📍Chiesetta dei Santi Fermo e Rustico; SP31 41\n📍Chiesa Parrocchiale di San Giovanni Battista di Pacengo; Piazza Chiesa\n📍Chiesa di San Giorgio Martire; Via Castello 10\n📍Chiesa di Santa Maria delle Grazie “La Pergolana”; Via della Pergolana 15\n📍Chiesetta in Corte Saline;Località Saine\n\nMonumenti:\n📍Monumento ai caduti Lazise; Piazza A.Partenio\n📍Monumento ai Marinai caduti; Via Porto 56\n📍Monumento ai caduti Pacengo; Piazza Senatore Alberti\n📍Monumento ai caduti Colà; Piazza Don Alessandro Vantini\n📍Monumento ai caduti Pacengo; Piazza Senatore Alberti\n📍Monumento ai caduti Colà; Piazza Don Alessandro Vantini\n\nEdifici:\n📍Dogana Veneta; Piazzetta Partenio 13\n📍Pieve Romanica di San Nicolò; Via Fontana 5\n📍Palazzo comunale; Piazza Vittorio Emanuele 2\n📍Castello Scaligero; Via Rosenheim 13\n📍Mura di Lazise; Via Rosenheim 13\n📍Palazzo comunale; Piazza Vittorio Emanuele 2\n📍Porta del Lion\n📍Porta San Zeno\n📍Porta Cansignorio')
    bot.sendMessage(chat_id, "Clicca qui per raggiungere la mappa!\n\nhttps://umap.openstreetmap.fr/it/map/mappa-senza-nome_932236?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true#14/45.5052/10.7326")
  
  elif query_data == 'mozzecane':
    bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Mozzecane!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:\n\nMonumenti:\n📍Monumento ai Caduti; Via carlo Montanari 4\n📍Monumento ai Caduti; Via Crocetta\n\nParchi naturali:\n📍Parco della Rimembranza; Via XXV Aprile')
    bot.sendMessage(chat_id, "Clicca qui per raggiungere la mappa!\n\nhttps://umap.openstreetmap.fr/it/map/new/?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true")  
  
  elif query_data == 'pastrengo':
    bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Pastrengo!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:\n\nChiese:\n📍Santuario di Santa Maria di Pol\n📍Chiesetta di San Rocco\n📍Chiesetta romanica di San Zeno\n\nMonumenti:\n📍Forte Degenfeld\n📍Forte Nugent\n📍Forte Leopold\n📍Forte Benedek\n📍Fortino Belvedere\n📍Monumento ai Caduti\n📍Le Fontane\n\nEdifici storici:\n📍Rustico di Carlo Alberto sul campo di battaglia della Carica \n📍Palazzo del Comune\n📍Caserma di Campara\n📍Villa Randina\n📍Colombaron')
    bot.sendMessage(chat_id, "Clicca qui per raggiungere la mappa!\n\nhttps://umap.openstreetmap.fr/it/map/mappa-pastrengo_932237?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true")
  
  elif query_data == 'pescantina':
    bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Pescantina!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:\n\nMonumenti:\n📍Monumento agli ex internati; Via Brizzi 22\n\nEdifici storici:\n📍Villa Quaranta; Via Ospedaletto 57\n📍Caà del Comun; Piazza San Rocco\n📍Villa Bertoldi; Via Bertoldi 13')
    bot.sendMessage(chat_id, "Clicca qui per raggiungere la mappa!\n\nhttps://umap.openstreetmap.fr/it/map/new/?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true")
 
  elif query_data == 'sommacampagna':
    bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Sommacampagna!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:\n\nMonumenti:\n📍Cippo funerario in ricordo di Orseolo Barozzi; Strada Valbusa - Cimitero di Custoza\n📍Cippo funerario in ricordo di Don Bartolomeo Burti; Via Francesco Zomer - Cimitero di Sommacampagn\n📍Lapide commemorativa in ricordo di Stefano Messaggi; Strada di Sommacampagna 12\n📍Lapide in ricordo del soggiorno del principe Ferdinando di Savoia; Via Cesare Battisti 8\n📍Lapide in ricordo del soggiorno di Vittorio Emanuele II; Via Francesco Zomer 2\n📍Monumento al principe Amedeo di Savio duca D\'Aosta; Strada di Sommacampagna\n📍Monumento dedicato ai Granatieri di Sardegna; Monte Croce nella Strada del Tamburino Sardo\n📍Lapide dedicata a don Bartolomeo Burti; Piazza C. Alberto 1\n📍Targa in ricordo del soggiorno di Carlo Alberto; Piazza C. Alberto 1\n📍Ossario di Custoza; Strada Ossario\n📍Cippo funerario in ricordo degli ufficiali della Imperial-regia Brigata Oberst; Cimitero di Custoza - Strada Valbusa\n📍Lapide di Don Gaetano Pivatelli; Cimitero di Custoza - Strada Valbusa\n📍Croce austriaca per Theodor Kirkovic; Via del Combattente\n📍Targa Tamburino Sardo; Strada del Tamburino Sardo 28')
    bot.sendMessage(chat_id, "Clicca qui per raggiungere la mappa!\n\nhttps://umap.openstreetmap.fr/it/map/monumenti-sommacampagna_932247?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true")
  
  elif query_data == 'sona':
    bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Sona!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:\n\nChiese:\n📍Chiesa di San Quirico e Santa Giuditta; Via S. Quirico 4\n📍Chiesa di San Salvatore; Via Montespada\n📍Pieve di Santa Giustina; Via Santa Giustina\n📍Chiesa Parrocchiale di Lugagnano di Sona; Via Don Giuseppe Fracasso 3\n📍Chiesa Parrocchiale di Sona; Piazza della Vittoria 9\n📍Chiesa Parrocchiale di San Giorgio in Salici; Via Santini 1\n📍Chiesa Parrocchiale di Palazzolo di Sona; Via IV Novembre 2\n📍Chiesetta di Sant\'Antonio da Padova; Via Ghiaia\n📍Chiesetta di San Rocco; Via S. Rocco 9\n\nEdifici storici:\n📍Torre Scaligera di Palazzolo di Sona; Via Castello 7\n📍Corte Beccarie; Corte Beccarie 37\n📍Corte Centurara; Via Centurara 1\n📍Corte Colombarone; Via Molinara\n📍Corte Guastalla Vecchia; Via Guastalla Vecchia 11\n📍Corte La Merla; Via La Merla 1\n📍Corte Montresora; Via Montresora\n📍Corte Turco; Località Turco\n📍Villa Sparici Landini; Via Monte Corno 10\n📍Villa Bajetta, ora Gaspari; Via Santini 21\n📍Villa Cavazzocca Mazzanti, ora Bressan; Via San Rocco\n📍Villa Giusti del Giardino\n📍Villa L\'Innominata; Via Roma 23\n📍Villa Maggi Berzacola detta del Belvedere; Via Bellavista\n📍Villa Merighi; Via Gaburri 62\n📍Villa Patrovich ora Manzati; Via Castello\n📍Villa Cavallari Gauarenti; Via Monte Bonello 1\n📍Villa Spolverini Schizzi Fiorini; Via IV Novembre 1\n📍Villa Trevisani; Via Roma 21\n\nMonumenti:\n📍Monumento caduti grande guerra Palazzolo di Sona; Via Castello 2-10\n📍Cippo battaglia del 1866; Località Fenilon\n\nFontane:\n📍Fontana di Sona con monumento ai caduti; Piazza della Vittoria 7\n\nMusei:\n📍Museo Paleontologico e dell\'origine del territorio \'Attilio Fedrigo\'; Piazza della Vittoria 11\n📍Museo storico baita Monte Baldo-Alpini di Lugagnano di Sona; Via Caduti del Lavoro 4\n\nParchi naturali:\n📍Bagolaro Corte Pietà; Corte Pietà \n📍Tunnel Amore; Localit Guastalla\n📍Viale dei Cipressi presso Villa Landini-Sparici; Via Monte Corno 10\n📍Parco di Villa Trevisani; Via Roma')
    bot.sendMessage(chat_id, "Clicca qui per raggiungere la mappa!\n\nhttps://umap.openstreetmap.fr/it/map/mappa-bussolengo_932167?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true#13/45.4769/10.8578")
 
  elif query_data == 'valeggio':
    bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Valeggio!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:\n\nChiese:\n📍Chiesa di San Pietro E Oratorio del Santissimo; Vicolo Oratorio 2\n📍Chiesa di San Marco; Via Raffaello Sanzio\n📍Chiesa di Santa Lucia; Località Santa Lucia 13\n\nEdifici storici:\n📍Palazzo Guarienti; Via Antonio Murari 27\n📍Centro storico Borghetto\n📍Il Serraglio; Strada Provinciale 24\n📍Torre del Borgo; Via Raffaello Sanzio\n📍Borghetto Ponte di legno; Via Raffaello Sanzio\n📍Casa Natale Domenico e Jacopo Foroni\n📍Villa Zamboni; Via G.Zamboni\n📍Villa Sigurtà; Via Circonvallazione Maffei\n\nMonumenti:\n📍Castello Scaligero; Via Degli Scaligeri\n📍Cimitero Monumentale; Via Giuseppe Mazzini 34\n📍Cimitero di Salionze;Località Radicchio 5\n📍Ponte Visconteo; Via Ponte Visconteo\n\nFontane:\n📍Palazzo Municipale e Piazza; Piazza Carlo Alberto\n📍Fontanella Lavatoio; Via Roma\n\nParchi naturali:\n📍Villa Maffei - Sigurtà; Parco Giardino Sigurtà')
    bot.sendMessage(chat_id, "Clicca qui per raggiungere la mappa!\n\nhttps://umap.openstreetmap.fr/en/map/untitled-map_932256?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true")
 
  elif query_data == 'vigasio':
    bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Vigasio!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:\n\nChiese:\n📍Chiesa di Sant\'Eurosia ;Via Verona\n📍Chiesa Parrocchiale di San Zeno; Corso Vittorio Emanuele II 9/A\n📍Chiesa di Isolalta; Via Villafranca 42\n📍Chiesa di Forette; Via S.Martino 18\n📍Santuario della Madonna di Campagnamagra; Via Campagnamagra 12\n\nEdifici storici:\n📍Villa La Zambonina; Via Zambonina 68\n📍Villa Montemezzi; Via Montemezzi\n\nMonumenti:\n📍Statua natività; Piazza Papa Luciani\n📍Monumento ai caduti; Via Montemezzi\n📍Monumento ai bersaglieri; Via Montemezzi\n📍Monumento agli alpini; Viale Europa\n📍Monumento al fante; Piazzale dei fanti\n📍Monumento ai caduti; Via Villafranca')
    bot.sendMessage(chat_id, "Clicca qui per raggiungere la mappa!\n\nhttps://umap.openstreetmap.fr/it/map/mappa-senza-nome_932242?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true")
  
  elif query_data == 'villafranca':
    bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Villafrancaa!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:\n\nChiese:\n📍Chiesa Santi Pietro e Paolo; Corso Vittorio Emanuele II\n📍Chiesa San Matteo Apostolo; Via Mazzini\n📍Chiesa del Cristo; Piazza Castello\n📍Chiesa San Girolamo Dottore; Via Principe Amedeo\n\nEdifici storici:\n📍Casa della Pace di Villafranca e giardino; Via Pace 10\n📍Corte Valesi; Corso Vittorio Emanuele II\n📍Palazzo Galeotti; Corso Vittorio Emanuele II\n📍Ex Poligono Tiro a Segno; Via Custoza 16\n📍Castello Scaligero; Piazza Castello\n📍Corte Spellini; Località Fornaci\n📍Villa Alessandri; Via Alessandri\n📍Villa Bisinelli Bottacini; Via Rinaldo da Villafranca 16\n📍Villa Gazzola; Via Mazzini\n\nMonumenti:\n📍Monumento del Quadrato; Via Quadrato\n📍Cimitero di Villafranca di Verona; Via del Cimitero')
    bot.sendMessage(chat_id, "Clicca qui per raggiungere la mappa!\n\nhttps://umap.openstreetmap.fr/it/map/mappa-villafranca_932225?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true")
    
bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,'callback_query': on_callback_query}).run_as_thread() 
          
print('Avviando ...')

while 1:
  time.sleep(2)
  