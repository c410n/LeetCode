class Solution {
public:
    int HASH_AL[256]; // x - 97 -> {0 - 25} if only lowercase letters
    
    Solution() {
        memset(HASH_AL, -1, 256 * sizeof(int));
    }       
    
    int lengthOfLongestSubstring(string s) {
        if (!s.size())
            return 0;
        
        // using a 'window' with start point moving each time when the last item is a repeating character
        const char *str = s.c_str();
        const char *base = str;            
                
        int candidate = 0x0;        
        int intermediate = 0x0;
        
        while(*str) {            
            if (HASH_AL[*str] != -1) {
                str = base + HASH_AL[*str];
                str++;
                
                if (intermediate > candidate) 
                    candidate = intermediate;
                    
                intermediate = 0;
                memset(HASH_AL, -1, 256 * sizeof(int));
            } else {
                HASH_AL[*str] = str - base;                
                
                intermediate++;            
                str++;
            }
        }
        
        if (candidate > intermediate)
            return candidate;
        else 
            return intermediate;
    }
};