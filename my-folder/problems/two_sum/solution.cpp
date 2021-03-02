class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> index;
        map<int,int> hash;
        vector<int> ans;
        int cnt=0;
        for(int i:nums)
            index[i]=cnt++;
        for(int x:nums)
            hash[x]=target-x;
        for(int i=0;i<nums.size();++i){
            if(index.find(target-nums[i])!=index.end()){
                if(i==index[target-nums[i]])
                    continue;
                ans.push_back(i);
                ans.push_back(index[target-nums[i]]);
                
                return ans;
            }
        }
        return ans;
    }
};