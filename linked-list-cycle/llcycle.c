#include <stddef.h>
#include <stdio.h>
#include <stdbool.h>
#include <assert.h>

struct ListNode {
    int val;
    struct ListNode *next;
};


bool hasCycle(struct ListNode *head) {
    int BIGBOY = 0xffff;
    if (head == NULL || head->next == NULL)
        return false;


    while (head->val != BIGBOY) {
        head->val = BIGBOY;
        head = head->next;
        if (head == NULL || head->next == NULL)
            return false;
        if (head == head->next)
            return true;
    }
    return true;
}


void testcase_1() {
    struct ListNode node1 = {1, NULL};
    struct ListNode node2 = {2, NULL};
    node1.next = &node2;
    node2.next = &node1;
    bool res = hasCycle(&node1);
    assert(res == true);
    printf("testcase 1 PASSED\n");
}


void testcase_2() {
    struct ListNode node1 = {3, NULL};
    struct ListNode node2 = {2, NULL};
    struct ListNode node3 = {0, NULL};
    struct ListNode node4 = {-4, NULL};
    node1.next = &node2;
    node2.next = &node3;
    node3.next = &node4;
    node4.next = &node2;
    bool res = hasCycle(&node1);
    assert(res == true);
    printf("testcase 2 PASSED\n");
}

void testcase_3() {
    struct ListNode node1 = {1, NULL};
    bool res = hasCycle(&node1);
    assert(res == false);
    printf("testcase 3 PASSED\n");
}

int main() {
    testcase_1();
    testcase_2();
    testcase_3();
}
