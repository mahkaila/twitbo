#!/usr/bin/env python
# -*- coding: utf-8 -*-
from google.cloud import language 
import tweepy, time, sys
import random
import json
import requests
import os
from tweepy.parsers import JSONParser
 
#argfile = str(sys.argv[1])
import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
	#enter the corresponding information from your Twitter application:
	ACCESS_KEY ='3219273390-29zvXbVrbFaM49kEFfdbNYaHnl7slMa2LuhoPMs'
	ACCESS_SECRET ='vGRIiOfYVfCoQC70DVH6IblAWhRIo5ZgZajx3WjFhQlNm'
	CONSUMER_KEY ='iDcCcFmLmagPwIFIeTzuIstRf'
	CONSUMER_SECRET ='S8gB4DjsLznnCH5NiV6JVkCLU6DwtWtXJgiDPHhFHy34Os7Wuz'
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
 
	'''filename=open(argfile,'r')
	f=filename.readlines()
	filename.close()'''

	funtweet="hi "
	entitiesArray = []

	trends1 = api.trends_place(23424977) # from the end of your code
	# trends1 is a list with only one element in it, which is a 
	# dict which we'll put in data.
	data = trends1[0] 
	# grab the trends
	trends = data['trends']
	# grab the name from each trend
	names = [trend['name'] for trend in trends]
	# put all the names together with a ' ' separating them
	trendy = [ names[i] for i in [0, 1, 2, 3] ]
	trendsName = random.choice(trendy)

	tweety = api.search(q=trendsName, lang='en', rrp=1)

	headlines = ['22 Tweets Women Will Find True For No Damn Good Reason',
	'36 Jokes About Marriage That Will Make You Both Laugh',
	'Ellen Had To Take A Deep Inhale After This Interview With Jessica Simpson',
	'19 Memes Only People Who Hate Feelings Will Appreciate',
	'Nicole Kidman Had The Best Response To A Chef Who Was Rude To Her On “Ellen”',
	'Can You Match The Animal To The Cereal It Tried To Sell You?',
	'How Much Do You Actually Know About Japanese Food?',
	'Which Obscure Cat Breed Are You?',
	'What Type Of Fairy Are You?',
	'Build An Instagram Profile And We\'ll Guess How Many Followers You Actually Have',
	'Can You Date This Boy?',
	'People Who Grew Up With Strict Parents Are Sharing Insane Rules They Had To Follow',
	'14 Times We All Wanted To Marry Dan Stevens',
	'25 Things Sweaty People Definitely Can\'t Get Away With',
	'Urban Decay Is About To Drop A New Naked Palette And Here\'s What It Looks Like',
	'Just 17 Really Funny Graduation Caps From The Class Of 2017',
	'34 Gross Firsts All Newly Pregnant Women Experience',
	'This Guy Popped All His Blackheads At Once And It\'s Beautiful To Watch',
	'23 Struggles All Ambitious People With Depression Know Too Well',
	'21 Reasons Why Women Should Wear High Heels All The Time',
	'20 Photos That Prove Barcelona Is Basically Heaven On Earth',
	'Answer 10 Fast-Food Questions And We\'ll Reveal Which Soda You Are',
	'13 Situations That Will Make Any Picky Eater Feel Personally Attacked',
	'21 First Period Traditions From Around The World',
	'A 93-Year-Old Bride Is Asking The Internet To Help Her Pick Her Wedding Dress And It’s So Pure',
	'Why You MUST See The Mona Lisa If You\'re In Paris',
	'14 Things You Understand If You\'re Absolutely Fucking Terrified Of Your Parents',
	'Literally Just A Bunch Of Things That Only Will Make Sense If You\'re Addicted To In-N-Out',
	'Everyone Stop What You\'re Doing Because The Oreo Cereal Is Coming Back',
	'19 Badass Boss Ladies Share Career Advice That\'ll Change Your Life',
	'21 Struggles Breastfeeding Mommas Know All Too Well',
	'How Much Of A Justin Timberlake Expert Are You?',
	'The Hardest Would You Rather For Whataburger Lovers',
	'I Just Found Out Parmesan Cheese Isn\'t Vegetarian And Basically My Whole Life Is A Lie',
	'This One Shocking Fact About Bananas Will Probably Blow Your Mind',
	'17 Oddly Erotic Cake Decorating Videos That Will Make You Say, "Oh, That\'s The Spot”',
	'Okay, Millennial Parents Need To Chill The Fuck Out',
	'Here\'s Why I Could Never Work At Starbucks',
	'26 Tweets That Are Only Funny If You\'re Currently Bleeding From Your Vagina',
	'What If I Told You That Peanuts Aren\'t Nuts At All?',
	'Here\'s What A Muslim Dietitian Eats During Ramadan',
	'Order A Grilled Cheese To Discover What City You Should Live In',
	'This Woman Recreated Van Gogh\'s "Starry Night" On Hair And I\'m Floored',
	'19 Pictures Of Organized Refrigerators That Are Basically Porn To Type-A People',
	'People Are Saying There\'s A Haircut Celebs Get Right Before They Steal Black Culture',
	'17 Times Parents Did Not Hold Back On Twitter',
	'This Glow-In-The-Dark Glitter Slime Is The Most 90s Thing You\'ll See All Day',
	'This Little Boy Had The "Mrs. Doubtfire"–Themed Birthday Party Of Your Dreams',
	'16 Traumatized Parents Who Really Deserve A Vacation',
	'These Are The Hottest Twins On Instagram',
	'11 Movies That Almost Starred Nicolas Cage But Were Lame Instead',
	'17 Hilarious Tweets About Kids That Are Truly Savage',
	'Nikes Were Invented In A Waffle Iron And I\'m Freaking Out',
	'The Way Asparagus Grows Will Creep You The Fuck Out',
	'You\'ll Cry-Laugh At These Pics Of Meryl Streep Photoshopped Onto Random Foods',
	'Reese Witherspoon\'s Mom Style Is Seriously Extra And I\'m Here For It',
	'15 Pictures That Will Make Every True Pizza Lover Scream "I REBUKE IT IN THE NAME OF THE LORD!”']
	for result in tweety:
		tweetTrend = result.text
		tweet_sentiment, tweet_entities = language_analysis(tweetTrend)
		tweetSenti = tweet_sentiment.score
		print result.text
	trend_sentiment, trend_entities = language_analysis(trendsName)
	'''for e in trend_entities:
		if e.entity_type =='PERSON':
			entitiesArray.extend([e])'''
		
	'''example_text = random.choice(headlines)
	sentiment, entities = language_analysis(example_text)
	print(sentiment.score, sentiment.magnitude)
	important = 0.0
	importantName = "hold"
	for e in entities:
		print(e.name, e.entity_type, e.metadata, e.salience)
		if e.salience >= important:
			important = e.salience
			importantName = e.name
		if e.salience >= 0.5 or e.entity_type =='PERSON' or 'WORK_OF_ART' or 'ORGANIZATION':
			entitiesArray.extend([e.name])
			#funtweet=funtweet+e.name+" "
	if not entitiesArray:
		entitiesArray.extend([importantName])'''
	
	generateText()
	
	headlinesMixUpHappy = [findRightEntity('PERSON')+' Thinks '+findRightEntity('OTHER')+' Is Going To Haunt Them Forever', 
	'Watch '+findRightEntity('PERSON')+' tell white lies to help puppies find forever homes.',
	'32 WTF Pictures Of '+ findRightEntity('ANY')+' During The Cold War', 
	'If You are Under 16, You Will Not Believe What '+ findRightEntity('ANY')+' Used To Be Like',
	'11 Creepy Things About ' + findRightEntity('PERSON')+' That Will Make You Lose Sleep',
	'22 Tweets ' + findRightEntity('PERSON')+' Will Find True For No Damn Good Reason',
	'36 Jokes About ' + findRightEntity('ANY')+' That Will Make You Both Laugh',
	findRightEntity('PERSON')+' Had To Take A Deep Inhale After This Interview With Jessica Simpson',
	'19 Memes Only ' + findRightEntity('PERSON')+' Will Appreciate',
	findRightEntity('PERSON')+ ' Had The Best Response To A Chef Who Was Rude To Her On Ellen',
	'How Much Do You Actually Know About ' + findRightEntity('ANY'),
	'Which Obscure ' + findRightEntity('ANY')+' Are You?',
	'What Type Of ' + findRightEntity('ANY')+' Are You?',
	'Can You Date ' + findRightEntity('PERSON')+ '?',
	'People Who Grew Up With ' + findRightEntity('ANY')+' Are Sharing Insane Rules They Had To Follow',
	'14 Times We All Wanted To Marry ' + findRightEntity('PERSON'),
	'25 Things ' + findRightEntity('PERSON')+' Definitely Can\'t Get Away With',
	findRightEntity('PERSON')+ 'Is About To Drop A New Naked Palette And Here\'s What It Looks Like',
	'Just 17 Really Funny Graduation Caps From ' + findRightEntity('EVENT'),
	'34 Gross Firsts ' + findRightEntity('PERSON')+' Experience',
	findRightEntity('PERSON')+' Popped All His Blackheads At Once And It\'s Beautiful To Watch',
	'23 Struggles ' + findRightEntity('PERSON')+' Know Too Well',
	'21 Reasons Why ' + findRightEntity('ANY')+' Should Wear High Heels All The Time',
	'20 Photos That Prove ' + findRightEntity('ANY')+' Is Basically Heaven On Earth',
	'Answer 10 ' + findRightEntity('ANY')+' Questions And We\'ll Reveal Which Soda You Are',
	'13 Situations That Will Make ' + findRightEntity('PERSON')+' Feel Personally Attacked',
	'21 ' + findRightEntity('EVENT')+' Traditions From Around The World',
	findRightEntity('PERSON')+' Is Asking The Internet To Help Her Pick Her Wedding Dress And Its So Pure',
	'Why You MUST See ' + findRightEntity('ANY')+' If You\'re In Paris',
	'14 Things You Understand If You\'re Absolutely Fucking Terrified Of ' + findRightEntity('ANY'),
	'Literally Just A Bunch Of Things That Only Will Make Sense If You\'re Addicted To' + findRightEntity('ANY'),
	'Everyone Stop What You\'re Doing Because ' + findRightEntity('ANY')+' Is Coming Back',
	'19 ' + findRightEntity('ANY')+' Share Career Advice That\'ll Change Your Life',
	'21 Struggles ' + findRightEntity('PERSON')+' Know All Too Well',
	'How Much Of A ' + findRightEntity('ANY')+' Expert Are You?',
	'The Hardest Would You Rather For ' + findRightEntity('ANY')+' Lovers',
	'I Just Found Out ' + findRightEntity('PERSON')+' Isn\'t Vegetarian And Basically My Whole Life Is A Lie',
	'This One Shocking Fact About ' + findRightEntity('ANY')+' Will Probably Blow Your Mind',
	'17 Oddly Erotic ' + findRightEntity('ANY')+' Videos That Will Make You Say, Oh, Thats The Spot',
	'Okay, ' + findRightEntity('PERSON')+' Needs To Chill The Fuck Out',
	'26 ' + findRightEntity('ANY')+' Tweets That Are Only Funny If You\'re Currently Bleeding From Your Vagina',
	'What If I Told You That Peanuts Aren\'t ' + findRightEntity('PERSON')+' At All?',
	'Here\'s What ' + findRightEntity('PERSON')+' Eats During Ramadan',
	'This Woman Recreated ' + findRightEntity('EVENT')+' On Hair And I\'m Floored',
	'19 Pictures Of ' + findRightEntity('PERSON')+' That Are Basically Porn To Type-A People',
	'People Are Saying There\'s A Haircut ' + findRightEntity('PERSON')+' Get Right Before They Steal Black Culture',
	'17 Times ' + findRightEntity('PERSON')+' Did Not Hold Back On Twitter',
	'This ' + findRightEntity('ANY')+' Is The Most 90s Thing You\'ll See All Day',
	findRightEntity('PERSON')+' Had The Mrs. Doubtfire Themed Birthday Party Of Your Dreams',
	'16 Traumatized Parents Who Really Deserve ' + findRightEntity('ANY'),
	'These Are The Hottest ' + findRightEntity('PERSON')+' On Instagram',
	'11 Movies That Almost Starred ' + findRightEntity('PERSON')+' But Were Lame Instead',
	'17 Hilarious Tweets About ' + findRightEntity('ANY')+' That Are Truly Savage',
	findRightEntity('ANY')+' Were Invented In A Waffle Iron And I\'m Freaking Out',
	'The Way ' + findRightEntity('ANY')+' Grows Will Creep You The Fuck Out',
	'You\'ll Cry-Laugh At These Pics Of ' + findRightEntity('PERSON')+' Photoshopped Onto ' + findRightEntity('ANY'),
	findRightEntity('PERSON')+'\'s Mom Style Is Seriously Extra And I\'m Here For It',
	'15 Pictures That Will Make ' + findRightEntity('PERSON')+' Scream I REBUKE IT IN THE NAME OF THE LORD!']

	headlinesMixUpSad = [findRightEntity('PERSON')+' Thinks '+findRightEntity('PERSON')+' Is Going To Haunt Them Forever', 'Watch '+findRightEntity('PERSON')+' tell white lies to help '+findRightEntity('PERSON')+' find forever homes.',
	'32 WTF Pictures Of '+ findRightEntity('PERSON')+' During The Cold War', 
	'If You are Under 16, You Will Not Believe What '+ findRightEntity('PERSON')+' Used To Be Like',
	'11 Creepy Things About ' + findRightEntity('PERSON')+' That Will Make You Lose Sleep']

	headlinesMixUpNeutral = [findRightEntity('PERSON')+' Thinks '+findRightEntity('OTHER')+' Is Going To Haunt Them Forever', 'Watch '+findRightEntity('PERSON')+' tell white lies to help '+findRightEntity('PERSON')+' find forever homes.',
	'32 WTF Pictures Of '+ findRightEntity('PERSON')+' During The Cold War', 
	'If You are Under 16, You Will Not Believe What '+ findRightEntity('PERSON')+' Used To Be Like',
	'11 Creepy Things About ' + findRightEntity('PERSON')+' That Will Make You Lose Sleep']

	imagesHappy = ["http://www.photosdaily.com/wp-content/uploads/2012/12/Happy-Cat.jpg", 
	"http://www.funnycatsite.com/pictures/be_a_happy_cat.jpg"]

	imagesSad = ["https://i.ytimg.com/vi/cNycdfFEgBc/maxresdefault.jpg", 
	"https://i.imgflip.com/qv8cu.jpg"]

	imagesNeutral = ["http://img08.deviantart.net/8994/i/2011/089/3/2/cat_stock_part_2_by_theweirdlady-d3ct7a0.jpg", 
	"http://www.findcatnames.com/wp-content/uploads/2017/01/tabby-cat-names.jpg"]
	#print(funtweet)

	#message = funtweet+" "+trendsName+" "+str(tweetSenti)+ " https://www.youtube.com/watch?v=9pzm1lQX0qU"
	if tweetSenti >= 0.2:
		heady = random.choice(headlinesMixUpHappy)
		url = random.choice(imagesHappy)
	elif tweetSenti <= -0.3:
		heady = random.choice(headlinesMixUpHappy)
		url = random.choice(imagesSad)
	else:
		heady = random.choice(headlinesMixUpHappy)
		url = random.choice(imagesNeutral)
	
	message = heady + " https://www.youtube.com/watch?v=9pzm1lQX0qU"
	tweet_image(url, message)
	#status = funtweet+" "+trendsName+" "+str(tweetSenti)
	#img = os.path.abspath('/images/cat_afraid.jpg')
	#api.update_with_media(img, status=status)
	#api.update_status(funtweet+" "+trendsName+" "+str(tweetSenti))
	time.sleep(900)#Tweet every 15 minutes        	


