#  File: ERsim.py
#  Description: program that reads html file with instructions for adding and removing patients from their respective queues as they are treated  
#
#  Date Created: 10-15-17
#  Date Last Modified:10-18-17


class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        for i in self.items:
            return 



def main():

    myfile = open('ERsim.txt') 
    tasks = myfile.readlines() # reads html file line by line and puts into a list
    myfile.close()

    fairQ = Queue()
    seriousQ = Queue()
    criticalQ = Queue()

    tasklist = []
    for i in tasks: # creates list of tasks for program
        i = i[:-1]
        tasklist.append(i)
    
    for i in tasklist:
        if i[0:3] == "add": # if keyword is "add", evaluate next keyword for adding patients to queues, print command and queues
            if i[4:8] == "Fair":
                fairQ.enqueue(i[9:])
                print("Command: add patient", i[9:], "to Fair queue.\n")
                print("\tQueues are:")
                print("\tFair:", fairQ.items)
                print("\tSerious:", seriousQ.items)
                print("\tCritical:", criticalQ.items,"\n")
            elif i[4:12] == "Critical":
                criticalQ.enqueue(i[13:])
                print("Command: add patient", i[13:], "to Critical queue.\n")
                print("\tQueues are:")
                print("\tFair:", fairQ.items)
                print("\tSerious:", seriousQ.items)
                print("\tCritical:", criticalQ.items,"\n")
            else:
                seriousQ.enqueue(i[12:])
                print("Command: add patient", i[12:], "to Serious queue.\n")
                print("\tQueues are:")
                print("\tFair:", fairQ.items)
                print("\tSerious:", seriousQ.items)
                print("\tCritical:", criticalQ.items,"\n")
                
        elif i[0:5] == "treat": # if keyword is "treat", evaluate next keyword and remove next patient, next patient in appropriate queue, or all patients, print the command and queues
            if i[6:] == "next":
                if criticalQ.size() > 0:
                    print("Command: Treat next patient\n")
                    print("\tTreating", criticalQ.dequeue(), "from Critical queue")
                    print("\tQueues are:")
                    print("\tFair:", fairQ.items)
                    print("\tSerious:", seriousQ.items)
                    print("\tCritical:", criticalQ.items,"\n")
                elif seriousQ.size() > 0:
                    print("Command: Treat next patient\n")
                    print("\tTreating", seriousQ.dequeue(), "from Serious queue")
                    print("\tQueues are:")
                    print("\tFair:", fairQ.items)
                    print("\tSerious:", seriousQ.items)
                    print("\tCritical:", criticalQ.items,"\n")
                elif fairQ.size() > 0:
                    print("Command: Treat next patient\n")
                    print("\tTreating", fairQ.dequeue(), "from Fair queue")
                    print("\tQueues are:")
                    print("\tFair:", fairQ.items)
                    print("\tSerious:", seriousQ.items)
                    print("\tCritical:", criticalQ.items,"\n")
                else:
                    print("Command: Treat next patient\n")
                    print("\tNo patients in queues\n")
                    
            elif i[6:] == "Fair": 
                if fairQ.size() >0:
                    print("Command: Treat next patient on Fair queue\n")
                    print("\tTreating", fairQ.dequeue(), "from Fair queue")
                    print("\tQueues are:")
                    print("\tFair:", fairQ.items)
                    print("\tSerious:", seriousQ.items)
                    print("\tCritical:", criticalQ.items,"\n")
                else:
                    print("Command: Treat next patient on Fair queue\n")
                    print("\tNo patients in queue\n")
            elif i[6:] == "Serious":
                if seriousQ.size() > 0:
                    print("Command: Treat next patient on Serious queue\n")
                    print("\tTreating", seriousQ.dequeue(), "from Serious queue")
                    print("\tQueues are:")
                    print("\tFair:", fairQ.items)
                    print("\tSerious:", seriousQ.items)
                    print("\tCritical:", criticalQ.items,"\n")
                else:
                    print("Command: Treat next patient on Serious queue\n")
                    print("\tNo patients in queue\n")
            elif i[6:] == "Critical":
                if criticalQ.size() > 0:
                    print("Command: Treat next patient on Critical queue\n")
                    print("\tTreating", critical.dequeue(), "from Critical queue")
                    print("\tQueues are:")
                    print("\tFair:", fairQ.items)
                    print("\tSerious:", seriousQ.items)
                    print("\tCritical:", criticalQ.items,"\n")
                else:
                    print("Command: Treat next patient on Critical queue\n")
                    print("\tNo patients in queue","\n")
                    
            elif i[6:] == "all":
                print("Command: Treat all patients\n")
                while criticalQ.size() > 0:
                    print("\tTreating", criticalQ.dequeue(), "from Critical queue")
                    print("\tQueues are:")
                    print("\tFair:", fairQ.items)
                    print("\tSerious:", seriousQ.items)
                    print("\tCritical:", criticalQ.items,"\n")
                while seriousQ.size() > 0:
                    print("\tTreating", seriousQ.dequeue(), "from Serious queue")
                    print("\tQueues are:")
                    print("\tFair:", fairQ.items)
                    print("\tSerious:", seriousQ.items)
                    print("\tCritical:", criticalQ.items,"\n")
                while fairQ.size() > 0:
                    print("\tTreating", fairQ.dequeue(), "from Fair queue")
                    print("\tQueues are:")
                    print("\tFair:", fairQ.items)
                    print("\tSerious:", seriousQ.items)
                    print("\tCritical:", criticalQ.items,"\n")
                
                print("\tNo patients in queues\n")
                
        else: # if none of the other conditions fulfilled, exit
            print("Command: Exit\n")
                
main()
