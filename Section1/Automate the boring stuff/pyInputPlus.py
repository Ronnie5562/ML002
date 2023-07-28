import pyinputplus as pyip

'''
PyInputPlus has several functions for different kinds of input:

inputStr() Is like the built-in input() function but has the general PyInputPlus features. You can also pass a custom validation function to it

inputNum() Ensures the user enters a number and returns an int or float, depending on if the number has a decimal point in it

inputChoice() Ensures the user enters one of the provided choices

inputMenu() Is similar to inputChoice(), but provides a menu with numbered or lettered options

inputDatetime() Ensures the user enters a date and time

inputYesNo() Ensures the user enters a “yes” or “no” response

inputBool() Is similar to inputYesNo(), but takes a “True” or “False” response and returns a Boolean value

inputEmail() Ensures the user enters a valid email address

inputFilepath() Ensures the user enters a valid file path and filename, and can optionally check that a file with that name exists

inputPassword() Is like the built-in input(), but displays * characters as the user types so that passwords, or other sensitive information, aren’t displayed on the screen

NOTE: These functions will automatically reprompt the user for as long as they enter invalid input
'''

import random, time


class MathQuiz:
    
    def start(self):
        numberOfQuestions = 10
        correctAnswers = 0
        for questionNumber in range(numberOfQuestions):
            # Pick two random numbers:
            num1 = random.randint(0, 9)
            num2 = random.randint(0, 9)

            prompt = f'#{questionNumber}: {num1} x {num2} = '

            try:
                # Right answers are handled by allowRegexes.
                # Wrong answers are handled by blockRegexes, with a custom message.
                pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                                        blockRegexes=[('.*', 'Incorrect!')],
                                        timeout=8, limit=3)
            except pyip.TimeoutException:
                print('You are out of time: ')

            except pyip.RetryLimitException:
                print('You are out of tries')
            
            else:
                # This block runs if no exceptions were raised in the try block.
                print('Correct!')
                correctAnswers += 1
            
            time.sleep(1) # Brief pause to let user see the result.
            print('Score: %s / %s' % (correctAnswers, numberOfQuestions))


quiz = MathQuiz()

quiz.start()
