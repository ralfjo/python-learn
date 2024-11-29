Turtle class
https://docs.python.org/3/library/turtle.html

```
1. scoreboard
2. 공 이동
3. 유저1 이동
4. 유저2 이동
```

```
1. create the screen
2. create and move a paddle
3. create another paddle
4. create the ball and make it move
5. detect collision with wall and bounce
6. detect collision with paddle
7. detect when paddle misses
8. keep score
``` 

Paddle class
```
Refactor the code. Create a paddle.py file for the Paddle class.
The Paddle class needs to inherit from Turtle.
Paddle objects need to be initalised with a tuple for the X and Y coordinates.
The l_paddle needs to move up and down with the 'w' and 's' keys
```

Detect when paddle misses
```
Detect if the ball goes out of bounds at the edge of the screen.
If yes, reset the ball's position to the center of the screen.
the ball should when start moving towards the other player.
```