def language_analysis(text):
    client = language.Client()
    document = client.document_from_text(text)
    sent_analysis = document.analyze_sentiment()
    dir(sent_analysis)
    sentiment = sent_analysis.sentiment

    ent_analysis = document.analyze_entities()
    dir(ent_analysis)
    entities = ent_analysis.entities

    return sentiment, entities

def generateText():
    for i in range(0, 3):
    	exampleText = random.choice(headlines)
        makeList(exampleText)
	
def makeList(example_text):

	sentiment, entities = language_analysis(example_text)
	print(sentiment.score, sentiment.magnitude)
	important = 0.0
	importantName = "hold"
	
	for e in entities:
   		print(e.name, e.entity_type, e.metadata, e.salience)
        if e.salience >= 0.5: 
        	entitiesArray.extend([e])
        	#funtweet=funtweet+e.name+" "
        if e.entity_type =='PERSON': 
        	entitiesArray.extend([e])
        if e.entity_type == 'EVENT':
        	entitiesArray.extend([e])
        if e.entity_type == 'ORGANIZATION':
        	entitiesArray.extend([e])
        if e.entity_type == 'OTHER':
        	entitiesArray.extend([e])

def findRightEntity(entityType):
    #current_entity = random.choice(entitiesArray)
    enty = None
    type = entityType
    #currentSentiment, currentEntity = language_analysis(current_entity)
    for e in entitiesArray:
        if e.entity_type == entityType:
            enty = e.name
            break
    if enty is None or type is 'ANY':
    	nameo = random.choice(entitiesArray)
    	enty = nameo.name
    return enty

def tweet_image(url, message):
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unable to download image")

