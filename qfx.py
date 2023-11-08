from selenium import webdriver
import winsound
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import discord_webhook

import time

from datetime import date
from datetime import datetime
import csv
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")

url = 'https://www.qfxcinemas.com'
s = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=s,options=chrome_options)
driver.get(url)
duration = 1000  # milliseconds
freq = 440  # Hz
movieName = 'The Marvels'
mainMovie1 = 'Doctor Strange in the Multiverse of Madness'
hallName = 'QFX Civil Mall (Kathmandu Valley)'  # QFX Civil Mall (Kathmandu Valley)
mainMovie = movieName #assign movie name here
mainMovie = mainMovie.upper()
foundOnCS = False
foundOnNS = False
delayy = 0
numOfTickets = 8   # +1
offset = 2






def mainvitrakomain():
    global numOfTickets
    schedules = []
    hall = driver.find_elements(By.CLASS_NAME,'show-hall-name')
   
    for k in hall:
        if k.text == hallName:
            parentOf = k.find_element(By.XPATH,'..') 
            schedules = parentOf.find_elements(By.TAG_NAME,'a')
    

            
    for l in range(0,(len(schedules)),1):
        time.sleep(2)
        header = driver.find_element(By.CLASS_NAME,'show-movies-header')
        datee = header.find_element(By.TAG_NAME,'span').text
        
        if datee == 'Today':
            datee = '[ '+ date.today().strftime("%B %d, %Y") + ' ]'
        elif datee == 'Tomorrow':
            datee = '[ '+ (date.today() + timedelta(days = 1)).strftime("%B %d, %Y") + ' ]'

        hall = driver.find_elements(By.CLASS_NAME,'show-hall-name')
        for k in hall:
            if k.text == hallName:
                parentOf = k.find_element(By.XPATH,'..') 
                schedules = parentOf.find_elements(By.TAG_NAME,'a')

        if schedules[l].get_attribute("class") != 'time-mark expired ng-star-inserted' and schedules[l].get_attribute("class") != 'time-mark soldout ng-star-inserted':
            temp = datee + ' ' + str((schedules[l].text).replace('\n',' '))
            schedules[l].click()
            validSeats = 0
            time.sleep(4)
            


            #raatattata
            rows = driver.find_elements(By.CSS_SELECTOR, 'span.seat-row-letter')
            tobeclicked = []

            for row in rows:
              
                if row.text == 'F' and validSeats < numOfTickets :
                    rowparent = row.find_element(By.XPATH,'..')
                   
                    
                    availSeatsparent = rowparent.find_elements(By.CSS_SELECTOR, 'div.ng-star-inserted')
                    noOfseats = len(availSeatsparent)
                    avails = []
                    for elem in availSeatsparent:
                        
                        buttonfinder = elem.find_element(By.TAG_NAME, 'button').get_attribute('class')
                       
                        if buttonfinder == 'seat-btn Available' or buttonfinder == 'seat-btn YourSeat':
                           
                            avails.append(int(elem.text))
                            
                    avails.sort()
                    consec = 1
                    for p in range(9,noOfseats,1):
                        if p in avails and (p+1) in avails and validSeats < numOfTickets and consec < numOfTickets:
                            consec = consec + 1
                        elif p in avails and not (p+1) in avails and consec > 1 and validSeats < numOfTickets:
                            req = numOfTickets  - validSeats
                            if consec >= req:
                                consec = req
                            validSeats = validSeats + consec
                            for m in range(p-consec+1,p+1,1):
                                tobeclicked.append(row.text + str(m))
                            consec = 1
                        elif p in avails and (p+1) in avails and validSeats < numOfTickets and consec == numOfTickets:
                            req = numOfTickets  - validSeats
                            if consec >= req:
                                consec = req
                            validSeats = validSeats + consec
                            for m in range(p-consec+1,p+1,1):
                                tobeclicked.append(row.text + str(m))
                            consec = 1



                    consec = 1 
                    for p in range(9,0,-1):
                        if (row.text + str(9)) in tobeclicked and (row.text + str(10)) in tobeclicked:
                            continue
                        if p in avails and (p-1) in avails and validSeats < numOfTickets and consec < numOfTickets :
                            consec = consec + 1
                        elif p in avails and not (p-1) in avails and consec > 1 and validSeats < numOfTickets:
                            req = numOfTickets - validSeats
                            if consec >= req:
                                consec = req
                            validSeats = validSeats + consec
                            for m in range(p+consec-1,p-1,-1):
                                tobeclicked.append(row.text + str(m))
                            consec = 1
                        elif p in avails and (p-1) in avails and validSeats < numOfTickets and consec == numOfTickets :
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p+consec-1,p-1,-1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1
                            

                    
                    

            if(validSeats < numOfTickets):
                for row in rows:
                    if row.text == 'G' and validSeats < numOfTickets:
                        rowparent = row.find_element(By.XPATH,'..')
                        
                        availSeatsparent = rowparent.find_elements(By.CSS_SELECTOR, 'div.ng-star-inserted')
                        avails = []
                        for elem in availSeatsparent:
                            buttonfinder = elem.find_element(By.TAG_NAME, 'button').get_attribute('class')
                            if buttonfinder == 'seat-btn Available' or buttonfinder == 'seat-btn YourSeat':
                                avails.append(int(elem.text))
                        avails.sort()
                        consec = 1
                        for p in range(9,noOfseats,1):
                            if p in avails and (p+1) in avails and validSeats < numOfTickets and consec < numOfTickets :
                                consec = consec + 1
                            elif p in avails and not (p+1) in avails and consec > 1 and validSeats < numOfTickets:
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p-consec+1,p+1,1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1
                            elif p in avails and (p+1) in avails and validSeats < numOfTickets and consec == numOfTickets:
                                req = numOfTickets  - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p-consec+1,p+1,1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1



                        consec = 1 
                        for p in range(9,0,-1):
                            if (row.text + str(9)) in tobeclicked and (row.text + str(10)) in tobeclicked:
                                continue
                            if p in avails and (p-1) in avails and validSeats < numOfTickets and consec < numOfTickets :
                                consec = consec + 1
                            elif p in avails and not (p-1) in avails and consec > 1 and validSeats < numOfTickets:
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p+consec-1,p-1,-1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1
                            elif p in avails and (p-1) in avails and validSeats < numOfTickets and consec == numOfTickets :
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p+consec-1,p-1,-1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1

            if(validSeats < numOfTickets):
                for row in rows:
                    if row.text == 'H' and validSeats < numOfTickets:
                        rowparent = row.find_element(By.XPATH,'..')
                        
                        availSeatsparent = rowparent.find_elements(By.CSS_SELECTOR, 'div.ng-star-inserted')
                        avails = []
                        for elem in availSeatsparent:
                            buttonfinder = elem.find_element(By.TAG_NAME, 'button').get_attribute('class')
                            if buttonfinder == 'seat-btn Available' or buttonfinder == 'seat-btn YourSeat':
                                avails.append(int(elem.text))
                        avails.sort()
                        consec = 1
                        for p in range(9,noOfseats,1):
                            if p in avails and (p+1) in avails and validSeats < numOfTickets and consec < numOfTickets :
                                consec = consec + 1
                            elif p in avails and not (p+1) in avails and consec > 1 and validSeats < numOfTickets:
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p-consec+1,p+1,1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1
                            elif p in avails and (p+1) in avails and validSeats < numOfTickets and consec == numOfTickets:
                                req = numOfTickets  - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p-consec+1,p+1,1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1



                        consec = 1 
                        for p in range(9,0,-1):
                            if (row.text + str(9)) in tobeclicked and (row.text + str(10)) in tobeclicked:
                                continue
                            if p in avails and (p-1) in avails and validSeats < numOfTickets and consec < numOfTickets :
                                consec = consec + 1
                            elif p in avails and not (p-1) in avails and consec > 1 and validSeats < numOfTickets:
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p+consec-1,p-1,-1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1
                            elif p in avails and (p-1) in avails and validSeats < numOfTickets and consec == numOfTickets :
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p+consec-1,p-1,-1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1
            if validSeats < numOfTickets:
                for row in rows:
                    if row.text == 'D' and validSeats < numOfTickets:
                        rowparent = row.find_element(By.XPATH,'..')
                        
                        availSeatsparent = rowparent.find_elements(By.CSS_SELECTOR, 'div.ng-star-inserted')
                        avails = []
                        for elem in availSeatsparent:
                            buttonfinder = elem.find_element(By.TAG_NAME, 'button').get_attribute('class')
                            if buttonfinder == 'seat-btn Available' or buttonfinder == 'seat-btn YourSeat':
                                avails.append(int(elem.text))
                        avails.sort()
                        consec = 1
                        for p in range(9,noOfseats,1):
                            if p in avails and (p+1) in avails and validSeats < numOfTickets and consec < numOfTickets :
                                consec = consec + 1
                            elif p in avails and not (p+1) in avails and consec > 1 and validSeats < numOfTickets:
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p-consec+1,p+1,1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1
                            elif p in avails and (p+1) in avails and validSeats < numOfTickets and consec == numOfTickets:
                                req = numOfTickets  - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p-consec+1,p+1,1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1



                        consec = 1 
                        for p in range(9,0,-1):
                            if (row.text + str(9)) in tobeclicked and (row.text + str(10)) in tobeclicked:
                                continue
                            if p in avails and (p-1) in avails and validSeats < numOfTickets and consec < numOfTickets :
                                consec = consec + 1
                            elif p in avails and not (p-1) in avails and consec > 1 and validSeats < numOfTickets:
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p+consec-1,p-1,-1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1
                            elif p in avails and (p-1) in avails and validSeats < numOfTickets and consec == numOfTickets :
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p+consec-1,p-1,-1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1
            if validSeats < numOfTickets:
                for row in rows:
                    if row.text == 'C' and validSeats < numOfTickets:
                        rowparent = row.find_element(By.XPATH,'..')
                        
                        availSeatsparent = rowparent.find_elements(By.CSS_SELECTOR, 'div.ng-star-inserted')
                        avails = []
                        for elem in availSeatsparent:
                            buttonfinder = elem.find_element(By.TAG_NAME, 'button').get_attribute('class')
                            if buttonfinder == 'seat-btn Available' or buttonfinder == 'seat-btn YourSeat':
                                avails.append(int(elem.text))
                        avails.sort()
                        consec = 1
                        for p in range(9,noOfseats,1):
                            if p in avails and (p+1) in avails and validSeats < numOfTickets and consec < numOfTickets:
                                consec = consec + 1
                            elif p in avails and not (p+1) in avails and consec > 1 and validSeats < numOfTickets:
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p-consec+1,p+1,1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1
                            elif p in avails and (p+1) in avails and validSeats < numOfTickets and consec == numOfTickets:
                                req = numOfTickets  - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p-consec+1,p+1,1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1



                        consec = 1 
                        for p in range(9,0,-1):
                            if (row.text + str(9)) in tobeclicked and (row.text + str(10)) in tobeclicked:
                                continue
                            if p in avails and (p-1) in avails and validSeats < numOfTickets and consec < numOfTickets :
                                consec = consec + 1
                            elif p in avails and not (p-1) in avails and consec > 1 and validSeats < numOfTickets:
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p+consec-1,p-1,-1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1
                            elif p in avails and (p-1) in avails and validSeats < numOfTickets and consec == numOfTickets :
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p+consec-1,p-1,-1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1
            print(tobeclicked)

