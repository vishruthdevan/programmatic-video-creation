from moviepy.editor import *

screen_1 = ImageClip('assets/back1.jpg').set_duration(5)
img1 = ImageClip('assets/asset1.png').set_duration(5).set_position('center')
screen_1 = CompositeVideoClip([screen_1, img1])
