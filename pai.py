import pyttsx3 as pt
import speech_recognition as sr
import webbrowser as wb
import os as os
import smtplib as smp
import wikipedia as wk
import pyautogui as pag
import time as tm
import psutil as ps
import winshell as ws
import pywhatkit as pkt
from email.message import EmailMessage

def run_script(sn):
    try:
        os.system(f"python {sn}")
        speak(f"running script {sn}")
    except Exception as e:
        speak("Failed to run the script")
        print(e)

def speak(txt):
    engine.say(txt)
    engine.runAndWait()
def close():
        speak("Have a nice day sir!")
        exit()  
engine=pt.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',200)
engine.setProperty('volume',1.0)
def mail(to,sub,bod):
    e=EmailMessage()
    e["From"]='krishshukla.11052006@gmail.com'
    e['To']=to
    e['Subject']=sub
    e.set_content(bod)
    with smp.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login('krishshukla.11052006@gmail.com','melgpexmxortfczd')
        smtp.send_message(e)
    speak("Email sent")

def totext():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        speak("listening sir...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)


        try:
            print("Recognizing...")
            txt=r.recognize_google(audio)
            return txt
        except sr.UnknownValueError:
            speak("Sorry, could not understand the audio.")
            return ""
        except sr.RequestError:
            print("Could not request results from google.")
            return ""
        return ""

while(True):
    txt=totext()
    txt=txt.lower()
    speak("you said "+txt)
    com=txt
    com=com.lower()
    if 'close' in com or 'quit' in com:
        close()
    elif "open" in com:
        app=com.replace("open","").strip()
        app=app.lower()
        if 'youtube' in com:
            speak("launching youtube sir")
            wb.open("https://www.youtube.com/")
        elif 'google' in com:
            speak("launching google sir")
            wb.open("https://www.google.com/")
        elif 'vscode' in com or 'code' in com:
            speak("launching vs code")
            os.system('"D:\\VS CODE\\vscode\\Microsoft VS Code\\Code.exe"')
        elif 'valorant' in com:
            speak("enjoy your game sir")
            os.system('"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Riot Games\\VALORANT.lnk"')
        elif 'notepad' in com:
            speak("launching "+app+" sir")
            os.system("start "+app)
    elif 'volume up' in txt:
        for _ in range(5):
            pag.press("volumeup")
            tm.sleep(0.1)
    elif 'volume down' in txt:
        for _ in range(5):
            pag.press("volumedown")
            tm.sleep(0.1)
    elif 'mute' in txt:
        pag.press("volumemute")
    elif 'unmute' in txt:
        pag.press("volumeunmute")
    elif 'shutdown' in txt:
        speak("Shutting down the system...")
        os.system("shutdown /s /t 1")
    elif 'restart' in txt:
        speak("restarting the system...")
        os.system("shutdown /r /t 1")
    elif "battery" in txt:
        bat=ps.sensors_battery()
        per=bat.percent
        speak(f"Battery is at {per} percent.")
    elif "recycle" in txt:
        speak("Emptying the Recycle bin sir...")
        ws.recycle_bin().empty(confirm=True,show_progress=True,sound=True)
    elif "screenshot" in txt:
        ss=pag.screenshot()
        ss.save("ss.png")
        speak("ScreenShot taken and saved sir..")
    elif 'google for' in txt:
        q=txt.replace("google for","").strip()
        speak("Searching google for "+q)
        wb.open(f"https://www.google.com/search?q={q}")
    elif "wikipedia" in txt:
        query = txt.replace("wikipedia for", "").strip()
        speak("Searching Wikipedia for " + query)
        try:
            result = wk.summary(query, sentences=2)
            speak(result)
        except:
            speak("Sorry, I couldn't find that on Wikipedia.")
    elif "youtube" in txt:
        query = txt.replace("youtube", "").strip()
        speak("Searching YouTube for " + query)
        wb.open(f"https://www.youtube.com/results?search_query={query}")
    elif "play" in txt:
        sg=txt.replace("play","").strip()
        speak("playing "+sg)
        pkt.playonyt(sg)
    elif "send email" in txt:
        speak("Who is the recipient?")
        tp=input()
        
        speak("What is the subject?")
        sub=totext()
        speak("What is the content?")
        bod=totext()
        mail(tp,sub,bod)
    elif "weather in" in txt:
        lc=txt.split("weather in")[-1].strip()
        speak(f"Fetching weather for{lc}")
        wb.open(f"https://www.google.com/search?q=weather+in+{lc}")
    elif "news" in txt:
        speak("The latest headlines are")
        wb.open("https://www.google.com/search?q=news&rlz=1C1ONGR_enIN1137IN1137&oq=news&gs_lcrp=EgZjaHJvbWUyDwgAEEUYORiDARixAxiABDIMCAEQIxgnGIAEGIoFMhMIAhAAGIMBGJECGLEDGIAEGIoFMg0IAxAAGJECGIAEGIoFMhMIBBAuGIMBGMcBGLEDGNEDGIAEMg0IBRAAGIMBGLEDGIAEMgoIBhAAGLEDGIAEMg0IBxAAGIMBGLEDGIAEMhAICBAAGIMBGLEDGIAEGIoFMg0ICRAAGIMBGLEDGIAE0gEIMjY1OGowajSoAgiwAgHxBVRY-McMIHUH&sourceid=chrome&ie=UTF-8")
    elif "score" in txt:
        speak("which sports are you searching for?")
        s=totext()
        speak("the updates are")
        wb.open(f"https://www.google.com/search?q={s}+scores&sca_esv=7899e45081c54108&rlz=1C1ONGR_enIN1137IN1137&sxsrf=AHTn8zqO1lHWQm55BxnNTRT-CMt6G11p8Q%3A1747795457773&ei=AT4taIH_LryJ4-EP9PDukQ4&ved=0ahUKEwjBg5q7xbONAxW8xDgGHXS4O-IQ4dUDCBA&uact=5&oq="+s+"+scores&gs_lp=Egxnd3Mtd2l6LXNlcnAiDmNyaWNrZXQgc2NvcmVzMhUQABiABBixAxiDARgUGIcCGEYY_QEyChAAGIAEGEMYigUyERAAGIAEGJECGLEDGIMBGIoFMhEQLhiABBiRAhixAxiDARiKBTIREAAYgAQYkQIYsQMYgwEYigUyChAAGIAEGEMYigUyChAAGIAEGAIYywEyCxAAGIAEGLEDGIMBMggQABiABBixAzIKEAAYgAQYQxiKBUiiR1DwEVjVRnALeACQAQCYAcYBoAGoHKoBBDAuMjK4AQPIAQD4AQGYAiCgArkcqAIKwgIKEAAYsAMY1gQYR8ICBxAjGCcY6gLCAgcQLhgnGOoCwgIKECMYgAQYJxiKBcICCxAAGIAEGJECGIoFwgIOEC4YgAQYkQIY1AIYigXCAhAQABiABBixAxhDGIMBGIoFwgIREC4YgAQYsQMY0QMYgwEYxwHCAgUQLhiABMICBBAjGCfCAg0QABiABBixAxhDGIoFwgIOEAAYgAQYsQMYgwEYigXCAg8QIxiABBgnGIoFGEYY_wHCAhAQLhiABBixAxhDGIMBGIoFwgINEC4YgAQYQxjUAhiKBcICDRAAGIAEGLEDGBQYhwLCAgwQABiABBgCGAoYywHCAhQQABiABBiRAhixAxiDARjJAxiKBcICDhAAGIAEGJECGLEDGIoFwgILEAAYgAQYkgMYigXCAg0QABiABBixAxiDARgKwgIKEAAYgAQYsQMYCsICDRAuGIAEGLEDGIMBGArCAgsQLhiABBiRAhiKBcICEBAAGIAEGLEDGIMBGBQYhwLCAg4QLhiABBiRAhixAxiKBcICCBAuGIAEGLEDwgIFEAAYgATCAgoQABiABBgUGIcCwgIHEAAYgAQYCsICExAAGIAEGJECGLEDGIoFGEYY_QGYAwfxBXSUEr6sYsSCiAYBkAYIkgcHMTEuMTkuMqAH-9EBsgcGMC4xOS4yuAeIHA&sclient=gws-wiz-serp")
    elif "python program" in txt:
        speak("Please say the script name")
        sc=totext()
        run_script(sc+".py")