# axaaaaxaa
            if len(tobeclicked) == (numOfTickets) :
                s = len(tobeclicked)
                for t in range(0, s - numOfTickets):
                    tobeclicked.pop()
                
                rowsdata = []
                rows = driver.find_elements(By.CSS_SELECTOR, 'span.seat-row-letter')
                for elem in rows:
                    rowsdata.append(elem.text)
                 
                while len(tobeclicked) != 0:
                    
                    indx = rowsdata.index((tobeclicked[0][0]))
                    rows = driver.find_elements(By.CSS_SELECTOR, 'span.seat-row-letter') 
                    rowparent = rows[indx].find_element(By.XPATH,'..')
                    availSeatsparent = rowparent.find_elements(By.CSS_SELECTOR, 'div.ng-star-inserted')

                    availSeatsparenttext = []
                    for elem1 in availSeatsparent:
                        availSeatsparenttext.append(elem1.text)

                    indx2 = availSeatsparenttext.index((tobeclicked[0][1::1]))   
                    buttonfinder = (WebDriverWait(availSeatsparent[indx2], 30).until(
                                            EC.presence_of_element_located((By.TAG_NAME, 'button')))).get_attribute('class')
                    
      
                    if buttonfinder == 'seat-btn Available' :
                        try:
                            availSeatsparent[indx2].click()
                            print('seat locked: ' + tobeclicked[0])
                        except:
                            print('seat lock fail: ' + tobeclicked[0])
                            time.sleep(0.2)
                        for itemss in range(1,len(tobeclicked),1):
                            tobeclicked[itemss - 1] = tobeclicked[itemss]
                        tobeclicked = tobeclicked[:-1]
                        time.sleep(2)


                    elif buttonfinder == 'seat-btn YourSeat' :
                        print('seat locked: ' + tobeclicked[0])
                        for itemss in range(1,len(tobeclicked),1):
                            tobeclicked[itemss - 1] = tobeclicked[itemss]
                        tobeclicked = tobeclicked[:-1]
                        time.sleep(1)
                       

            
            #rayaauayaya
                try:
                    booked = True
                    if (driver.find_element(By.XPATH,'/html/body/app-root/app-seat-layout/section/div/div[6]/div[3]/button[3]').is_enabled()):
                        buttonThich('/html/body/app-root/app-seat-layout/section/div/div[6]/div[3]/button[3]')
                        time.sleep(1)
                        buttonThich('/html/body/ngb-modal-window/div/div/app-confirmation-dialog/div[3]/button[2]')
                        time.sleep(1)
                        
                        for i in range(1,1000,1):
                            print('BOOKED THIS HOUR, PAY ASAP ' + temp,end = '\n\n')
                            discord_webhook.send_msg(movie_name = mainMovie, status="booked", datee = temp)
                            winsound.Beep(freq, duration)
                            time.sleep(5)
                        break
                    else:
                        time.sleep(2)
                        print("Buy Button Not Clickable")
                        driver.execute_script("window.history.go(-1)")
                        time.sleep(2)
                except:
                    time.sleep(2)
                    print("Buy Button Press Fail")
                    driver.execute_script("window.history.go(-1)")
                    time.sleep(2)
                
            else:
                print('This hour doesnot have enough valid seats: ' + temp,end = '\n\n')
                driver.execute_script("window.history.go(-1)")
                time.sleep(2)
        else:
            print('This hour is either SOLD OUT or EXPIRED: ' + datee + ' '  + str((schedules[l].text).replace('\n',' ')),end = '\n\n')

