class Solution {
public:
    int maxSubArray(vector<int>& num) {
    int max=num[0];
	int sum=0;
    int global_max=max;
	//跑一層迴圈，檢查每一個元素，加上其之前最大的子集合時，會不會比目前的元素大
	for(int i=0;i<num.size();++i){
		//加上num[i]之前的最大的子集合
		sum+=num[i];
		//看看num[i]加上它之前的最大子集合時，會不會比num[i]小，會的話我就不要加了
		if(sum>=num[i]){
			max=sum;
		}else{
			sum=max=num[i];
		}
        if(max>global_max){
            global_max=max;
        }
	}
return global_max;
    }
};