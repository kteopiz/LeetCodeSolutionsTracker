
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
     




if __name__ == "__main__":
    x = ListNode(1)
    x.next = ListNode(2)

    print(reverse_ll(x))

