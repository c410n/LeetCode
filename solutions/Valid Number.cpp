// " .55e16 " considered to be a valid number as the '0' before '.' can be omitted
// " 0.e1" " considered to be a valid number
// " +.1e1" considered to be a valid number
class Solution {
public:
    bool isNumber(string s) {        
        // 0. INITIALIZATION (WILL BE MOVED TO A CONSTRUCTOR IF THAT WILL BE A STATE MACHINE ALGO CLASS)
        const char* str = s.c_str();
        bool number_detected = false;
        
        // 1. SPACE ELIMINATION STAGE
        while (*str == ' ') {            
            str++;
        }
        
        // 2. CHECKING FOR A POSSIBLE '-' OR '+' SIGN
        if (*str == '-' || *str == '+') {
            str++;
        }
        
        // 3. CHECK FIRST NUMBER IF ANY
        if (*str <= '9' && *str >= '0') {
            str++;
            number_detected = true;
            
            // 4. REST OF THE NUMBERS PROCESSING STAGE
            while (*str <= '9' && *str >= '0') {
                str++;
            }
        }
        
        // 5. CHECK FOR THE DOT AT LEAST IF DOT THEN BEFORE OR AFTER A NUMBER MUST BE PRESENT
        if (*str == '.') {
            str++;
        }
        
        // 6. CHECK AN AFTER DOT NUMBER IF ANY
        if (*str <= '9' && *str >= '0') {
            str++;
            number_detected = true;
            
            // 7. REST OF THE NUMBERS PROCESSING STAGE
            while (*str <= '9' && *str >= '0') {
                str++;
            }        
        }
        
        if ( !number_detected )
            return false;
        number_detected = false;
        
        // 8. PROCESS 'e' SYMBOL
        if (*str == 'e') {
            str++;
            
            // 9. CHECKING FOR A POSSIBLE '-' OR '+' SIGN
            if (*str == '-' || *str == '+') {
                str++;
            }
            
            // 10. CHECK FIRST NUMBER IF ANY        
            if (*str <= '9' && *str >= '0') {
                str++;
                number_detected = true;

                // 11. REST OF THE NUMBERS PROCESSING STAGE
                while (*str <= '9' && *str >= '0') {
                    str++;
                }
            }
            
            if (!number_detected)
                return false;
        }
        
        // 12. SPACE ELIMINATION STAGE
        while (*str == ' ') {
            str++;
        }
        
        // C. CHECK FOR EXTRA SYMBOLS LEFT IN A STRING
        if (*str != '\0')
            return false;
        
        return true;
    }
};