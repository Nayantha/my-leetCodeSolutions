from add_two_numbers import ListNode, add_two_numbers


def test_add_two_numbers():
    l1_val_list = [ListNode(2), ListNode(4), ListNode(3)]
    l1_val_list[0].next = l1_val_list[1]
    l1_val_list[1].next = l1_val_list[2]
    l1 = l1_val_list[0]

    l2_val_list = [ListNode(5), ListNode(6), ListNode(4)]
    l2_val_list[0].next = l2_val_list[1]
    l2_val_list[1].next = l2_val_list[2]
    l2 = l2_val_list[0]

    expected_val_list = [ListNode(7), ListNode(0), ListNode(8)]
    expected_val_list[0].next = expected_val_list[1]
    expected_val_list[1].next = expected_val_list[2]
    expected = expected_val_list[0]

    output = add_two_numbers(l1, l2)

    while expected and output:
        assert expected.val == output.val
        expected = expected.next
        output = output.next
