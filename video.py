import os
import cv2

path =r"C:\Users\ASHUTOSH ARYAN\OneDrive\Desktop\coding\module 3\project\C---105[VIDEO ALBUM]\PRO-C105-Project-Images-main\Images"
images= []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file
        print(file_name)
        images.append(file_name)
        
print(len(images))
count = len(images)


video = cv2.imread(images[0])
height, width , channels = video.shape
size = (width , height)


out = cv2.VideoWriter("friendship.mp4",cv2.VideoWriter_fourcc(*'DIVX'),10,size)
for i in range(count-1,0,-1):
    video = cv2.imread(images[i])
    out.write(video)

out.release()
print("Done it!")