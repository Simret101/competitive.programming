class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
     unordered_map<int,int> mymap;
        
        for(int i=0;i<nums.size();++i){
            if(mymap.count(target-nums[i]))
                return {i,mymap[target-nums[i]]};
           
            mymap[nums[i]] = i;
        }
        return {};
    }
};
