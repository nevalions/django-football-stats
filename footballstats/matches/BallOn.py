# Calculate where is the ball on the field

def BallOn(field_length: int, ball_on_added: int) -> int:
    if ball_on_added > 0:
        ball_on_real = field_length - ball_on_added
        return ball_on_real
    else:
        ball_on_real = 0 - ball_on_added
        return ball_on_real


print(BallOn(90, -1))
