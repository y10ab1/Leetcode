class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
                set<int> s;
        for(int x:candyType){
            s.insert(x);
        }
        if(s.size()>candyType.size()/2){
            return candyType.size()/2;
        }else{
            return s.size();
        }
    }
};