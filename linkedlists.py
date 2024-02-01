
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def reverse_ll(head):
    slow = None
    fast = head

    while fast:
        temp = fast.next
        fast.next = slow
        slow = fast
        fast = temp
    return slow

def add_two_numbers(l1, l2):
    def traverse(LL):
        number = ""
        while LL:
            number += str(LL.val)
            LL = LL.next
        return number[::-1]

    new_num = int(traverse(l1)) + int(traverse(l2))
    res = None
    for i in str(new_num):
        temp = ListNode(i)
        temp.next = res
        res = temp
    return res
    




if __name__ == "__main__":
    x = ListNode(1)
    x.next = ListNode(2)

    print(reverse_ll(x))

