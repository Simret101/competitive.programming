class Solution {
public:
    vector<int> arrayChange(vector<int>& nums, vector<vector<int>>& operations) {
       
        unordered_map<int,int> hm;
        for(int i=0;i<nums.size();i++)
        hm[nums[i]]=i;
        for(auto it:operations){
            int ind=hm[it[0]];
            nums[ind]=it[1];
            hm.erase(it[0]);
            hm[it[1]] = ind;
        }
return nums;
    }
};
