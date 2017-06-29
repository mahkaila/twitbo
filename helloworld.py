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


#@app.route('/')
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
'Ellen Had To Take A Deep Inhale After This Interview With Jessica Simpson',
'19 Memes Only People Who Hate Feelings Will Appreciate',
'Nicole Kidman Had The Best Response To A Chef Who Was Rude To Her On “Ellen”',
'Can You Match The Animal To The Cereal It Tried To Sell You?',
'How Much Do You Actually Know About Japanese Food?',
'Which Obscure Cat Breed Are You?',
'What Type Of Fairy Are You?',
'Can You Date This Boy?',
'15 Times Kim Kardashian Was A Total "Sex And The City" Fangirl',
'Create The Most Evil Disney Villain You Can Think Of And We\'ll Tell You Which Disney Princess You Are',
'Only A Real "RuPaul\'s Drag Race" Fan Can Identify These Queens Based On Their Real Names',
'Ed Sheeran Uses Britney Spears To Finally Release A Good Song',
'Selena Gomez, Are You Kidding Me Right Now?!?!?',
'This Family Threw A Quinceanera For Their Cat, And It\'s Everything',
'Watching James Corden And Ben Kingsley Sing "Mary Poppins" Was The Highlight Of My Life',
'Only A Sex Expert Can Score 10/12 On This Crappy Sex Drawings Quiz',
'People Who Grew Up With Strict Parents Are Sharing Insane Rules They Had To Follow',
'14 Times We All Wanted To Marry Dan Stevens',
'25 Sweaty People Can\'t Get Away',
'Obama And Trudeau Had A Romantic Dinner And It Was A Throwback To Simpler Times',
'People Are Either In Love With Or Totally Freaked Out By This Kitty With "Hands"',
'Urban Decay Is About To Drop A New Naked Palette And Here\'s What It Looks Like',
'34 Gross Firsts All Newly Pregnant Women Experience',
'This Guy Popped All His Blackheads At Once And It\'s Beautiful To Watch',
'23 Struggles All Ambitious People With Depression Know Too Well',
'21 Reasons Why Women Should Wear High Heels All The Time',
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
'People Are Saying There\'s A Haircut Celebs Get Right Before They Steal Black Culture',
'17 Times Parents Did Not Hold Back On Twitter',
'This Glow-In-The-Dark Glitter Slime Is The Most 90s Thing You\'ll See All Day',
'This Little Boy Had The "Mrs. Doubtfire"–Themed Birthday Party Of Your Dreams',
'16 Traumatized Parents Who Really Deserve A Vacation',
'These Are The Hottest Twins On Instagram',
'11 Movies That Almost Starred Nicolas Cage But Were Lame Instead',
'Nikes Were Invented In A Waffle Iron And I\'m Freaking Out',
'The Way Asparagus Grows Will Creep You The Fuck Out',
'You\'ll Cry-Laugh At These Pics Of Meryl Streep Photoshopped Onto Random Foods',
'Reese Witherspoon\'s Mom Style Is Seriously Extra And I\'m Here For It',
'15 Pictures That Will Make Every True Pizza Lover Scream "I REBUKE IT IN THE NAME OF THE LORD!”']


 
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

generateText()

#funtweet = ' '.join(entitiesArray)

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

#findRightEntity('PERSON')

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

