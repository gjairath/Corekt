"""
Created on Mon Feb  1 03:31:29 2021

@author: garvi

Filename: Main.py
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import process_data as pd
import gui_utility as gui
import sys
import booking_utility as bu
import time

import graph_utility as gu


if __name__ == "__main__":

    is_fast = False
    if (len(sys.argv) >= 2):
        if (sys.argv[1] == "-f"):
            is_fast = True
    
    #Debugging
    is_fast = True
    data = pd.ProcessData(is_fast)
    
    is_true = True

    if (is_fast == False):
        print ("\n\n\nNote:\n\tThe Corec decided to replace \
                    \n\t0 spots available with No spots available. [You cannot spam book requests for 0 spots] \
                    \n\t\tI.e, they spotted bots on their website (I wonder who has the time to make bots...) \
                    \n\tHowever, this doesn't change anything infact makes my project even more useful.\n\n\n")
        
        print ("\n\n\n\n\t=== Corekt === ")
        print ("\t\t A fuck you to all jocks world-wide.\n\nIf you want to use the faster alt, -f argv")
        
    while (is_true):
        

        if (is_fast == True):
            print (" Try: book 6:00 pm Monday or if you're really lazy: b 6 P M [Please space input]\n Try: cancel or cancel all or c all or c show\n Try: automate or a or A [really fucking cool]")
            ud = input("\n\nput: ")
            
            if (ud[0] == 'b' or ud[0] == 'B'):
                
                
                data.parsed.driver.get("https://recwell.purdue.edu/booking/83456ef4-1d99-4e58-8e66-eb049941f7c1")
                
                time.sleep(2)
                    
                id_t = "divBookingDateSelector"
                
                
                day_header = WebDriverWait(data.parsed.driver, 20).until(
                                EC.presence_of_element_located((By.ID, id_t)))
    
                
                day_to_click = day_header.find_element_by_xpath("//*[@id='divBookingDateSelector']/div[2]/div[2]")
                days = day_to_click.find_elements_by_tag_name("button")
                
                choice = 0
                
                day_array = data.days
                for item in day_array:
                    if (item.isnumeric()):
                        day_array.remove(item)
                print("These are the days: {}".format(day_array))
                
                for idx, item in enumerate(day_array):
                    # If nothing went wrong the third input is the time?
                    if (item[0].lower() == ud.split(" ")[3][0].lower()):
                        choice = idx
                
                print ("\nNavigating to...  {}".format(day_array[(choice)]))
                days[int(choice)].click()
                
                
                          
                time.sleep(2)
        
                if (choice != 1): data.refetch_data_time()
                
                #displays the time slots.
                times, isBooked = data.processing_data() 
    
                if (isBooked):
                    print ("You've already booked on this day, cancel and try again OR the day is over there are no spots left.\n\n")
                    
                else:
                    bu.book(data, False, times, is_fast, ud)
                    
            elif (ud[0] == 'C' or ud[0] == 'c'):
                bu.cancel(data)


            
            
        else:     
            
            user_decision = input("\n[[1] Book | [2] Cancel/View | [3] Concurrent-Booking \
                                        \n[4] Auto-Book The Least Spot | [5] Show Fancy Stats For Fun \
                                        \n[6] Give Feedback. | [7] Quit] \
                                         \n\nEnter Your Choice Here:")
                                     
            
            if (user_decision == "1" or user_decision == "3"):
                
                data.parsed.driver.get("https://recwell.purdue.edu/booking/83456ef4-1d99-4e58-8e66-eb049941f7c1")
                
    
                time.sleep(2)
                days = data.show_days()
                
                choice = input("\n\nWhat Day? Enter numerically [1,2,3]. \n q to quit: ")    
                
                if (choice == ""): choice = "1"
                
                if (choice == "q" or choice == "Q"): 
                    is_true = False
                    print ("Exiting...")
                    exit()
                    
                id_t = "divBookingDateSelector"
                
                
                day_header = WebDriverWait(data.parsed.driver, 20).until(
                                EC.presence_of_element_located((By.ID, id_t)))
    
                
                day_to_click = day_header.find_element_by_xpath("//*[@id='divBookingDateSelector']/div[2]/div[2]")
                days = day_to_click.find_elements_by_tag_name("button")
    
                
                days[int(choice) - 1].click()
            
            # TODO
            
                time.sleep(2)
        
                if (choice != 1): data.refetch_data_time()
                
                #displays the time slots.
                times, isBooked = data.processing_data() 
    
    
                gui.prettify(times, days[int(choice) - 1].text.split("\n")[1], choice)
                
                show_all = input("===============\n\n See all options? [Yes|No (Go Back)|Book]: ")
                if (show_all == "Yes"): 
                    for idx in range(len(times)):
                        print("[" + str(idx + 1) + "] " + times[idx][0] + "\t\t\t" + times[idx][1])
                    
                    if (isBooked):
                        print ("You've already booked on this day, cancel and try again.")
                    
                    else:
                        bu.book(data, False, times)
                        
                if (show_all == "Book" or show_all == "book" or show_all == "b" or show_all == "B"):
                    
                    if (isBooked):
                        print ("You've already booked on this day, cancel and try again.")
                    else:    
                        isConcurrent = False
                        if (user_decision == "3"): isConcurrent = True
                        bu.book(data, isConcurrent, times)
            
            elif (user_decision == "2"):
                bu.cancel(data)
                
            
            elif (user_decision == "4"):
                data.parsed.driver.get("https://recwell.purdue.edu/booking/83456ef4-1d99-4e58-8e66-eb049941f7c1")
            
                time.sleep(2)
                days = data.show_days()
                
                choice = input("\n\nWhat Day? Enter numerically [1,2,3]. \n q to quit: ")    
                
                if (choice == ""): choice = "1"
                
                if (choice == "q" or choice == "Q"): 
                    is_true = False
                    print ("Exiting...")
                    exit()
                    
                time.sleep(2)
                id_t = "divBookingDateSelector"
                
                
                day_header = WebDriverWait(data.parsed.driver, 20).until(
                                EC.presence_of_element_located((By.ID, id_t)))
    
                
                day_to_click = day_header.find_element_by_xpath("//*[@id='divBookingDateSelector']/div[2]/div[2]")
                days = day_to_click.find_elements_by_tag_name("button")
    
                
                days[int(choice) - 1].click()
            
                
                if (choice != 1): data.refetch_data_time()
                
                #displays the time slots.
                times, isBooked = data.processing_data() 
                
                
                
                all_spots = list()
                for item in times:
                    if (item[1][0] == 'N'): continue
                    spots = int(item[1][0])
                    all_spots.append(spots)
                    
                # super rare case when literally every booking has the same number of slots.
                    #  On one sunday it was 90 for all of them, the min catch fails.
                uncaught_exception = False
                try: desired_val = min(i for i in all_spots if i > 0)
                except: uncaught_exception = True
                
                if (uncaught_exception == True):
                    desired_idx = 0
                else:
                    desired_idx = all_spots.index(desired_val)
                
                print ("Trying to book spot {} with availability {}"
                       .format(times[desired_idx][0], times[desired_idx][1]))
                
                notBooked = True
                while (notBooked):
                    try:    
                        class_book = data.parsed.driver.find_element_by_class_name("container-flex")
                        booking_card = class_book.find_element_by_xpath("(//*[@class='booking-slot-item'])[%d]" % int(desired_idx + 1))
                        booking = booking_card.find_element_by_tag_name("button")
                        booking.click()
                        
                        notBooked = False
                        
                    except:
                        #I dont know. Just sleep and hope it works out lol.
                        time.sleep(0.25)
                        print(".", end = "")
                    
                
                print ("\nSuccess. Cancel it on your time.")
                
                
            elif (user_decision == "5"):
                
                print("\n\nLoading...")
                gu.get_all_bookings(data)
                
            
            elif (user_decision == "6"):
                print ("\nDo you like this software?\n[1] Yes [2] No")
                his_reply = input("Enter [1] or [2]: ")
                
                if (his_reply == "1"):
                    print ("\n Your response has been recorded.")
                    
                else:
                    print ("\n You answered: Yes. Your response has been recorded.")
                
    
                        
            elif (user_decision == "7"):
                exit()
                
            else:
                print ("\n\nEnter what the menu says dummy.\n\n")