/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        bool carry = false;
        ListNode *lr = nullptr, *node = nullptr, *candidate = nullptr;
        int number;
        
        while(true) {
            if (l1 == nullptr && l2 == nullptr) {
                if (carry) {
                    candidate = new ListNode(1);
                    
                    if (lr == nullptr) {
                        lr = candidate;
                    } else {
                        node->next = candidate;
                    }
                    
                    break;
                } else {
                    break;
                }
            } else if (l1 == nullptr && l2 != nullptr) {                
                if (carry) {
                    number = 1 + l2->val;
                    
                    if (number > 9) {
                        carry = true;                        
                        number -= 10;
                            
                        candidate = new ListNode(number);
                        
                        if (lr == nullptr) {
                            lr = node = candidate;
                        } else {
                            node = node->next = candidate;
                        }
                    } else {
                        carry = false;
                            
                        candidate = new ListNode(number);
                        
                        if (lr == nullptr) {
                            lr = node = candidate;
                        } else {
                            node = node->next = candidate;
                        }
                    }
                } else {
                    number = l2->val;
                            
                    candidate = new ListNode(number);
                        
                    if (lr == nullptr) {
                        lr = node = candidate;
                    } else {
                        node = node->next = candidate;
                    }                   
                }
            } else if (l1 != nullptr && l2 == nullptr) {
                if (carry) {
                    number = 1 + l1->val;
                    
                    if (number > 9) {
                        carry = true;                 
                        number -= 10;
                            
                        candidate = new ListNode(number);
                        
                        if (lr == nullptr) {
                            lr = node = candidate;
                        } else {
                            node = node->next = candidate;
                        }
                    } else {
                        carry = false;
                            
                        candidate = new ListNode(number);
                        
                        if (lr == nullptr) {
                            lr = node = candidate;
                        } else {
                            node = node->next = candidate;
                        }
                    }
                } else {
                    number = l1->val;
                    
                    if (number > 9) {
                        carry = true;                 
                        number -= 10;
                            
                        candidate = new ListNode(number);
                        
                        if (lr == nullptr) {
                            lr = node = candidate;
                        } else {
                            node = node->next = candidate;
                        }
                    } else {
                        carry = false;
                            
                        candidate = new ListNode(number);
                        
                        if (lr == nullptr) {
                            lr = node = candidate;
                        } else {
                            node = node->next = candidate;
                        }
                    }
                }
            } else {
                if (carry) {
                    number = 1 + l1->val + l2->val;
                    
                    if (number > 9) {
                        carry = true;                 
                        number -= 10;
                            
                        candidate = new ListNode(number);
                        
                        if (lr == nullptr) {
                            lr = node = candidate;
                        } else {
                            node = node->next = candidate;
                        }
                    } else {
                        carry = false;
                            
                        candidate = new ListNode(number);
                        
                        if (lr == nullptr) {
                            lr = node = candidate;
                        } else {
                            node = node->next = candidate;
                        }
                    }
                } else {
                    number = l1->val + l2->val;
                    
                    if (number > 9) {
                        carry = true;                 
                        number -= 10;
                            
                        candidate = new ListNode(number);
                        
                        if (lr == nullptr) {
                            lr = node = candidate;
                        } else {
                            node = node->next = candidate;
                        }
                    } else {
                        carry = false;
                            
                        candidate = new ListNode(number);
                        
                        if (lr == nullptr) {
                            lr = node = candidate;
                        } else {
                            node = node->next = candidate;
                        }
                    }
                }
            }
            
            // Setting nodes for next iteration
            if (l1) {
                l1 = l1->next;
            }
            if (l2) {
                l2 = l2->next;
            }
        }
        
        return lr;
    }
};