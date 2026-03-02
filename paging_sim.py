#   Paging Simulation homework

class PageFrame:
    def __init__(self, page_num):
        self.page_num = page_num
        self.second_chance_bit = 0
        self.last_used= 0
        self.valid = 0



def  read_file(filename):
    # first line of the file - number of page frames we got
    #the rest are the page references.
    open_f = open(filename, 'r')
    frames = int(open_f.readline().strip())
    page_refs = []
    for line in open_f:
        page_refs.append(int(line.strip()))

    print("Number of frames: ", frames)
    print("Page references: ", page_refs)
    print(page_refs[0])


    open_f.close()
    
    return frames, page_refs


def optimal_sim(frames, page_refs):
    #Optimal - when you need to replace a page, replace the one whose next reference is furthest in the future.
    page_faults = 0



    

    
    return page_faults

def fifo_sim(frames, page_refs):
    #FIFO - when you need to replace a page, replace the one that was loaded furthest in the past.
    page_faults = 0






    return page_faults

def second_chance_sim(frames, page_refs):
    # Second chance - Each page frame has an associated bit (the second chance bit) initially set to 0.  
    # The bit is also set to 0 whenever a page is loaded into the associated frame.  
    # Whenever the page in a given frame is referenced, set the associated bit to 1.  
    # When you need to put a page into a frame (a page is referenced that is not already in a frame), do a round-robin look at the bits.  
    # If a given bit is 1, set it to 0 and continue.  If a given bit is 0, remove that page and load the new one 
    # into that frame (remember to set that bit to 0). When you need to do your round robin look, start with the bit for the page frame 
    # immediately AFTER the frame where you most recently loaded a new page (the first time any page is loaded, start with the first frame).
    page_faults = 0






    return page_faults

def lru_sim(frames, page_refs):
    # LRU - when you need to replace a page, replace the one that was referenced least recently.
    page_faults = 0





    return page_faults

def main():
    #frames, page_refs = read_file("data.txt")
    frames, page_refs = read_file("data1.txt")

    optimal_sim(frames, page_refs) #| TODO | sould be 9 page faults on the test data1.txt

    fifo_sim(frames, page_refs) #| TODO | should be 15 page faults on the test data1.txt 

    second_chance_sim(frames, page_refs) #| TODO |

    lru_sim(frames, page_refs) #| TODO |


if __name__ == "__main__":
    main()