import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def image_processing(img,data):
	n = 0
	rgb = [0,0,0]
	for i in range(len(data)):	
		rgb[0] = int(data[n]/3)	
		rgb[1] = int(data[n]/3)	
		rgb[2] = data[n] - rgb[0] - rgb[1] 
		while True:
			x = np.random.randint(1,rows-1)
			y = np.random.randint(1,cols-1)
			if (record[x-1,y+1]!=1 and record[x,y+1]!=1 and record[x+1,y+1]!=1 
			and record[x-1,y]!=1 and record[x,y]!=1 and record[x+1,y]!=1 and 
			record[x-1,y-1]!=1 and record[x,y-1]!=1 and record[x+1,y-1]!=1 and
			img[x,y,0]<100 and img[x,y,1]<100 and img[x,y,2]<100):
				break
		record[x-1,y+1] = 1
		record[x,y+1] = 1
		record[x+1,y+1] = 1
		record[x-1,y] = 1
		record[x,y] = 1
		record[x+1,y] = 1
		record[x-1,y-1] = 1
		record[x,y-1] = 1
		record[x+1,y-1] = 1
		key[n,0] = x
		key[n,1] = y
		for m in range(3):
			s = int(rgb[m]/9)
			img[x-1,y+1,m] += s
			img[x,y+1,m] += s
			img[x+1,y+1,m] += s
			img[x-1,y,m] += s
			img[x,y,m] += s
			img[x+1,y,m] += s
			img[x-1,y-1,m] += s
			img[x,y-1,m] += s
			img[x+1,y-1,m] += rgb[m] - 8*s
		n+=1
	return img

def show_position(img,key):
	for x,y in key:
		img[x,y,:] = 255
	return img



def print_matadata():
	print ("Numbers of the character in plaintext: ",end="")
	print (len(msg))
	# numbers of rows, colums and channels
	print ("The type of the image: ",end="")
	print (img.dtype)
	print ("The shape of the image: ",end="")
	print (img.shape) 
	print ("The size of the image: ",end="")
	print (img.size)


def plot(img):
	plt.figure('cat_processed')
	plt.imshow(img)
	plt.axis('off')
	plt.show()


if __name__ == '__main__':

	np.set_printoptions(threshold=np.nan)

	#read image and convert it into matrix
	image_filename = "cat.jpg"
	img = np.array(Image.open(image_filename)) 
	rows,cols,dims=img.shape
	record = np.zeros(shape=[rows,cols],dtype=int) 

	#read plaintext 
	message_filename = "plaintext.txt"
	msg = [] # msg is the text format of plaijntext
	with open(message_filename,"r") as f:   
		msg = f.read()
	data = [] # data is the ASCII value of plaintext
	for w in msg:
		data.append(ord(w))
	key = np.zeros(shape=[len(data),2],dtype=int)

	img_enc = image_processing(img,data)
	plt.imsave('cat+',img_enc,cmap='gray')

	print_matadata()

	img1 = show_position(img,key)
	plot(img_enc)










