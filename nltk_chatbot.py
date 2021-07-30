from nltk.chat.util import Chat, reflections 

reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

pairs =[ 
	['my name is (.*)', ['Hello ! % 1']], 
	['(hi|hello|hey|holla|hola|hi jackson|hello jackson|hey jackson)', ['Hey !', 'Hello !', 'Hi']], 
	['(.*) your name', ['My name is Jackson.']], 
	['(.*) do you do', ['I am  Chatbot and I entertain you.']], 
	['(.*) created you', ['Joel Shine created me using Python and Natural Language Processing.']],
        ['(.*) are you', ['I am fine. Thanks for asking !']],
        ['(.*) you like (.*)', ['I like to interact with people and of course entertain everyone.']],
        ['(close|quit|bye|take care)', ['It was nice talking to you', 'Bye. Have a good day.']],
        ['(.*) sad (.*)', ['What happened ? Are you okay ?', 'What happened ?']],
        ['(no|nope|not okay|(.*) not okay|not ok|(.*) not ok)', ['Oh, I see. Well what happened ?']],
        ['(yes|yes i will|yes (.*)|i will do it|i will)', ['Yes. That\'s my friend !']],
        ['(.*) sad', ['What happened ? Are you okay ?', 'What happened ?']],
        ['(.*) low marks (.*)', ['It\'s Ok friend. Maybe we can improve next time. Never give up. You can do it.']],
        ['(.*) low marks ', ['It\'s Ok friend. Maybe we can improve next time. Never give up. You can do it.']],
        ['(.*) beaten (.*)', ['It\'s Ok friend. Maybe you did some naughtiness. But you can try to correct it.']],
        ['(.*) beat (.*)', ['It\'s Ok friend. Maybe you did some naughtiness. But you can try to correct it.']],
        ['(.*) doing (.*) study', ['It\'s Ok friend. You have to fix some time for doing things so that everything will be fine.']],
        ['(.*) watching youtube (.*) study', ['It\'s Ok friend. Maybe you have to fix some time for watching youtube.']],
        ['(.*) watching youtube (.*) studying', ['It\'s Ok friend. Maybe you have to fix some time for watching youtube.']]
] 

def Jackson():
    print("My name is Jackson and I am a ChatBot.")
    print("Please type in lowercase letters to start a conversation.")
    print("")

Jackson()
chat = Chat(pairs, reflections) 
chat.converse()
