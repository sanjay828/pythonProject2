import time
from turtle import Screen
from snak import snaak
from food import Food
from scoreboard import Scoreboard
screen=Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
snakke=snaak()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snakke.up,"Up")
screen.onkey(snakke.down,"Down")
screen.onkey(snakke.left,"Left")
screen.onkey(snakke.right,"Right")
game_is_on= True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snakke.move()
    if snakke.head.distance(food)<15:
        food.refresh()
        snakke.extend()
        scoreboard.increasescore()
    if snakke.head.xcor()>280 or snakke.head.xcor() < -280 or snakke.head.ycor()>280 or snakke.head.xcor()<-280:
        game_is_on=False
        scoreboard.gamerover()
    for segment in snakke.segment:
        if segment== snakke.head:
            pass
        elif snakke.head.distance(segment)<10:
            game_is_on= False
            scoreboard.gamerover()





















screen.exitonclick()