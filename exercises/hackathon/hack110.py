"""Our Hack110 project: How to Train Your COMP 110 Student!"""

import pygame 
from pygame.locals import *
import sys

pygame.font.init()

# username: str = input("Enter your username: ")
#print(f"Welcome!/n You have reached Berk, the home of many dragons. /n Hiccup Haddock, our local dragon expert, will be your coach today.")
pygame.init() 

text_font = pygame.font.SysFont('Impact', 20)

# Background music
test_drive: bool = True
pygame.mixer.music.load("/Users/sophiamcreynolds/comp110-23f-workspace/exercises/hackathon/test_drive.mp3")
pygame.mixer.music.play(loops=-1)
  
color = (255,255,255) 
position = (500,500)
  
# CREATING CANVAS 
canvas = pygame.display.set_mode((1000,1000)) 
  
# TITLE OF CANVAS 
pygame.display.set_caption("How to Train Your COMP 110 Student!") 
  
toothless = pygame.image.load("/Users/sophiamcreynolds/comp110-23f-workspace/exercises/hackathon/toothless.webp") 
hiccup = pygame.image.load("/Users/sophiamcreynolds/comp110-23f-workspace/exercises/hackathon/Character_Hiccup_02.webp")
berk = pygame.image.load("/Users/sophiamcreynolds/comp110-23f-workspace/exercises/hackathon/berk.jpeg")
hic_and_tooth = pygame.image.load("/Users/sophiamcreynolds/comp110-23f-workspace/exercises/hackathon/hic_and_tooth.jpeg")

# Scale hiccup
hiccup = pygame.transform.scale(hiccup, (200, 500))
berk = pygame.transform.scale(berk, (1000, 1000))

# textbox -------------------------------------------------
title_text = text_font.render("How to Train Your COMP 110 Student!", True, (0, 0, 0))
title_textRect = title_text.get_rect()
title_textRect.center = (500, 55)
text1 = "This is Berk, the home of dragons. Hiccup Haddock, our local dragon expert, will be your coach today."
#text2 = "Let's get started! (Press down to continue)"
text = text_font.render(f"{text1}", True, (0, 0, 0))
textRect = text.get_rect()
textRect.center = (500, 700)

q_null = ""
true_null = ""
false_null = ""
q1 = "Question 1: Stormfly is a Deadly Nadder." # True
q2 = "Question 2: The Hideous Zippleback has three heads." # False
q3 = "Question 3: Toothless likes eels." # False
q4 = "Question 4: Hiccup lost his left leg." # True
q5 = "Question 5: Snotlout and Hiccup are BFFS" # False
question = text_font.render(f"{q_null}", True, (0, 0, 0))
questionRect = question.get_rect()
questionRect.center = (100, 650)

true = "Left Button: True"
false = "Right Button: False"
true_button = text_font.render(f"{true_null}", True, (0, 0, 0))
true_buttonRect = true_button.get_rect()
true_buttonRect.center = (100, 750)
false_button = text_font.render(f"{false_null}", True, (0, 0, 0))
false_buttonRect = false_button.get_rect()
false_buttonRect.center = (750, 750)

result_dict: dict[str, int] = {"Correct": 0, "Incorrect": 0}


s_null = ""
correct_text = "You got it!"
incorrect_text = "Careful there."
correct_feedback = text_font.render(f"{s_null}", True, (0, 0, 0))
correct_feedbackRect = correct_feedback.get_rect()
correct_feedbackRect.center = (450, 750)
incorrect_feedback = text_font.render(f"{s_null}", True, (0, 0, 0))
incorrect_feedbackRect = incorrect_feedback.get_rect()
incorrect_feedbackRect.center = (450, 750)


num_correct: dict[str, int] = {"correct": 0, "incorrect": 0}
total_feedback = text_font.render(f"{s_null}", True, (0, 0, 0))
total_feedbackRect = total_feedback.get_rect()
total_feedbackRect.center = (550, 650)

num_questions: int = 10

fail: str = "You failed :("
fail_feedback = text_font.render(f"{s_null}", True, (0, 0, 0))
fail_feedbackRect = fail_feedback.get_rect()
fail_feedbackRect.center = (450, 700)
passed: str = "You passed! Now, are you ready to train a dragon?"
pass_feedback = text_font.render(f"{s_null}", True, (0, 0, 0))
pass_feedbackRect = pass_feedback.get_rect()
pass_feedbackRect.center = (300, 700)
question_number = 1
exit = False