def mainvitrakomain2(nextCount):
    global numOfTickets
    schedules = []
    hall = driver.find_elements(By.CLASS_NAME,'show-hall-name')
    for k in hall:
        if k.text == hallName:
            parentOf = k.find_element(By.XPATH,'..') 
            schedules = parentOf.find_elements(By.TAG_NAME,'a')
    

            
    for l in range(0,(len(schedules)),1):
        time.sleep(2)
        header = driver.find_element(By.CLASS_NAME,'show-movies-header')
        datee = header.find_element(By.TAG_NAME,'span').text
        
        if datee == 'Today':
            datee = '[ '+ date.today().strftime("%B %d, %Y") + ' ]'
        elif datee == 'Tomorrow':
            datee = '[ '+ (date.today() + timedelta(days = 1)).strftime("%B %d, %Y") + ' ]'

        hall = driver.find_elements(By.CLASS_NAME,'show-hall-name')
        for k in hall:
            if k.text == hallName:
                parentOf = k.find_element(By.XPATH,'..') 
                schedules = parentOf.find_elements(By.TAG_NAME,'a')

        if schedules[l].get_attribute("class") != 'time-mark expired ng-star-inserted' and schedules[l].get_attribute("class") != 'time-mark soldout ng-star-inserted':
            temp = '[ ' + datee + ' ] ' + str((schedules[l].text).replace('\n',' '))
            schedules[l].click()
            validSeats = 0
            time.sleep(4)
            
            #raatattata
            rows = driver.find_elements(By.CSS_SELECTOR, 'span.seat-row-letter')
            tobeclicked = []

            for row in rows:
              
                if row.text == 'F' and validSeats < numOfTickets :
                    rowparent = row.find_element(By.XPATH,'..')
                   
                    
                    availSeatsparent = rowparent.find_elements(By.CSS_SELECTOR, 'div.ng-star-inserted')
                    noOfseats = len(availSeatsparent)
                    avails = []
                    for elem in availSeatsparent:
                        
                        buttonfinder = elem.find_element(By.TAG_NAME, 'button').get_attribute('class')
                       
                        if buttonfinder == 'seat-btn Available' or buttonfinder == 'seat-btn YourSeat':
                           
                            avails.append(int(elem.text))
                            
                    avails.sort()
                    consec = 1
                    for p in range(9,noOfseats,1):
                        if p in avails and (p+1) in avails and validSeats < numOfTickets and consec < numOfTickets:
                            consec = consec + 1
                        elif p in avails and not (p+1) in avails and consec > 1 and validSeats < numOfTickets:
                            req = numOfTickets  - validSeats
                            if consec >= req:
                                consec = req
                            validSeats = validSeats + consec
                            for m in range(p-consec+1,p+1,1):
                                tobeclicked.append(row.text + str(m))
                            consec = 1
                        elif p in avails and (p+1) in avails and validSeats < numOfTickets and consec == numOfTickets:
                            req = numOfTickets  - validSeats
                            if consec >= req:
                                consec = req
                            validSeats = validSeats + consec
                            for m in range(p-consec+1,p+1,1):
                                tobeclicked.append(row.text + str(m))
                            consec = 1



                    consec = 1 
                    for p in range(9,0,-1):
                        if (row.text + str(9)) in tobeclicked and (row.text + str(10)) in tobeclicked:
                            continue
                        if p in avails and (p-1) in avails and validSeats < numOfTickets and consec < numOfTickets:
                            consec = consec + 1
                        elif p in avails and not (p-1) in avails and consec > 1 and validSeats < numOfTickets:
                            req = numOfTickets - validSeats
                            if consec >= req:
                                consec = req
                            validSeats = validSeats + consec
                            for m in range(p+consec-1,p-1,-1):
                                tobeclicked.append(row.text + str(m))
                            consec = 1
                        elif p in avails and (p-1) in avails and validSeats < numOfTickets and consec == numOfTickets :
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p+consec-1,p-1,-1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1

                    
                    

            if(validSeats < numOfTickets):
                for row in rows:
                    if row.text == 'G' and validSeats < numOfTickets:
                        rowparent = row.find_element(By.XPATH,'..')
                        
                        availSeatsparent = rowparent.find_elements(By.CSS_SELECTOR, 'div.ng-star-inserted')
                        avails = []
                        for elem in availSeatsparent:
                            buttonfinder = elem.find_element(By.TAG_NAME, 'button').get_attribute('class')
                            if buttonfinder == 'seat-btn Available' or buttonfinder == 'seat-btn YourSeat':
                                avails.append(int(elem.text))
                        avails.sort()
                        consec = 1
                        for p in range(9,noOfseats,1):
                            if p in avails and (p+1) in avails and validSeats < numOfTickets and consec < numOfTickets:
                                consec = consec + 1
                            elif p in avails and not (p+1) in avails and consec > 1 and validSeats < numOfTickets:
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p-consec+1,p+1,1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1
                            elif p in avails and (p+1) in avails and validSeats < numOfTickets and consec == numOfTickets:
                                req = numOfTickets  - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p-consec+1,p+1,1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1



                        consec = 1 
                        for p in range(9,0,-1):
                            if (row.text + str(9)) in tobeclicked and (row.text + str(10)) in tobeclicked:
                                continue
                            if p in avails and (p-1) in avails and validSeats < numOfTickets and consec < numOfTickets:
                                consec = consec + 1
                            elif p in avails and not (p-1) in avails and consec > 1 and validSeats < numOfTickets:
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p+consec-1,p-1,-1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1
                            elif p in avails and (p-1) in avails and validSeats < numOfTickets and consec == numOfTickets :
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p+consec-1,p-1,-1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1

            if(validSeats < numOfTickets):
                for row in rows:
                    if row.text == 'H' and validSeats < numOfTickets:
                        rowparent = row.find_element(By.XPATH,'..')
                        
                        availSeatsparent = rowparent.find_elements(By.CSS_SELECTOR, 'div.ng-star-inserted')
                        avails = []
                        for elem in availSeatsparent:
                            buttonfinder = elem.find_element(By.TAG_NAME, 'button').get_attribute('class')
                            if buttonfinder == 'seat-btn Available' or buttonfinder == 'seat-btn YourSeat':
                                avails.append(int(elem.text))
                        avails.sort()
                        consec = 1
                        for p in range(9,noOfseats,1):
                            if p in avails and (p+1) in avails and validSeats < numOfTickets and consec < numOfTickets:
                                consec = consec + 1
                            elif p in avails and not (p+1) in avails and consec > 1 and validSeats < numOfTickets:
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p-consec+1,p+1,1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1
                            elif p in avails and (p+1) in avails and validSeats < numOfTickets and consec == numOfTickets:
                                req = numOfTickets  - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p-consec+1,p+1,1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1



                        consec = 1 
                        for p in range(9,0,-1):
                            if (row.text + str(9)) in tobeclicked and (row.text + str(10)) in tobeclicked:
                                continue
                            if p in avails and (p-1) in avails and validSeats < numOfTickets and consec < numOfTickets:
                                consec = consec + 1
                            elif p in avails and not (p-1) in avails and consec > 1 and validSeats < numOfTickets:
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p+consec-1,p-1,-1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1
                            elif p in avails and (p-1) in avails and validSeats < numOfTickets and consec == numOfTickets :
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p+consec-1,p-1,-1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1
            if validSeats < numOfTickets:
                for row in rows:
                    if row.text == 'D' and validSeats < numOfTickets:
                        rowparent = row.find_element(By.XPATH,'..')
                        
                        availSeatsparent = rowparent.find_elements(By.CSS_SELECTOR, 'div.ng-star-inserted')
                        avails = []
                        for elem in availSeatsparent:
                            buttonfinder = elem.find_element(By.TAG_NAME, 'button').get_attribute('class')
                            if buttonfinder == 'seat-btn Available' or buttonfinder == 'seat-btn YourSeat':
                                avails.append(int(elem.text))
                        avails.sort()
                        consec = 1
                        for p in range(9,noOfseats,1):
                            if p in avails and (p+1) in avails and validSeats < numOfTickets and consec < numOfTickets:
                                consec = consec + 1
                            elif p in avails and not (p+1) in avails and consec > 1 and validSeats < numOfTickets:
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p-consec+1,p+1,1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1
                            elif p in avails and (p+1) in avails and validSeats < numOfTickets and consec == numOfTickets:
                                req = numOfTickets  - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p-consec+1,p+1,1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1



                        consec = 1 
                        for p in range(9,0,-1):
                            if (row.text + str(9)) in tobeclicked and (row.text + str(10)) in tobeclicked:
                                continue
                            if p in avails and (p-1) in avails and validSeats < numOfTickets and consec < numOfTickets:
                                consec = consec + 1
                            elif p in avails and not (p-1) in avails and consec > 1 and validSeats < numOfTickets:
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p+consec-1,p-1,-1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1
                            elif p in avails and (p-1) in avails and validSeats < numOfTickets and consec == numOfTickets :
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p+consec-1,p-1,-1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1
            if validSeats < numOfTickets:
                for row in rows:
                    if row.text == 'C' and validSeats < numOfTickets:
                        rowparent = row.find_element(By.XPATH,'..')
                        
                        availSeatsparent = rowparent.find_elements(By.CSS_SELECTOR, 'div.ng-star-inserted')
                        avails = []
                        for elem in availSeatsparent:
                            buttonfinder = elem.find_element(By.TAG_NAME, 'button').get_attribute('class')
                            if buttonfinder == 'seat-btn Available' or buttonfinder == 'seat-btn YourSeat':
                                avails.append(int(elem.text))
                        avails.sort()
                        consec = 1
                        for p in range(9,noOfseats,1):
                            if p in avails and (p+1) in avails and validSeats < numOfTickets and consec < numOfTickets :
                                consec = consec + 1
                            elif p in avails and not (p+1) in avails and consec > 1 and validSeats < numOfTickets:
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p-consec+1,p+1,1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1
                            elif p in avails and (p+1) in avails and validSeats < numOfTickets and consec == numOfTickets:
                                req = numOfTickets  - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p-consec+1,p+1,1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1



                        consec = 1 
                        for p in range(9,0,-1):
                            if (row.text + str(9)) in tobeclicked and (row.text + str(10)) in tobeclicked:
                                continue
                            if p in avails and (p-1) in avails and validSeats < numOfTickets and consec < numOfTickets :
                                consec = consec + 1
                            elif p in avails and not (p-1) in avails and consec > 1 and validSeats < numOfTickets:
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p+consec-1,p-1,-1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1
                            elif p in avails and (p-1) in avails and validSeats < numOfTickets and consec == numOfTickets :
                                req = numOfTickets - validSeats
                                if consec >= req:
                                    consec = req
                                validSeats = validSeats + consec
                                for m in range(p+consec-1,p-1,-1):
                                    tobeclicked.append(row.text + str(m))
                                consec = 1
            print(tobeclicked)
