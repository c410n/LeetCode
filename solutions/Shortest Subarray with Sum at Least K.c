int shortestSubarray(int* A, int ASize, int K) {
    int *A_back = A, *A_front = A, *A_end = A + ASize, min_length = INT_MAX, sum = 0;
    bool direct_pass = true;
    
begin:
    if (direct_pass) {
begin_direct:
        if (A_front >= A_end)
            goto end;
        
        sum += *A_front;
        
        if (sum >= K) {
            int shorter_distance = A_front - A_back + 1;
            if (shorter_distance < min_length)
                min_length = shorter_distance;
            
            if (min_length == 1)
                return min_length;
            
            direct_pass = false;            
            A_back = A_front;
            sum = 0;
            
            goto begin;
        }  
        
        if (sum < 0) {  
            sum = 0;
            A_back = ++A_front;
            goto begin;
        } else {        
            A_front++;
            goto begin_direct;
        }
    } else {  
begin_reverse:
        if (A_back < A)
            goto end;
            
        sum += *A_back;
        
        if (sum >= K) {
            int shorter_distance = A_front - A_back + 1;
            if (shorter_distance < min_length)
                min_length = shorter_distance;            
            
            if (min_length == 1)
                return min_length;
            
            direct_pass = true;
            A_front = ++A_back;
            sum = 0;
            
            goto begin;
        }       
        
        if (sum < 0) {
            sum = 0;
            A_back = ++A_front;
            direct_pass = true;
            goto begin;
        } else {
            A_back--;            
            goto begin_reverse;            
        }
        
    }
end:
    return min_length>ASize?-1:min_length;
}