class HitCounter {
private:
    std::mutex HitCounterMutex;
    
    vector<int> hits;
public:
    /** Initialize your data structure here. */
    HitCounter() {}
    
    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    void hit(int timestamp) {
        std::lock_guard guard(this->HitCounterMutex);
        
        hits.push_back(timestamp);
    }
    
    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    int getHits(int timestamp) {
        std::lock_guard guard(this->HitCounterMutex);        
        
        int i;
        
        for (i = 0; i < hits.size(); i++) {
            // binary search is an obvious alternative, adaptive binary search approach is even more
            if (hits[i] > timestamp - 300)
                break;        
        }
        
        if (i == 0 && i == hits.size())
            return hits.size();
        
        hits.erase(hits.begin(), hits.begin()+i);
        
        return hits.size();
    }
};

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter* obj = new HitCounter();
 * obj->hit(timestamp);
 * int param_2 = obj->getHits(timestamp);
 */