# axaaaaxaa
            if len(tobeclicked) == (numOfTickets) :
                s = len(tobeclicked)
                for t in range(0, s - numOfTickets):
                    tobeclicked.pop()
                
                rowsdata = []
                rows = driver.find_elements(By.CSS_SELECTOR, 'span.seat-row-letter')
                for elem in rows:
                    rowsdata.append(elem.text)
                 
                while len(tobeclicked) != 0:
                    
                    indx = rowsdata.index((tobeclicked[0][0]))
                    rows = driver.find_elements(By.CSS_SELECTOR, 'span.seat-row-letter') 
                    rowparent = rows[indx].find_element(By.XPATH,'..')
                    availSeatsparent = rowparent.find_elements(By.CSS_SELECTOR, 'div.ng-star-inserted')

                    availSeatsparenttext = []
                    for elem1 in availSeatsparent:
                        availSeatsparenttext.append(elem1.text)

                    indx2 = availSeatsparenttext.index((tobeclicked[0][1::1]))    
                    buttonfinder = (WebDriverWait(availSeatsparent[indx2], 30).until(
                                            EC.presence_of_element_located((By.TAG_NAME, 'button')))).get_attribute('class')
                    
      
                    if buttonfinder == 'seat-btn Available' :
                        try:
                            availSeatsparent[indx2].click()
                            print('seat locked: ' + tobeclicked[0])
                        except:
                            print('seat lock fail: ' + tobeclicked[0])
                            time.sleep(0.2)
                        for itemss in range(1,len(tobeclicked),1):
                            tobeclicked[itemss - 1] = tobeclicked[itemss]
                        tobeclicked = tobeclicked[:-1]
                        time.sleep(2)


                    elif buttonfinder == 'seat-btn YourSeat' :
                        print('seat locked: ' + tobeclicked[0])
                        for itemss in range(1,len(tobeclicked),1):
                            tobeclicked[itemss - 1] = tobeclicked[itemss]
                        tobeclicked = tobeclicked[:-1]
                        time.sleep(1)

   
            
            #rayaauayaya
 
     
            
            
                try:
                    booked = True
                    if (driver.find_element(By.XPATH,'/html/body/app-root/app-seat-layout/section/div/div[6]/div[3]/button[3]').is_enabled()):
                        buttonThich('/html/body/app-root/app-seat-layout/section/div/div[6]/div[3]/button[3]')
                        time.sleep(1)
                        buttonThich('/html/body/ngb-modal-window/div/div/app-confirmation-dialog/div[3]/button[2]')
                        time.sleep(1)
                        
                        for i in range(1,1000,1):
                            print('BOOKED THIS HOUR, PAY ASAP ' + ' ** ' + temp + ' ** ',end = '\n\n')
                            discord_webhook.send_msg(movie_name = mainMovie, status="booked", datee = temp)
                            winsound.Beep(freq, duration)
                            time.sleep(5)
                        break
                    else:
                        time.sleep(2)
                        print("Buy Button Not Clickable")
                        driver.execute_script("window.history.go(-1)")
                        time.sleep(2)
                        for m in range(0,nextCount,1):
                            buttonThich('/html/body/app-root/app-show/section/div/div[2]/div/div[1]/button[2]')
                            time.sleep(2)
                except:
                    time.sleep(2)
                    print("Buy Button Press Fail")
                    driver.execute_script("window.history.go(-1)")
                    time.sleep(2)
                    for m in range(0,nextCount,1):
                        buttonThich('/html/body/app-root/app-show/section/div/div[2]/div/div[1]/button[2]')
                        time.sleep(2)
                
            else:
                print('This hour doesnot have enough valid seats: ' + temp,end = '\n\n')
                driver.execute_script("window.history.go(-1)")
                time.sleep(2)
                for m in range(0,nextCount,1):
                    buttonThich('/html/body/app-root/app-show/section/div/div[2]/div/div[1]/button[2]')
                    time.sleep(2)
        else:
            print('This hour is either SOLD OUT or EXPIRED: ' + datee + ' '  + str((schedules[l].text).replace('\n',' ')),end = '\n\n')