while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
    
    if event.type == KEYDOWN:
        if event.key == K_UP:
            text = text_font.render(f"{s_null}", True, (0, 0, 0))
            question = text_font.render(f"{q1}", True, (0, 0, 0))
            true_button = text_font.render(f"{true}", True, (0, 0, 0))
            false_button = text_font.render(f"{false}", True, (0, 0, 0))
        if event.key == K_LEFT:
            if question_number == 1 or question_number == 4:
                correct_feedback = text_font.render(f"{correct_text}", True, (0, 0, 0))
                result_dict["Correct"] += 1
            else:
                incorrect_feedback = text_font.render(f"{incorrect_text}", True, (0, 0, 0))
                result_dict["Incorrect"] += 1
            true_button = text_font.render(f"{s_null}", True, (0, 0, 0))
            false_button = text_font.render(f"{s_null}", True, (0, 0, 0))
        elif event.key == K_RIGHT:
            if question_number == 2 or question_number == 3 or question_number == 5:
                correct_feedback = text_font.render(f"{correct_text}", True, (0, 0, 0))
                result_dict["Correct"] += 1
            else:
                incorrect_feedback = text_font.render(f"{incorrect_text}", True, (0, 0, 0))
                result_dict["Incorrect"] += 1
            true_button = text_font.render(f"{s_null}", True, (0, 0, 0))
            false_button = text_font.render(f"{s_null}", True, (0, 0, 0))
        if event.key == K_DOWN:
            question_number = 2
            question = text_font.render(f"{q2}", True, (0, 0, 0))
            true_button = text_font.render(f"{true}", True, (0, 0, 0))
            false_button = text_font.render(f"{false}", True, (0, 0, 0))
            correct_feedback = text_font.render(f"{s_null}", True, (0, 0, 0))
            incorrect_feedback = text_font.render(f"{s_null}", True, (0, 0, 0))
        if event.key == K_LSHIFT:
            question_number = 3
            question = text_font.render(f"{q3}", True, (0, 0, 0))
            true_button = text_font.render(f"{true}", True, (0, 0, 0))
            false_button = text_font.render(f"{false}", True, (0, 0, 0))
            correct_feedback = text_font.render(f"{s_null}", True, (0, 0, 0))
            incorrect_feedback = text_font.render(f"{s_null}", True, (0, 0, 0))
        if event.key == K_RSHIFT:
            question_number = 4
            question = text_font.render(f"{q4}", True, (0, 0, 0))
            true_button = text_font.render(f"{true}", True, (0, 0, 0))
            false_button = text_font.render(f"{false}", True, (0, 0, 0))
            correct_feedback = text_font.render(f"{s_null}", True, (0, 0, 0))
            incorrect_feedback = text_font.render(f"{s_null}", True, (0, 0, 0))
        if event.key == K_RETURN:
            question_number = 5
            question = text_font.render(f"{q5}", True, (0, 0, 0))
            true_button = text_font.render(f"{true}", True, (0, 0, 0))
            false_button = text_font.render(f"{false}", True, (0, 0, 0))
            correct_feedback = text_font.render(f"{s_null}", True, (0, 0, 0))
            incorrect_feedback = text_font.render(f"{s_null}", True, (0, 0, 0))
        if event.key == K_TAB:
            test_drive is False
            question = text_font.render(f"{s_null}", True, (0, 0, 0))
            correct_feedback = text_font.render(f"{s_null}", True, (0, 0, 0))
            incorrect_feedback = text_font.render(f"{s_null}", True, (0, 0, 0))
            if result_dict["Correct"] > result_dict["Incorrect"]:
                pass_feedback = text_font.render(f"{passed}", True, (0, 0, 0))
            elif result_dict["Incorrect"] > result_dict["Correct"]:
                fail_feedback = text_font.render(f"{fail}", True, (0, 0, 0))



            

    canvas.fill(color)
    canvas.blit(hic_and_tooth, dest = (-250,0))
    pygame.draw.rect(canvas, (150, 75, 0), pygame.Rect((290, 30, 420, 50)))
    pygame.draw.rect(canvas, (255, 253, 208), pygame.Rect((300, 40, 400, 30)))
    pygame.draw.rect(canvas, (150, 75, 0), pygame.Rect((40, 590, 920, 220)))
    pygame.draw.rect(canvas, (255, 253, 208), pygame.Rect((50, 600, 900, 200)))
    canvas.blit(title_text, title_textRect)
    canvas.blit(text, textRect)
    canvas.blit(question, questionRect)
    canvas.blit(true_button, true_buttonRect)
    canvas.blit(false_button, false_buttonRect)
    canvas.blit(correct_feedback, correct_feedbackRect)
    canvas.blit(incorrect_feedback, incorrect_feedbackRect)
    canvas.blit(pass_feedback, pass_feedbackRect)
    canvas.blit(fail_feedback, fail_feedbackRect)
    pygame.display.flip()
    pygame.display.update() 