headlinesMixUpHappy = [findRightEntity('PERSON')+' Thinks '+findRightEntity('OTHER')+' Is Going To Haunt Them Forever', 
'Watch '+findRightEntity('PERSON')+' tell white lies to help puppies find forever homes.',
'32 WTF Pictures Of '+ findRightEntity('ANY')+' During The Cold War', 
'If You are Under 16, You Will Not Believe What '+ findRightEntity('ANY')+' Used To Be Like',
'Create The Most Evil ' + findRightEntity('ANY')+' You Can Think Of And We\'ll Tell You Which Disney Princess You Are',
'Only A Real "RuPaul\'s Drag Race" Fan Can Identify These '+ findRightEntity('ANY')+' Based On Their Real Names',
'11 Creepy Things About ' + findRightEntity('PERSON')+' That Will Make You Lose Sleep',
'22 Tweets ' + findRightEntity('PERSON')+' Will Find True For No Damn Good Reason',
'36 Jokes About ' + findRightEntity('ANY')+' That Will Make You Both Laugh',
findRightEntity('PERSON')+' Threw A Quinceanera For Their Cat, And It\'s Everything',
'Only a'+ findRightEntity('ANY')+ ' Expert Can Score 10/12 On This Crappy Sex Drawings Quiz',
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
'15 Times '+findRightEntity('PERSON') +' Was A Total "Sex And The City" Fangirl',
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
'Hey '+ findRightEntity('PERSON')+ ', Don\'t Microwave Your Pee In A 7-Eleven',
'15 Pictures That Will Make ' + findRightEntity('PERSON')+' Scream I REBUKE IT IN THE NAME OF THE LORD!']

headlinesMixUpSad = [findRightEntity('PERSON')+' Thinks '+findRightEntity('PERSON')+' Is Going To Haunt Them Forever', 'Watch '+findRightEntity('PERSON')+' tell white lies to help '+findRightEntity('PERSON')+' find forever homes.',
'32 WTF Pictures Of '+ findRightEntity('PERSON')+' During The Cold War', 
'If You are Under 16, You Will Not Believe What '+ findRightEntity('PERSON')+' Used To Be Like',
'11 Creepy Things About ' + findRightEntity('PERSON')+' That Will Make You Lose Sleep']

headlinesMixUpNeutral = [findRightEntity('PERSON')+' Thinks '+findRightEntity('OTHER')+' Is Going To Haunt Them Forever', 'Watch '+findRightEntity('PERSON')+' tell white lies to help '+findRightEntity('PERSON')+' find forever homes.',
'32 WTF Pictures Of '+ findRightEntity('PERSON')+' During The Cold War', 
'If You are Under 16, You Will Not Believe What '+ findRightEntity('PERSON')+' Used To Be Like',
'11 Creepy Things About ' + findRightEntity('PERSON')+' That Will Make You Lose Sleep']