def login():
    try:
                driver.find_element(By.XPATH,'/html/body/app-root/app-login/section/div/div/form/div[1]/input').send_keys("9841394852")
                time.sleep(0.5)
                driver.find_element(By.XPATH,'/html/body/app-root/app-login/section/div/div/form/div[2]/input').send_keys("1331voker")
                time.sleep(0.5)
                buttonThich('/html/body/app-root/app-login/section/div/div/form/div[3]/button')
                time.sleep(1)
    except:
        time.sleep(1)

def mainFunc(movieBanner):
    booked = False
    nextCount = 1
    try:
        movieBanner.click()
        #buy ticket xpath
        # buttonThich(ticketXpath)
        time.sleep(2)
        print('--' + ((date.today()).strftime("%B %d, %Y")).upper() + '--',end = ('\n\n'))
        mainvitrakomain()
        time.sleep(2)
        buttonThich('/html/body/app-root/app-show/section/div/div[2]/div/div[1]/button[2]')
        time.sleep(2)

                

        while booked == False and nextCount < 4:
            print('--' + ((date.today() + timedelta(days = nextCount)).strftime("%B %d, %Y")).upper()+ '--',end = ('\n\n'))   
            mainvitrakomain2(nextCount)
            nextCount = nextCount + 1
            buttonThich('/html/body/app-root/app-show/section/div/div[2]/div/div[1]/button[2]')
            if nextCount == 4:
                discord_webhook.send_msg(movie_name = mainMovie, status="not-available", datee = '')
            time.sleep(2)

        
        
       



       
        


                


    except:
        time.sleep(0.2)
       




        


        # #right or left arrow
        
        # #time xpath (bkt bhatbhateni)
        # time.sleep(2)
        # buttonThich('/html/body/app-root/app-show/section/div/div[2]/div/div[2]/div/a')
        # time.sleep(2)


    















