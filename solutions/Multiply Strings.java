class Solution {    
    public String multiply(String num1, String num2) {
        if (num1 == null || num2 == null)
            return null;
        
        if (num1.isEmpty() || num2.isEmpty())
            return null;
        
        int left_l = num1.length()-1;
        int right_l = num2.length()-1;
        
        int result_i_size = left_l + right_l + 2;
        int result_i_last = result_i_size - 1;
        
        int[] result_i = new int[result_i_size];
        
        int result_it = 0, slow_iterator = 0;
        
        for (int i1 = left_l; i1 >= 0; i1--) {
            for (int i2 = right_l; i2 >= 0; i2--) {
                result_i[result_it] += (num1.charAt(i1)-'0') * (num2.charAt(i2)-'0');
                result_it++;
            }
            
            result_it = ++slow_iterator;
        }
             
        // spread the number over the vector of cells
        for (int i = 0; i < result_i_last; i++) {
            int number = result_i[i] % 10;
            int remainder = result_i[i] / 10;
            
            result_i[i] = number;
            
            //if (i < result_i_size) // this can't occur mathematically   
            result_i[i+1] += remainder;                 
        }
                
        String result_s = "";
        
        result_it = 0;
        while(result_it < result_i_size) {
            String tmp = "";
            
            while (result_i[result_it] == 0) {
                tmp = '0' + tmp;
                
                if (result_it < result_i_last)
                    result_it++;
                else
                    return (result_s.isEmpty())?"0":result_s;
            }
            
            result_s = result_i[result_it++] + tmp + result_s;
        }

        return result_s;
    }
}