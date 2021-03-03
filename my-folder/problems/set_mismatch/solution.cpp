class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        vector<int> ans;
        int sum=0;
        int tmp=0;
        int record[10001]={0};
        for(int i=1;i<=nums.size();++i)
            sum+=i;
        for(int j:nums){
            tmp+=j;
            ++record[j];
            if(record[j]>1){
                ans.push_back(j);
                tmp-=j;
            }
        }
        ans.push_back(sum-tmp);
        
       
        
        return ans;
    }
};