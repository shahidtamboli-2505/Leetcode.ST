class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy

        carry = 0

        while l1 or l2 or carry:
            # Get values
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Add
            total = x + y + carry

            # Current digit
            digit = total % 10

            # New carry
            carry = total // 10

            # Create node
            curr.next = ListNode(digit)
            curr = curr.next

            # Move lists
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next