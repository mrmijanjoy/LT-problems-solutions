class ListNode {
    constructor(val, next = null) {
        this.val = val;
        this.next = next;
    }
}

const addTwoNumbers = (l1, l2) => {
    let dummy = new ListNode(0);
    let current = dummy;
    let carry = 0;

    while (l1 !== null || l2 !== null) {
        const val1 = l1 !== null ? l1.val : 0;
        const val2 = l2 !== null ? l2.val : 0;
        const sum = val1 + val2 + carry;

        carry = Math.floor(sum / 10);
        current.next = new ListNode(sum % 10);
        current = current.next;

        if (l1 !== null) l1 = l1.next;
        if (l2 !== null) l2 = l2.next;
    }

    if (carry > 0) {
        current.next = new ListNode(carry);
    }

    return dummy.next;
};

// Example usage:
const l1 = new ListNode(2, new ListNode(4, new ListNode(3)));
const l2 = new ListNode(5, new ListNode(6, new ListNode(4)));

const result = addTwoNumbers(l1, l2);

// Function to print the result linked list
const printList = (head) => {
    let current = head;
    while (current !== null) {
        console.log(current.val);
        current = current.next;
    }
};

printList(result);
