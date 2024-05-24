#deletion at tail
def deletion(head):
    curr=head
    if curr==none and curr.next==none:
        return None
    while curr.next.next!=none:
        curr=curr.next
    curr.next=none
    return head
head=None

#deletion at head
def deletionatstart(head):
    if head==none:
        return None
    secondnode=head.next
    head.next=None
    head=secondnode
    return head

#deletion at particularposition 
#del pos-1 position 
def particularposition(head,pos):
    if pos==0:
        return deletionatstart(head)
    currindex=0
    currnode=head
    while currnode!=pos-1:
        currindex+ = 1
        curr=curr.next