imagesHappy = ["https://img.buzzfeed.com/buzzfeed-static/static/2017-06/5/21/asset/buzzfeed-prod-fastlane-01/sub-buzz-11517-1496714151-1.jpg?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/26/10/asset/buzzfeed-prod-fastlane-01/sub-buzz-30560-1495810053-2.png?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/24/14/asset/buzzfeed-prod-fastlane-01/sub-buzz-9888-1495649079-3.jpg?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/19/9/asset/buzzfeed-prod-fastlane-03/anigif_sub-buzz-6313-1495201791-8.gif?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/9/12/enhanced/buzzfeed-prod-fastlane-03/enhanced-3688-1494347386-10.jpg?downsize=715:*&output-format=auto&output-quality=auto",
"https://pbs.twimg.com/media/C9W-TEXVoAAEUoo.jpg",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/5/14/asset/buzzfeed-prod-fastlane-01/sub-buzz-17203-1496687244-9.jpg?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/5/13/asset/buzzfeed-prod-fastlane-03/sub-buzz-15505-1496684937-4.jpg?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/2/8/asset/buzzfeed-prod-fastlane-01/anigif_sub-buzz-19277-1496408268-1.gif?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/6/6/asset/buzzfeed-prod-fastlane-03/anigif_sub-buzz-25951-1496744682-3.gif?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/7/10/asset/buzzfeed-prod-fastlane-02/sub-buzz-21743-1496846795-1.jpg?resize=625:463&no-auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/7/11/asset/buzzfeed-prod-fastlane-02/sub-buzz-22834-1496848159-1.jpg?resize=625:1068&no-auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/22/15/asset/buzzfeed-prod-fastlane-02/sub-buzz-23142-1495481959-5.png?resize=625:678&no-auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/19/19/asset/buzzfeed-prod-fastlane-03/sub-buzz-31936-1495236683-3.png?no-auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/16/13/asset/buzzfeed-prod-fastlane-02/sub-buzz-9149-1494957001-1.jpg?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/2/10/asset/buzzfeed-prod-fastlane-01/anigif_sub-buzz-23388-1496415334-2.gif?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/25/19/asset/buzzfeed-prod-fastlane-02/anigif_sub-buzz-29978-1495756398-4.gif?downsize=715:*&output-format=auto&output-quality=auto",
"https://pbs.twimg.com/media/DBeul54UAAA9L7x.jpg",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/2/7/asset/buzzfeed-prod-fastlane-03/sub-buzz-23762-1496401542-7.jpg?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/2/10/asset/buzzfeed-prod-fastlane-03/sub-buzz-31768-1496415092-7.jpg?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/23/12/asset/buzzfeed-prod-fastlane-03/anigif_sub-buzz-5929-1495558624-4.gif?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/22/13/asset/buzzfeed-prod-fastlane-03/sub-buzz-5665-1495473671-1.jpg?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/2/19/asset/buzzfeed-prod-fastlane-01/sub-buzz-7835-1496444635-10.jpg?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/6/11/asset/buzzfeed-prod-fastlane-03/anigif_sub-buzz-14547-1496763064-1.gif?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/3/11/asset/buzzfeed-prod-web-15/anigif_sub-buzz-3044-1496503805-1.gif?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/6/9/enhanced/buzzfeed-prod-fastlane-03/enhanced-10428-1496756432-1.jpg?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/17/12/asset/buzzfeed-prod-fastlane-02/sub-buzz-29156-1495038084-1.png?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/17/12/asset/buzzfeed-prod-fastlane-03/sub-buzz-18588-1495038941-1.jpg?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/17/14/asset/buzzfeed-prod-fastlane-03/anigif_sub-buzz-2916-1495047358-1.gif?downsize=715:*&output-format=auto&output-quality=auto"]


imagesSad = ["https://img.buzzfeed.com/buzzfeed-static/static/2017-06/6/9/asset/buzzfeed-prod-fastlane-01/sub-buzz-12566-1496757417-17.png?downsize=715:*&output-format=auto&output-quality=auto", 
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/6/7/enhanced/buzzfeed-prod-fastlane-03/enhanced-1459-1496749957-17.jpg?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/6/9/enhanced/buzzfeed-prod-fastlane-02/enhanced-24263-1496754092-1.jpg?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/6/11/asset/buzzfeed-prod-fastlane-01/sub-buzz-17656-1496764187-1.jpg?downsize=715:*&output-format=auto&output-quality=auto", 
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/6/11/asset/buzzfeed-prod-fastlane-01/anigif_sub-buzz-17856-1496764444-1.gif", 
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/6/11/asset/buzzfeed-prod-fastlane-01/sub-buzz-17776-1496764488-1.png?downsize=715:*&output-format=auto&output-quality=auto",
"https://68.media.tumblr.com/ca8195df797faeab79817835ee82fbed/tumblr_inline_mici0ina9F1qz4rgp.jpg",
"https://68.media.tumblr.com/4d10c194c6adedec6f35bc4cdf3314a5/tumblr_ofw096d7yY1u7z9nwo2_r1_1280.jpg", 
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/6/5/asset/buzzfeed-prod-fastlane-02/sub-buzz-7907-1496740868-1.jpg?downsize=715:*&output-format=auto&output-quality=auto", 
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/7/12/asset/buzzfeed-prod-fastlane-02/sub-buzz-24898-1496852159-2.jpg?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/4/11/asset/buzzfeed-prod-fastlane-01/anigif_sub-buzz-20393-1496589753-2.gif?downsize=715:*&output-format=auto&output-quality=auto", 
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/6/12/asset/buzzfeed-prod-fastlane-01/sub-buzz-22198-1496764820-1.jpg?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/6/20/asset/buzzfeed-prod-fastlane-03/sub-buzz-31686-1496793759-12.jpg?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/1/13/asset/buzzfeed-prod-fastlane-01/sub-buzz-1521-1496338580-1.png?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/2/19/asset/buzzfeed-prod-fastlane-01/anigif_sub-buzz-9317-1496447433-17.gif?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/5/16/asset/buzzfeed-prod-fastlane-03/sub-buzz-31684-1496693723-1.png?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/1/12/asset/buzzfeed-prod-fastlane-01/sub-buzz-15422-1496334265-3.png?downsize=715:*&output-format=auto&output-quality=auto",
"https://pbs.twimg.com/media/DBm1qqIUQAADbjM.jpg:small",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/18/8/asset/buzzfeed-prod-fastlane-01/sub-buzz-20786-1495111584-8.png?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/18/6/asset/buzzfeed-prod-fastlane-02/sub-buzz-11866-1495104803-1.png?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/25/19/asset/buzzfeed-prod-fastlane-01/anigif_sub-buzz-20760-1495754893-9.gif?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/2/10/asset/buzzfeed-prod-fastlane-02/anigif_sub-buzz-13373-1496413625-11.gif?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/1/16/asset/buzzfeed-prod-fastlane-01/sub-buzz-19209-1496349973-3.jpg?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/23/13/asset/buzzfeed-prod-fastlane-02/sub-buzz-23894-1495560759-1.jpg?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/24/11/asset/buzzfeed-prod-fastlane-02/sub-buzz-31236-1495638261-9.jpg?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/24/13/asset/buzzfeed-prod-fastlane-01/sub-buzz-30854-1495646435-2.jpg?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/19/10/asset/buzzfeed-prod-fastlane-01/anigif_sub-buzz-27120-1495203219-12.gif?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/19/9/asset/buzzfeed-prod-fastlane-02/anigif_sub-buzz-17676-1495201611-11.gif?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/19/9/asset/buzzfeed-prod-fastlane-03/anigif_sub-buzz-5850-1495201115-6.gif?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/18/17/asset/buzzfeed-prod-fastlane-02/anigif_sub-buzz-19916-1495143140-1.gif?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/25/15/asset/buzzfeed-prod-fastlane-02/anigif_sub-buzz-21385-1495740539-1.gif?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-05/26/11/asset/buzzfeed-prod-fastlane-02/sub-buzz-6995-1495812595-2.png?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-06/2/11/asset/buzzfeed-prod-fastlane-03/anigif_sub-buzz-1779-1496418471-13.gif?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-04/26/22/asset/buzzfeed-prod-fastlane-02/sub-buzz-10754-1493259428-12.jpg?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-03/24/14/asset/buzzfeed-prod-fastlane-03/sub-buzz-7474-1490381258-9.jpg?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-03/24/14/asset/buzzfeed-prod-fastlane-03/sub-buzz-7419-1490381590-6.jpg?downsize=715:*&output-format=auto&output-quality=auto",
"https://img.buzzfeed.com/buzzfeed-static/static/2017-03/10/12/asset/buzzfeed-prod-fastlane-03/sub-buzz-31431-1489167892-1.png?downsize=715:*&output-format=auto&output-quality=auto"]

imagesNeutral = ["http://img08.deviantart.net/8994/i/2011/089/3/2/cat_stock_part_2_by_theweirdlady-d3ct7a0.jpg", 
"http://www.findcatnames.com/wp-content/uploads/2017/01/tabby-cat-names.jpg"]
#print(funtweet)

#message = funtweet+" "+trendsName+" "+str(tweetSenti)+ " https://www.youtube.com/watch?v=9pzm1lQX0qU"
if tweetSenti >= 0.2:
    heady = random.choice(headlinesMixUpHappy)
    url = random.choice(imagesHappy)
    face = ' :-)'
elif tweetSenti <= -0.3:
    heady = random.choice(headlinesMixUpHappy)
    url = random.choice(imagesSad)
    face = ' >:-('
else:
    heady = random.choice(headlinesMixUpHappy)
    url = random.choice(imagesHappy)
    face = ' :-|'
    
message = heady + " http://1-dot-clickit-169903.appspot.com/ " + ' #' + trendsName + face
#+ " #" +trendsName
tweet_image(url, message)
#time.sleep(180)#Tweet every 15 minutes  
#status = funtweet+" "+trendsName+" "+str(tweetSenti)
#img = os.path.abspath('/images/cat_afraid.jpg')
#api.update_with_media(img, status=status)
#api.update_status(funtweet+" "+trendsName+" "+str(tweetSenti))
      