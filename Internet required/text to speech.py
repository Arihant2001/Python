from gtts import gTTS
import os
myText="plants make their food by photosynthesis"
language="en"
output=gTTS(text=myText,lang=language,slow=False)
output.save("ok.mp3")
os.system("start ok.mp3")
