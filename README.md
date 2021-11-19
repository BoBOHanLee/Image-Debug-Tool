# Image-Debug-Tool

A HMI tool which support streaming , log showing , script and photo grabing

###### **Enviromnet building**
1. Download git and clone the file.  
        `git clone http://ginga.vivotek.tw:3000/hank.lee/Image-Debug-Tool.git`
2. Download python 3.6 https://www.python.org/downloads/windows/
3. Add enviroment valuables for python.exe
4. Go to cmd. 
        `pip install -r requirements.txt`
5. Go to Image-Debug-Tool file and run the tool.
        `python StreamTemplate.py`



###### **There is this tool's basic function**
![Alt text](HMI_photo.PNG)
1. Support ssh/telnet connection

2. Streaming and image infomation showing
   * User can calculate/detect any image info from the image
   * User can observe streaming image and image info simultaneously
   
3. Commend window and Log filter window
   * User can type any linux commend or script to the machine
   * User can design any log showing method 
     ex. 'Shutter'&&'ISO' means that the debug window will show the log which contains the string 'Shutter' and 'ISO'
![Alt text](HMI_log.PNG)

4. Customized functions (ex. Take picture button)
  * User can design any functions to meet specific needs. (ex. Take a photo any time, like below)
![Alt text](test.jpg)

