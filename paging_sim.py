#   Paging Simulation homework


def  read_file(filename):
    # first line of the file - number of page frames we got
    #the rest are the page references.
    open_f = open(filename, 'r')
    frames = int(open_f.readline().strip())
    page_refs = []
    for line in open_f:
        page_refs.append(int(line.strip()))

    #print("Number of frames: ", frames)
    #print("Page references: ", page_refs)
    #print(page_refs[0])
    open_f.close()
    
    return frames, page_refs


def optimal_sim(frames, page_refs):
    #Optimal - when you need to replace a page, replace the one whose next reference is furthest in the future.
    page_faults = 0
    memory_page_frames = []
    page_refs_copy = page_refs.copy() # removes the used ones as we go without editing og list

    for page in page_refs:
        if page not in memory_page_frames:
            page_faults += 1
            if len(memory_page_frames)<frames:
                memory_page_frames.append(page)
                page_refs_copy.pop(0) # keeping track of where we are 
            else:
                furthest_page = None
                furthest_away = 0 #
                for page_frame in memory_page_frames:
                    if page_frame not in page_refs_copy:
                        furthest_page =page_frame # if it doesnt occur again then thats the one that we replace
                        break
                    else:
                        next_index= page_refs_copy.index(page_frame)
                        if next_index >furthest_away:# this way we can count how far the next occurence is 
                            furthest_away = next_index 
                            furthest_page = page_frame  # set it 

                memory_page_frames.remove(furthest_page)
                memory_page_frames.append(page)
                page_refs_copy.pop(0)
        else:
            page_refs_copy.pop(0)

    print("Optimal page faults: ", page_faults)
    return None

def fifo_sim(frames, page_refs):
    #FIFO - when you need to replace a page, replace the one that was loaded furthest in the past.
    page_faults = 0
    memory_page_frames = []

    for page in page_refs:
        if page not in memory_page_frames:
            page_faults += 1
            if len(memory_page_frames) < frames:
                memory_page_frames.append(page) 
            else:
                memory_page_frames.pop(0) # super straight forward, pop most recent one and add new one. it will alaways be in order
                memory_page_frames.append(page)


    print("FIFO page faults: ", page_faults)
    return None

def second_chance_sim(frames, page_refs):
    # Second chance - Each page frame has an associated bit (the second chance bit) initially set to 0.  
    # The bit is also set to 0 whenever a page is loaded into the associated frame.  
    # Whenever the page in a given frame is referenced, set the associated bit to 1.  
    # When you need to put a page into a frame (a page is referenced that is not already in a frame), do a round-robin look at the bits.  
    # If a given bit is 1, set it to 0 and continue.  If a given bit is 0, remove that page and load the new one 
    # into that frame (remember to set that bit to 0). When you need to do your round robin look, start with the bit for the page frame 
    # immediately AFTER the frame where you most recently loaded a new page (the first time any page is loaded, start with the first frame).
    page_faults = 0
    memory_page_frames = []
    page_refs_copy = page_refs.copy()
    rr_pointer = 0

    for page in page_refs_copy:
        if page not in memory_page_frames:
            page_faults +=1
            if len(memory_page_frames) <frames:
                memory_page_frames.append(page) 
            else:
                while True:
                    if memory_page_frames[rr_pointer] == 1: # if the bit is 1, set it to 0 
                        memory_page_frames[rr_pointer]= 0 
                        rr_pointer += 1
                        if rr_pointer >= frames:
                            rr_pointer = 0
                    else: 
                        memory_page_frames[rr_pointer]= page # otherwise rplace the page 
                        rr_pointer += 1
                        if rr_pointer >= frames:
                            rr_pointer = 0
                        break 


    print("Second Chance page faults: ", page_faults)
    return None

def lru_sim(frames, page_refs):
    # LRU - when you need to replace a page, replace the one that was referenced least recently.
    page_faults = 0
    memory_page_frames = []
    page_refs_copy = page_refs.copy()

    for page in page_refs_copy:
        if page in memory_page_frames:
            # move the page to the end of the list to mark it as most recently used
            memory_page_frames.remove(page)
            memory_page_frames.append(page)
        else:
            page_faults += 1
            if len(memory_page_frames) == frames:
                memory_page_frames.pop(0) # remove least recently used page
            memory_page_frames.append(page) 

    print("LRU page faults: ", page_faults)

    return None


def main():
    #frames, page_refs = read_file("data1.txt") #for the testing 
    frames, page_refs = read_file("data.txt")

    optimal_sim(frames, page_refs) #| works | sould be 9 page faults on the test data1.txt

    fifo_sim(frames, page_refs) #| works | should be 15 page faults on the test data1.txt 

    second_chance_sim(frames, page_refs) #| TODO | 

    lru_sim(frames, page_refs) #| works | should be 12 page faults on the test data1.txt




if __name__ == "__main__":
    main()