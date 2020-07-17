import io
import asyncio, aiohttp, requests

MagmatarBaseURL = 'https://api.magmatar.com/'

def fetchSkinUrl(playerQuery):
    global MagmatarBaseURL
    return MagmatarBaseURL + 'f/skin/' + playerQuery

def fetchHeadUrl(playerQuery, playerHeadSize, playerHeadOverlay):
    global MagmatarBaseURL
    return MagmatarBaseURL + 'f/head/' + playerQuery + '?size=' + str(playerHeadSize) + ['', '&overlay=True'][playerHeadOverlay]

def fetchSkinIo(playerQuery):
    skinIo = io.BytesIO(requests.get(fetchSkinUrl(playerQuery)).content)
    return skinIo

def fetchSkinBytes(playerQuery):
    skinIo = io.BytesIO(requests.get(fetchSkinUrl(playerQuery)).content)
    skinBytes = skinIo.getvalue()
    skinIo.close()
    return skinBytes

def fetchHeadIo(playerQuery, playerHeadSize=32, playerHeadOverlay=False):
    headIo = io.BytesIO(requests.get(fetchHeadUrl(playerQuery, playerHeadSize, playerHeadOverlay)).content)
    return headIo

def fetchHeadBytes(playerQuery, playerHeadSize=32, playerHeadOverlay=False):
    headIo = io.BytesIO(requests.get(fetchHeadUrl(playerQuery, playerHeadSize, playerHeadOverlay)).content)
    headBytes = headIo.getvalue()
    headIo.close()
    return headBytes

async def fetchBytes(session, url):
    async with session.get(url) as resp:
        respBytes = await resp.read()
    return respBytes

async def fetchSkinIoAsync(playerQuery, sessionX=None):
    if sessionX == None:
        sessionY = aiohttp.ClientSession()
    else:
        sessionY = sessionX
    skinIo = io.BytesIO(await fetchBytes(sessionY, fetchSkinUrl(playerQuery)))
    if sessionX == None:
        await sessionY.close()
    return skinIo

async def fetchSkinBytesAsync(playerQuery, sessionX=None):
    if sessionX == None:
        sessionY = aiohttp.ClientSession()
    else:
        sessionY = sessionX
    skinIo = io.BytesIO(await fetchBytes(sessionY, fetchSkinUrl(playerQuery)))
    if sessionX == None:
        await sessionY.close()
    skinBytes = skinIo.getvalue()
    skinIo.close()
    return skinBytes

async def fetchHeadIoAsync(playerQuery, playerHeadSize=32, playerHeadOverlay=False, sessionX=None):
    if sessionX == None:
        sessionY = aiohttp.ClientSession()
    else:
        sessionY = sessionX
    skinIo = io.BytesIO(await fetchBytes(sessionY, fetchHeadUrl(playerQuery, playerHeadSize, playerHeadOverlay)))
    if sessionX == None:
        await sessionY.close()
    return skinIo

async def fetchHeadBytesAsync(playerQuery, playerHeadSize=32, playerHeadOverlay=False, sessionX=None):
    if sessionX == None:
        sessionY = aiohttp.ClientSession()
    else:
        sessionY = sessionX
    skinIo = io.BytesIO(await fetchBytes(sessionY, fetchHeadUrl(playerQuery, playerHeadSize, playerHeadOverlay)))
    if sessionX == None:
        await sessionY.close()
    skinBytes = skinIo.getvalue()
    skinIo.close()
    return skinBytes