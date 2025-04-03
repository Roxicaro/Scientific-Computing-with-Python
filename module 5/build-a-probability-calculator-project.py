import copy
import random

class Hat:
    def __init__(self, **args):
        #Dictionary containing all arguments and their values
        self.colors = {color: number for color, number in args.items()}
        
        #Defining HAT Contents
        self.contents = []
        for color,number in self.colors.items():
            int(number)
            counter = 0
            while counter < number:
                self.contents.append(f'{color}')
                counter += 1

    #__STR__ METHOD:
    def __str__(self):
        return f'{self.contents}'
    
    #Random Draw method (Returns string list with balls drawn)
    def draw(self, number):
        self.balls_drawn = []
        counter = 0
        if number <= len(self.contents):
            while counter < number:
                ball_drawn = random.choice(self.contents)
                self.balls_drawn.append(ball_drawn) 
                self.contents.remove(ball_drawn)
                counter += 1
            return self.balls_drawn
        else:
            for i in self.contents:
                self.balls_drawn.append(i)
            self.contents.clear()
            return self.balls_drawn
    
    #Reset draw
    def reset(self):
        self.contents = []
        for color,number in self.colors.items():
            int(number)
            counter = 0
            while counter < number:
                self.contents.append(f'{color}')
                counter += 1       
    

#Experiment Function<<<<<<<<<<<<<
def experiment(*,hat, expected_balls, num_balls_drawn, num_experiments):
    #Get and save contents of Hat
    balls = hat.contents

    def draw_ball():
        balls_drawn = hat.draw(num_balls_drawn)
        drawn_dict = {ball:balls_drawn.count(ball) for ball in balls_drawn}
        hat.reset()
        
        #Check if all colors in the expected_balls appear in the draw
        all_colors_in = all(color in drawn_dict for color in expected_balls)

        #Check if the number of balls drawn are >= the number of balls expected
        if all_colors_in:
            if all(expected_balls[color] <= drawn_dict[color] for color in expected_balls if color in drawn_dict):
                return 1
            else:
                return 0      
        else:
            return 0   

           
    count = 0
    success = 0
    while count < num_experiments:
        if draw_ball() == 1:
            success += 1
            count += 1
        else:
            count += 1

    probability = success / num_experiments
    return probability
    

#TESTING

hat = Hat(black=6, red=4, green=3)

print(experiment(hat=hat,
                  expected_balls={'red':1,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000))
