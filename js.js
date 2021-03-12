/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var swapNodes = function (head, k) {
	var length_node = head;
	var length = 0;

	while (length_node !== null) {
		length_node = length_node.next;
		length++;
	}

	var neg = head;
	var pos = head;
	var index_neg = 0;
	var index_pos = 0;

	while (index_neg !== length - k || index_pos !== k - 1) {
		if (index_neg !== length - k) {
			index_neg++;
			neg = neg.next;
		}
		if (index_pos !== k - 1) {
			index_pos++;
			pos = pos.next;
		}
	}

	temp = neg.val;
	neg.val = pos.val;
	pos.val = temp;

	return head;
};
