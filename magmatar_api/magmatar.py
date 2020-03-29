import os, sys, re, io
import requests, json
import datetime, time

def fetchSkinFile(uuid):
    magmatarBaseUrl = 'https://api.magmatar.com/'
    skinUrl = magmatarBaseUrl + 'f' + '/' + 'skin' + '/' + uuid
    skinReq = requests.get(skinUrl)
    skinBytes = skinReq.content
    skinObj = io.BytesIO(skinBytes)
    return skinObj

def fetchSkinUrl(uuid, extension=None):
    magmatarBaseUrl = 'https://api.magmatar.com/'
    skinUrl = magmatarBaseUrl + 'f' + '/' + 'skin' + '/' + uuid
    if extension == True:
        skinUrl = skinUrl + '.' + 'png'
    return skinUrl

def fetchHeadFile(uuid, overlay=False, size=32):
    magmatarBaseUrl = 'https://api.magmatar.com/'
    headUrl = magmatarBaseUrl + 'f' + '/' + 'head' + '/' + uuid + '?' + 'overlay' + '=' + str(overlay) + '&' + 'size' + '=' + str(size)
    headReq = requests.get(headUrl)
    headBytes = headReq.content
    headObj = io.BytesIO(headBytes)
    return headObj

def fetchHeadUrl(uuid, overlay=False, size=32, extension=None):
    magmatarBaseUrl = 'https://api.magmatar.com/'
    if extension == True:
        png = '.png'
    else:
        png = ''
    headUrl = magmatarBaseUrl + 'f' + '/' + 'head' + '/' + uuid + png + '?' + 'overlay' + '=' + str(overlay) + '&' + 'size' + '=' + str(size)
    return headUrl
