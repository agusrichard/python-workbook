class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f'{self.val} -> {self.next}'


def add_two_numbers(l1, l2):
    flag = True
    carry = 0
    agg = []
    while flag:
        if l1 == None and l2 == None:
            break
        
        summ = 0
        if l2 == None:
            summ = l1.val + carry
            l1 = l1.next
        elif l1 == None:
            summ = l2.val + carry
            l2 =  l2.next
        else:
            summ = l1.val + l2.val + carry
            l1 = l1.next
            l2 = l2.next
        
        remainder = summ % 10
        agg.append(remainder)
        carry = summ // 10

    if carry != 0:
        agg.append(carry)


    return list_to_linkedlist(agg)

def list_to_linkedlist(lst):
    if len(lst) == 0:
        return None
    return ListNode(val=lst[0], next=list_to_linkedlist(lst[1:]))



print(add_two_numbers(list_to_linkedlist([9,9,9,9,9,9,9]), list_to_linkedlist([9,9,9,9])))
# print(list_to_linkedlist([1,2,3,4,5]))