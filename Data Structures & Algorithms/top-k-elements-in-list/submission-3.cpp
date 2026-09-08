class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> nums_count;
        for (int n : nums) {
            nums_count[n]++;
        }
        
        vector<vector<int>> buckets(nums.size() + 1);
        for (auto const& [num, count] : nums_count) {
            buckets[count].push_back(num);
        }
        
        vector<int> output;
        
        for (int i = buckets.size() - 1; i >= 0 && k > 0; --i) {
            for (int num : buckets[i]) {
                output.push_back(num);
                k--;
                if (k == 0) {
                    break;
                }
            }
        }
        
        return output;
    }
};
