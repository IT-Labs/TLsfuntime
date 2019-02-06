
import time
from enum import Enum
import random
#0:'angry',1:'disgust',2:'fear',3:'happy',4:'sad',5:'surprise',6:'neutral'
class Emotion(Enum):
    ANGRY = 1
    SAD = 2
    HAPPY = 3
    SURPRISE = 4
	  
def get_hour_of_day():
	currentTime = '14'
	#currentTime = time.strftime('%H')    
	print(currentTime)	


def get_greeting(name, emotion_in):  

	emotion_lower=emotion_in.lower()

	if emotion_lower == 'angry' or emotion_lower == 'disgust':
		emotion=1
	elif emotion_lower == 'fear' or  emotion_lower == 'sad':
		emotion=2
	elif emotion_lower == 'happy' or emotion_lower == 'neutral':
		emotion=3
	else:
		emotion=4
		
	user_hour = int(time.strftime('%H'))	 
   
	if 0 <= user_hour < 8:   
		part_of_day=1
	elif 8 <= user_hour <11:
		part_of_day=2
	elif 11<=user_hour<13:
		part_of_day=3
	elif 13<=user_hour<17:
		part_of_day=4
	else:
		part_of_day=5	 
	

	messageIndex = int(int(part_of_day) * int(emotion) * int(random.randint(0,2)))
   	
	messages = [
	#early morning
	# angry  
            'Look at the bright side of the day',  
            'The day is still ahead of you be positive',  
		    'Is this the best you can do',  
	#SAD
            'There is no hope for you today', 
			'Put a smile on that pretty face', 
			'The day is ahead of you be positive', 
	#HAPPY		
			'So happy in the morning What is wrong with you?',  
			'Nice to see a happy face so early in the morning', 
			'You rock',
	#surprise
			'Hope that the reason for your happiness is being part of IT Labs team',  
			'Give me five minutes of your time and I will be happy the rest of the day',
			'Surprise Nobody is at work It is weekend',

	#morning       
	#angry     
            'It is sunny please smile', 
            'The day is still ahead of you be positive',  
		    'You and your bed are perfect for each other, but the alarm clock keeps trying to break you apart',  
    #sad
	        'Your troubles will decrease if you share them with friends',  			
			'Do not wait for someone, who will make you happy!', 
			'Do not wait for the perfect moment Take the moment and make it perfect', 
	#HAPPY		
			'Your happiness will increase if you make someone happy!', 
			'It is a real talent to be happy: appreciate what you have, and like what you do!', 
			'Becoming happy with money or things is impossible. Only people are able to make you happy.',	
	#surprise
			'Hope that the reason for your happiness is being part of IT Labs team', 
			'Give me five minutes of your time and I will be happy the rest of the day',
			'Surprise Nobody is at work It is weekend',
	#noon
    #angry
			'The world cannot make you happy But you can create the world, in which you will be happy!', 
		   'Your happiness will increase if you make someone happy!',
		   'Nothing will make you happier than your thoughts',
	#sad
		   'If you want to be a champion, do not forget about self-awareness', 
		   'Maybe if we tell people the brain is an app, they will start using it',
		   'Sometimes to be happy you just need someone, who will cook lunch for you',
	#happy
		   'The happiness of each your day begins with your morning thoughts! Think positively, and be happy!',
		   'You seems like a super nice and awesome, we should talk more!',
		   'The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty',
	#suprisse
			'If you want always be on trend, be yourself, and be happy',
			'it has been a long time since we spoke but i still think about you',
			'Do not take life too seriously. You will never get out of it alive',
	#afternoon

	#angry 
		   'Do not take life too seriously. You will never get out of it alive',
		   'Sometimes I just can not ignore the way I feel when I see you smile',	
		   'I have seen the best of you, and the worst of you, and I choose both.',	   
	#sad 
			'All of life is peaks and valleys. Do not let the peaks get too high and the valleys too low',
			'No matter what people tell you, words and ideas can change the world',
			'Age is something that does not matter, unless you are a cheese',
	#happy 
			'Sometimes I just can not ignore the way I feel when I see you smile',
			'It is a real talent to be happy: appreciate what you have, and like what you do',
			'you seem super nice and awesome, we should talk more',
	#suprisse
			'You only live once, but if you do it right, once is enough',
			'Quality is never an accident It is always the result of intelligent effort',
		    'Effort only fully releases its reward after a person refuses to quit',
 
#evening

#angry
		 'Think in the morning. Act in the noon. Eat in the evening. Sleep in the night',
		 'The amount of effort you put in is the amount of results you end up with',
		 'A winning effort begins with preparation',
	#sad 
		'If you cannot do great things, do small things in a great way.',
		'There is often a much simpler way of doing things – if you make the effort to look for it',
		'Get mad, then get over it',
	#happy
		'Do a little more each day than you think you possibly can',
		'The difference between ordinary and extraordinary is that little extra',
		'Strength and growth come only through continuous effort and struggle',
	#supprise
		'For every disciplined effort there is a multiple reward',
		'What is written without effort is in general read without pleasure',
		'The one thing that matters is the effort.'
	]
	return '%s, %s' % (name,messages[messageIndex])
	
