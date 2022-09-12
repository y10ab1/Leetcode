class Solution {
public:
    int jump(vector<int>& nums) {
        if(nums.size() == 1){
            return 0;
        }
        int l = 0;
        int ans = 1;
        int r = nums[0];
        while(r < nums.size()-1){
            ++ans;
            int nxt = 0;
            for(int i=l+1;i<=r;++i){
                nxt = max(nxt, i+nums[i]);
            }
            
            l = r;
            r = nxt;
        }
        return ans;
    }
};