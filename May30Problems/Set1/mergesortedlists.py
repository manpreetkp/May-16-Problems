# Function that merges two sorted linked lists into a snew sorted linked list
# @author Manpreet Kaur

def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0 # pointers for list1 and list2

    # While loop continues as long as there are elements in both lists
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            # Add the smaller element to merged list and increase the pointer by 1
            merged_list = merged_list + [list1[i]]
            i += 1
        else:
            # Add smaller element from list2 and increase the pointer by 1
            merged_list = merged_list + [list2[j]]                
            j += 1

    # Add the rest of the elements from list1 into the merged list
    while i < len(list1):
        merged_list = merged_list + [list1[i]]
        i += 1
    
    # Add the rest of the elements from list2 into the merged list
    while j < len(list2):
        merged_list = merged_list + [list2[j]]
        j+= 1
    
    return merged_list

# Test
list1 = [1, 2, 4]
list2 = [1, 3, 4]
print(merge_sorted_lists(list1, list2))
