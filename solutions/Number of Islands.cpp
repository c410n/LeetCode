class Solution {
private:
    set<pair<int, int> > data;
    vector<vector<char> > grid;
    unsigned int x_max;
    unsigned int y_max;
    
    // land elimination
    void eliminateAllConnectingLand(int x, int y) {
        if ((unsigned)x >= x_max || (unsigned)y >= y_max)
            return;
        
        if (data.find(pair<int, int>(x, y)) != data.end()) {
            data.erase(pair<int, int>(x, y));
            
            if (grid[x][y] == '1') {                
                // up
                eliminateAllConnectingLand(x, y-1);
                // down
                eliminateAllConnectingLand(x, y+1); 
                // right
                eliminateAllConnectingLand(x+1, y);
                // left
                eliminateAllConnectingLand(x-1, y);
            }
        }
    }
    
public:
    int numIslands(vector<vector<char>>& grid_) {
        data.clear();
        grid = grid_;
        
        if (!grid.size())
            return 0;
        if (!grid[0].size())
            return 0;
                
        x_max = grid.size();
        y_max = grid[0].size();
        
        for (int i1 = 0; i1 < grid.size(); i1++) {
            for (int i2 = 0; i2 < grid[i1].size(); i2++)
                data.insert(pair<int, int>(i1, i2));
        }
        
        int number_of_islands = 0;
        
        set<pair<int, int> >::iterator it = data.begin();
        pair<int, int> position;
        
        do {            
            position = *it;
            
            if (grid[position.first][position.second] == '0')
                data.erase(position);
            else {
                number_of_islands++;
                
                eliminateAllConnectingLand(position.first, position.second);
            }
        } while ((it = data.begin()) != data.end());
        
        return number_of_islands;
    }
};