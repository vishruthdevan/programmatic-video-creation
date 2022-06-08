from moviepy.editor import *

screen_1 = ImageClip('assets/back1.jpg').set_duration(5)
img1 = ImageClip('assets/asset1.png').set_duration(5).set_position('center')
screen_1 = CompositeVideoClip([screen_1, img1])


screen_2 = ImageClip('assets/back2.jpg').set_duration(5)
img1 = ImageClip(
    'assets/asset2.png').resize(2).set_duration(5).set_position(("center", 0.45), relative=True)
text1 = TextClip("We're App Only", fontsize=90, color='white').set_duration(
    5).set_position(("center", 0.2), relative=True)
text2 = TextClip("The ______ app is now available as an app", fontsize=40, font='Calibri light',
                 color='white').set_duration(5).set_position(("center", 0.35), relative=True)
screen_2 = CompositeVideoClip([screen_2, img1, text1, text2])

video = concatenate([screen_1, screen_2], method="compose")
video.write_videofile('test.mp4', fps=24)
