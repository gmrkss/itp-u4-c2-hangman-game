from .exceptions import *
from random import randint

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if len(list_of_words)<1:
        raise InvalidListOfWordsException
    else:
        return list_of_words[randint(0,len(list_of_words)-1)]
        

def _mask_word(word):
    if word!='':
        return '*'*len(word)
    else:
        raise InvalidWordException


def _uncover_word(answer_word, masked_word, character):
    if answer_word=='' or masked_word=='':
        raise InvalidWordException
    if len(character)>1:
        raise InvalidGuessedLetterException
    if len(answer_word)!=len(masked_word):
        raise InvalidWordException
    answer_word=answer_word.lower()
    character=character.lower()
    if character in answer_word:
        answer_word_chars=[]
        masked_word_chars=[]
        for char in answer_word:
            answer_word_chars.append(char)
        for char in masked_word:
            masked_word_chars.append(char)
        
        for index, char in enumerate(answer_word_chars):
            if char==character:
                masked_word_chars[index]=character

        masked_word=''.join(masked_word_chars)
        
        return masked_word
    if character not in answer_word:
        return masked_word

# passes all tests except for last two
def guess_letter(game, letter):
    letter=letter.lower()
    res=_uncover_word(game['answer_word'], game['masked_word'],letter)
    if res!=game['masked_word']:
        game['masked_word']=res
        game['previous_guesses'].append(letter)
    else:
        game['remaining_misses']-=1
        game['previous_guesses'].append(letter)
    if game['masked_word']==game['answer_word'] and game['remaining_misses']>0:
        raise GameWonException
    if game['masked_word']!=game['answer_word'] and game['remaining_misses']==0:
        raise GameLostException

# test code for error handling
# def guess_letter(game, letter):
#     try:
#         letter=letter.lower()
#         res=_uncover_word(game['answer_word'], game['masked_word'],letter)
#         if res!=game['masked_word']:
#             game['masked_word']=res
#             game['previous_guesses'].append(letter)
#         else:
#             game['remaining_misses']-=1
#             game['previous_guesses'].append(letter)
#         if game['masked_word']==game['answer_word'] and game['remaining_misses']>0:
#             raise GameWonException
#         if game['masked_word']!=game['answer_word'] and game['remaining_misses']==0:
#             raise GameLostException
#     except GameWonException:
#         raise GameFinishedException
#     except GameLostException:
#         raise GameFinishedException


def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
