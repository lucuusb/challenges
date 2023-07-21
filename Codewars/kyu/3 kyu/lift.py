class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.capacity = capacity
        self.queues = queues
       
    def theLift(self):
        c = self.capacity
        queues = list(self.queues)
        queue = []
        lift = []
        order = [0]
        while any(queues):

            #Lift goes up
            for floor, tuple_ in enumerate(queues):

                #Exiting logic
                if floor in lift:
                    lift = list(filter(lambda p: p != floor,lift))
                    order.append(floor)
                    """obsolete patch--
                    boarded = len(lift)
                    lift = list(filter(lambda p: p != floor,lift))
                    #lift = [q for q in lift if q != floor]              
                    if len(lift) < boarded: #At least one person got off
                        order.append(floor)
                    elif len(lift) == c: #No one got off
                        continue
                    -------------------
                    """

                #Optimization logic
                
                #Boarding logic    
                if not tuple_ or max(tuple_) < floor or len(lift) == c:
                    continue #no one here can enter now   
                for person in tuple_:
                    if person > floor and len(lift) < c:
                        lift.append(person)
                    else:
                        queue.append(person)

                """obsolete boarding logic--
                #Boarding logic
                obsolete patch--
                queue = sorted(list(tuple_))
                boarding = c - len(lift)
                lift += queue[:boarding]
                del queue[:boarding]
                queues[floor] = tuple(queue)
                -------------------
                
                
                lift += boarding
                boarding.clear()
                obsolete patch--
                #People enter the lift
                for enter, person in enumerate(queue):
                    if person > floor:
                        if len(lift) < c:
                            lift.append(person)
                            queue[enter] = 'e'
                        else:
                            break
                queue = [p for p in queue if p != 'e']
                --------------
                """
                queues[floor] = tuple(queue)
                queue.clear()

                if order[-1] != floor:
                    order.append(floor)
    
            #Lift goes down
            for tuple_ in reversed(queues):

                if floor in lift:
                    lift = list(filter(lambda p: p != floor,lift))
                    order.append(floor)
    
                if not tuple_ or min(tuple_) > floor or len(lift) == c:
                    floor -= 1
                    continue

                for person in tuple_:
                    if person < floor and len(lift) < c:
                        lift.append(person)
                    else:
                        queue.append(person)

                queues[floor] = tuple(queue)
                queue.clear()

                if order[-1] != floor:
                    order.append(floor)
                floor -= 1
  
        #Lift stops
        if order[-1] != 0:
            order.append(0)
        return order

#99% yoyo passed
# Floors:    G(0)   1      2     3     4       5      6         Answers:
tests = [[ ( (),   (),    (4,4,4,), (),   (2,2,2,),    (),    () ),      [0, 2, 4, 2, 4, 2, 0]          ],
         [ ( (),   (),    (5,5,5,),   (),   (),    (),    () ),    [0, 2, 1, 0]          ],
         [ ( (),   (3,),  (4,),    (),   (5,),  (),    () ),     [0, 1, 2, 3, 4, 5, 0] ],
         [ ( (),   (0,),  (),      (),   (2,),  (3,),  () ),     [0, 5, 4, 3, 2, 1, 0] ]]
  
for queues, answer in tests:
    lift = Dinglemouse(queues, 5)
    print(lift.theLift())