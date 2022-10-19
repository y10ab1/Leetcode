class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        key_val_tuple_list = [(-v,k) for k,v in collections.Counter(words).items()]
        ans = [word for _,word in sorted(key_val_tuple_list)[:k]]
        return ans