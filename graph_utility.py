# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 23:55:50 2021

@author: garvi
"""

import time
    
import sys

def first_graph(days, name):
    '''
    Parameters
    ----------
    days: array of days.
    name: users name.
    
    Returns
    -------
    None.

    '''

    #Lazy import
    import pandas as pd
    import matplotlib.pyplot as plt

    l = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    df = pd.DataFrame({'freq': days})
    
    
    df.groupby('freq', as_index=True).size().sort_values().plot(kind='bar', orientation='vertical')
    
    plt.xticks(rotation='horizontal')
    plt.xlabel("The Days")
    plt.ylabel("Frequency/Number of Days")
    plt.title("Frequency of Days Showed for {}".format(name))
    plt.tight_layout()

    plt.show()


def second_graph(days, name):
    '''
    Parameters
    ----------
    days: array of days.
    name: users name.
    
    Returns
    -------
    None.

    '''
    import pandas as pd
    import matplotlib.pyplot as plt

    # Graph of a pie chart showing what days the bookings were mostly booked.
    l = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    df = pd.DataFrame({'freq': days})

    explode=(0.12, 0.12, 0.12, 0.12, 0.12, 0.12)
    df.value_counts().plot(kind='pie', labels = l, title = "Pie Chart for Days Booked {}".format(name), \
                          shadow = True, autopct='%1.1f%%', ylabel = "", explode = explode, pctdistance=0.65)
    plt.tight_layout()        
    plt.show()
    
    
def third_graph(dates, name):
    '''
    Parameters
    ----------
    dates: array of dates that the user booked.
    name: users name.
    
    Returns
    -------
    A graph with freq of days.

    '''
    import pandas as pd
    import matplotlib.pyplot as plt

    # Graph to show a bar plot of the dates the reserations were booked.
    df = pd.DataFrame({'freq': dates})
    
    df.groupby('freq', as_index=True).size().sort_values().plot(kind='bar', orientation='vertical')
    
    plt.xlabel("The Days")
    plt.ylabel("Frequency/Number of Days")
    plt.title("Frequency of Days Showed for {}".format(name))
    plt.tight_layout()
    
    plt.show()
    
    
def fourth_graph(dates, name):
    # Graph to show a scatter plot of the dates it was mostly booked.
    
    import seaborn as sns
    from collections import Counter
    import pandas as pd
    import matplotlib.pyplot as plt

    counter = Counter(dates)
    df_new = pd.DataFrame.from_dict(counter, orient='index').reset_index()
    
    
    g = sns.scatterplot(x = 'index', y = 0, data = df_new)
    g.set_xticklabels(rotation=90, labels = df_new['index'])
    plt.tight_layout()
    
    plt.show()
    
    
def fifth_graph(am_pm, name):
    '''
    Parameters
    ----------
    am_pm: array of am/pm frequencies.
    name: users name.
    
    Returns
    -------
    None.

    '''
    import matplotlib.pyplot as plt

    # Graph to show the pie chart of when the person books for showing up, AM/PMs.
    am = 0
    pm = 0
    
    for elem in am_pm:
        
        # If you have something at AM/PM both, like 11AM-12PM its irrelevant lets just call that a border case.
        # And let it exist as whatever.
        
        if (elem.find("AM") == -1):
            pm +=1
        
        if (elem.find("PM") == -1):
            am += 1
            
    data = [am, pm]
    labels = ['AM', 'PM']
    explode = (0.1, 0.1)
    plt.pie(data, labels = labels, shadow = True, autopct='%1.1f%%', explode = explode, pctdistance=0.65)
    plt.title("Percentage of AM/PMs booked for {}".format(name))
    plt.tight_layout()
    plt.show() 

def make_graphs_bookings(days, dates_and_times, name, am_pm, tot_arr):

    '''
    Args.
        Days: The days to show up.
        Dates: The date to show up.
        
        Date_registered: <>
            
        tot_arr: THe array with all bookings include no shows and cancellations.
    
    Returns
        The graphs lol
    '''
        

    # Lazy import.
    
    isTrue = True
    
    while(isTrue):
        graph_choice = input("Choices: \n[1]. Bar plot of Days you book. \
                                       \n[2]. Pie chart of Days you book \
                                        \n[3]. Barplot for Dates you booked for. \
                                        \n[4]. Piechart for dates you booke for. \
                                        \n[5]. Pie chart for time usually booked - mornings or night. \
                                        \n[6]. Quit \n\n Enter Here: ")
    
    
        if (graph_choice == "1"): first_graph(days, name)
        elif (graph_choice == "2"): second_graph(days, name)    
        elif (graph_choice == "3"): third_graph(dates_and_times, name)
    
        elif (graph_choice == "4"): fourth_graph(dates_and_times, name)
        
        elif (graph_choice == "5"): fifth_graph(am_pm, name)
    
        else: 
            isTrue = False
            break
        
    return

def get_all_bookings(data, is_name = False):
    '''
    Parameters
    ----------
    data: class object, session tracker
    
    Returns
    -------
    total_array, containg all relevant data

    '''
    # Program to fidn total bookings.
    data.parsed.driver.get("https://recwell.purdue.edu/MemberDetails#Reg")
    data.parsed.driver.get("https://recwell.purdue.edu/MemberDetails#Reg")
    
    
    
    
    # either the page is fucked or something with the pages array, it works in GDB.

    
    print("\nLoading...")
    time.sleep(2)
    
    lower_scroll = data.parsed.driver.find_elements_by_tag_name("tfoot")
    try:
        pages = lower_scroll[0].find_elements_by_tag_name("a")
    except:
        print ("something went wrong. You might not have adequate data to show. Fitness is not a bad idea, you know.")
        return 
    # IF a user has 10 pages worth of bookigns, 10 pages + 1 for the forward button.
    # ARrays start at 0 ahhaha good joke memes programming humor. 
    
    total_array = []
    counter_loop = 0
    
    print("Navigating your pages...")
    for i in range(len(pages)):       
        time.sleep(3)
        lower_scroll = data.parsed.driver.find_elements_by_tag_name("tfoot")
        pages = lower_scroll[0].find_elements_by_tag_name("a")
    
        string = data.parsed.driver.find_element_by_id("content_Reg").text    
        find = string.find("CoRec Access")    
        new_string = string[find:] # The relevant data, with trash filtered out.
        
        # Either the booking is paid or cancelled.
        # Thus, just split it at that point.
        
        new_string = new_string.replace("\nCancelled", "\nPaid")
        arr = new_string.split("\nPaid")
        
        if (arr[len(arr) - 1] == ""):
            del arr[len(arr) - 1]
        
        total_array.extend(arr)
        
        isClick = True
        while(isClick and i != len(pages) - 1 and counter_loop <= len(pages)):
            try:
                pages[counter_loop].click()
                if (i == 0): counter_loop += 1
                isClick = False
                
            except:
                time.sleep(0.25)
                print ("\nLoading...")
                
        counter_loop += 1
        print ("At page: {}".format(counter_loop))
    
    print ("Done")

    days_frequently_booked = []
    date_time_array = []
    
    am_pm_instances = []
    
    print ("Processing your data...\n\n")
    name = total_array[1].split(" ")[0]    


    for idx, sub_rows in enumerate(total_array):

        length = sub_rows.find("Reservation:") + 13
        total_array[idx] = sub_rows[length:]
        
        splits = total_array[idx].split("n/a")
        
        
        # THis is done on purpose btw im really smart i would like to say.
        day_booked = splits[0]
        day = day_booked.split(" ")[0]
        
        # For some reason the website acts up with a sunday.
        if (day == "unday"): day = "Sunday"
        days_frequently_booked.append(day)
                
        lf = day_booked.split(",")[1].split(" ")[1:4]
        joiner = " "
        
        lf2 = day_booked.split(",")[1].split(" ")[4:]

        date_time_array.append(joiner.join(lf))
        
        am_pm_instances.append(joiner.join(lf2))
    

    
    print ("Done\n\n")
    return_array = [days_frequently_booked, date_time_array, name, am_pm_instances, total_array]
    if (is_name == True):
        return return_array
    make_graphs_bookings(days_frequently_booked, date_time_array, name, am_pm_instances, total_array)
    return total_array                
