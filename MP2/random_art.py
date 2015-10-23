##random_art.py creates and saves randomized visualizations of chosen dimensions
##using pseudo-random nested functions and values. 
from random import choice
from random import random
from random import randint
from PIL import Image
import math

#Pixel dimensions of final image
xdimension = 300
ydimension = 300

#Function complexity
depth = randint(10,50)

# this looks great as is and works well
# but looking at the min_depth / max_depth arguments as its shown on the website
# and looking into implementing them would have been a good way to go further
#Create random function list
def recurse(depth):
	funcs = ["x", "y", "prod(a,b)", "cos", "sin", "cos_pi", "sin_pi", "absval", "sec"]    
	params = ["x", "y"]

	if depth <= 1:
		return [choice(funcs), choice(params)]
	else: 
		return [choice(funcs), recurse(depth-1)]
#Interpret function list into interpretable function
def evalfunc(func, a, b):
	if func[0] == "x" :
	    return a
	elif func[0] == "y":
	    return b
	elif func[0] == "prod(a,b)":
	    return a*b
	elif func[0] == "cos":
	    return math.cos(evalfunc(func[1], a, b))
	elif func[0] == "sin" :
	    return math.sin(evalfunc(func[1], a, b))
	elif func[0] == "cos_pi":
	    return math.cos(math.pi*evalfunc(func[1], a, b))
	elif func[0] == "sin_pi":
	    return math.sin(math.pi*evalfunc(func[1], a, b))
	# Why does secant work even though it doesn't give numbers in the range -1 to 1?
	# your images look fine but I'm a little surprised
	elif func[0] == "sec" :
	    return 1/math.cos(evalfunc(func[1], a, b/2))
	elif func[0] == "absval":
		return abs(evalfunc(func[1], a, b))
	# be careful of indents - all these lines had an extra space in them

#Remap values from one interval to another
def remap(float_val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
	input_diff = input_interval_end - float_val
	input_size = input_interval_end - input_interval_start
	output_size = output_interval_end - output_interval_start

	proportion = input_diff / input_size

	output_diff = proportion * output_size

	new_val = output_interval_end - output_diff

	return new_val


if __name__ == "__main__":
    #create image file
	im = Image.new("RGB",(xdimension,ydimension))
	val_array = im.load()
	#generate a random function for each color
	redfxy = recurse(depth)
	grnfxy = recurse(depth)
	blufxy = recurse(depth)

	#plot the functions in the image file
	for a in range (0,xdimension):
		for b in range (0,ydimension):
			#remap the random input values for evalfunc
			aremap = remap(float(a), 0, xdimension, -1, 1)
			bremap = remap(float(b), 0, ydimension, -1, 1)
            #evaluate each color's random function 
			rf = evalfunc(redfxy, aremap, bremap)
			gf = evalfunc(grnfxy, aremap, bremap)
			bf = evalfunc(blufxy, aremap, bremap)
			#map the function output to an RGB value
			rfremap = int(remap(rf, -1, 1, 0, 255))
			gfremap = int(remap(gf, -1, 1, 0, 255))
			bfremap = int(remap(bf, -1, 1, 0, 255))
			#assign each pixel an RGB value
			val_array[a,b] = (rfremap, gfremap, bfremap)
    #Save the image (and give it a random integer file name, in the spirit of the project).
	im.save(str(randint(1,1000)) +".jpg" ,"JPEG" )
	