def buttonCleeker(abcde):
    try:
        abcde.click()
    except:
        time.sleep(0.2)

def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH,xpath)

    except NoSuchElementException:
        return False
    return True

def buttonThich(xpath):
    try:
        if(check_exists_by_xpath(xpath)):
            (driver.find_element(By.XPATH,xpath)).click()
        else:
            time.sleep(4)
            (driver.find_element(By.XPATH,xpath)).click()
            
    except:
        time.sleep(0.5)



try:
    time.sleep(4)
    login()
    time.sleep(2)
    try:
        modale = (WebDriverWait(driver, 8).until(
                                            EC.presence_of_element_located((By.XPATH, '/html/body/ngb-modal-window/div/div/app-popup-notice/section/button'))))
        modale.click()
        time.sleep(2)
    except:
        time.sleep(0.2)
except:
    time.sleep(0.5)

while True:
    try:
        modale = (WebDriverWait(driver, 8).until(
                                            EC.presence_of_element_located((By.XPATH, '/html/body/ngb-modal-window/div/div/app-popup-notice/section/button'))))
        modale.click()
        time.sleep(2)
    except:
        time.sleep(0.2)
    try:
        time.sleep(2)
        nowshowing = driver.find_element(By.XPATH,'/html/body/app-root/app-home/app-now-showing/section')
        comingsoon = driver.find_element(By.XPATH,'/html/body/app-root/app-home/app-coming-soon/section')
        time.sleep(1)
        movieList = nowshowing.find_elements(By.CLASS_NAME,"movie-poster-title")
        comingSoonList = comingsoon.find_elements(By.CLASS_NAME,"movie-poster-title")
        for movieBanner in movieList:
            if ((movieBanner.text).split('\n')[0]) == mainMovie:
                winsound.Beep(500, 2000)
                print("Movie Found At NOW SHOWING Tab Civil mall",end = '\n\n')
                foundOnNS = True
                for x in range(0,5,1):
                    time.sleep(0.5)
                    try:
                        discord_webhook.send_msg(movie_name = mainMovie, status="available", datee = '')
                    except:
                        time.sleep(0.2)
                    time.sleep(2)
                mainFunc(movieBanner)
        for movieOnComingSoon in comingSoonList:
            if ((movieOnComingSoon.text).split('\n')[0]) == mainMovie:
                # winsound.Beep(550, 1000)
                print("Movie Is On COMING SOON Tab Civil mall",end = '\n\n')
                foundOnCS = True
                if (delayy % 50) == 0:
                    delayy = 1
                delayy = delayy + 1    
                time.sleep(5)
                driver.refresh()
                time.sleep(4)
            try:
                driver.find_element(By.XPATH, '/html/body/ngb-modal-window/div/div/app-popup-notice/section/button').click()
                time.sleep(2)
            except:
                time.sleep(0.2)

        if not foundOnNS and not foundOnCS:
            print("Movie Not Available Yet",end = '\n\n')
            time.sleep(8)
            driver.refresh()
            time.sleep(4)
            try:
                driver.find_element(By.XPATH, '/html/body/ngb-modal-window/div/div/app-popup-notice/section/button').click()
                time.sleep(2)
            except:
                time.sleep(0.2)
                    



        
        
                
            
            
            
            
    except:

        time.sleep(5)
        driver.refresh()




