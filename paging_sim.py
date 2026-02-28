#   Paging Simulation homework

def  read_file(filename):
    open_f = open(filename, 'r')
    lines = open_f.readlines()
    open_f.close()
    for i in range(len(lines)):
        print(lines[i].strip())
    return lines


def optimal_sim(lines):
    #Optimal - when you need to replace a page, replace the one whose next reference is furthest in the future.
    

    
    return 0

def fifo_sim(lines):
    #FIFO - when you need to replace a page, replace the one that was loaded furthest in the past.



    return 0

def second_chance_sim(lines):
    # Second chance - Each page frame has an associated bit (the second chance bit) initially set to 0.  
    # The bit is also set to 0 whenever a page is loaded into the associated frame.  
    # Whenever the page in a given frame is referenced, set the associated bit to 1.  
    # When you need to put a page into a frame (a page is referenced that is not already in a frame), do a round-robin look at the bits.  
    # If a given bit is 1, set it to 0 and continue.  If a given bit is 0, remove that page and load the new one 
    # into that frame (remember to set that bit to 0). When you need to do your round robin look, start with the bit for the page frame 
    # immediately AFTER the frame where you most recently loaded a new page (the first time any page is loaded, start with the first frame).



    return 0

def lru_sim(lines):
    # LRU - when you need to replace a page, replace the one that was referenced least recently.



    return 0

def main():
    lines = read_file("data.txt")

    optimal_sim(lines) #| TODO |

    fifo_sim(lines) #| TODO |

    second_chance_sim(lines) #| TODO |

    lru_sim(lines) #| TODO |


if __name__ == "__main__":
    main()