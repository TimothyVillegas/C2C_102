import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
from requests.api import post

client = commands.Bot(command_prefix='!')


def get_soup_from_url(url):

     headers = ()
     response = requests.get(url, headers=headers)
     if response.status_code != 200:
       print('call to reddit failed!')
       return None
     soup = BeautifulSoup(response.content, 'lxml')
     return soup

def subcars():

    soup = get_soup_from_url('https://www.reddit.com/r/cars/')
    
    for item in soup.select('.Post'):
        try:
             print('----------------------------------------')
             print(item.select('._1rZYMD_4xY3gRcSS3p8ODO')[0].get_text()) #Votes
             print(item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text()) #Title
             print(item.select('.FHCV02u6Cp2zYL0fhQPsO')[0].get_text()) #Comments         
        except Exception as e:
            print('') 

def submoto():

     soup = get_soup_from_url('https://www.reddit.com/r/motorcycles/')

     for item in soup.select('.Post'):
         try:
             print('----------------------------------------')
             print(item.select('._1rZYMD_4xY3gRcSS3p8ODO')[0].get_text()) #Votes
             print(item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text()) #Title
             print(item.select('.FHCV02u6Cp2zYL0fhQPsO')[0].get_text()) #Comments         
         except Exception as e:
             print('')

def subtruck():

     soup = get_soup_from_url('https://www.reddit.com/r/Trucks/')

     for item in soup.select('.Post'):
         try:
             print('----------------------------------------')
             print(item.select('._1rZYMD_4xY3gRcSS3p8ODO')[0].get_text()) #Votes
             print(item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text()) #Title
             print(item.select('.FHCV02u6Cp2zYL0fhQPsO')[0].get_text()) #Comments         
         except Exception as e:
             print('')


@client.event
async def on_ready():

    g_channel = client.get_channel(845045332089503757)
    await g_channel.send('Hello I\'m Alfr3d, I can help with pulling up any subreddit you request! Please type \"!search\" to bring up search options.')

@client.event
async def on_message(message):

    if message.content == '!search':
        g_channel = client.get_channel(845045332089503757)
        await g_channel.send('Which Subreddit would you like to visit? Cars, Trucks, or Motorcycles?')
    await client.process_commands(message)
            
    if message.content == 'Cars':
        subcars()
    elif message.content == 'Trucks':
        subtruck()
    elif message.content == 'Motorcycles':
        submoto()


@client.command(name='hello', description="Greet the user!")
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.name}!")


@client.command(name='version')
async def version(context):

    myEmbed = discord.Embed(title='Current Version', description='Bot Version 1.0')
    myEmbed.add_field(name='Version Code:', value='v1.0.0', inline=False)
    myEmbed.add_field(name='Date Released:', value='March 28, 2021', inline=False)
    myEmbed.set_author(name='Timothy Villegas')

    await context.message.channel.send(embed=myEmbed)


client.run('Token')