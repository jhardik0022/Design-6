# Time complexity : O(L) --> k = 3
# Space complexity : O(n*L*4) --> frequency map, 4 is the size of list at each TrieNode
# Trie with Heap
# class for Trie
class TrieNode:
    def __init__(self,):
        self.children = [None for _ in range(256)]
        self.strList = []
        
class AutocompleteSystem:
    # inserting a sentence in Trie
    def insert(self, sentence):
            curr = self.root
            for i in range(len(sentence)):
                ch = sentence[i]
                # check if the char for current children is None, if so then make a new TrieNode
                if curr.children[ord(ch) - ord(' ')] == None:
                    curr.children[ord(ch) - ord(' ')] = TrieNode()
                # else move ahead the current pointer
                curr = curr.children[ord(ch) - ord(' ')]
                # we are appending the sentences as each TriNode
                if sentence not in curr.strList:
                    curr.strList.append(sentence)
                
                # custom sort function to sort the frequency of sentences in terms of decreasing frequency
                # if similar frequency, then lexographically which is the sentence itself
                curr.strList.sort(key = lambda x : (-self.freq[x],x))
                if len(curr.strList) > 3:
                    curr.strList.pop()
                
    
    # search for a prefix in Trie
    def search(self, prefix):
        curr = self.root
        for i in range(len(prefix)):
            ch = prefix[i]
            if curr.children[ord(ch) - ord(' ')] == None:
                # if the current children has nothing, then we return an empty list
                return []
            curr = curr.children[ord(ch) - ord(' ')]
        # else return the list
        return curr.strList
        
    def __init__(self, sentences: List[str], times: List[int]):
        self.sentences = sentences
        self.times = times
        self.freq = {}
        self.input_str = ''
        self.root = TrieNode()
        
        # building Hashmap with the frequency
        for i in range(len(self.sentences)):
            if self.sentences[i] in self.freq:
                self.freq[self.sentences[i]] = self.freq[self.sentences[i]] + times[i]
            else:
                self.freq[self.sentences[i]] = times[i]
                # insert into Trie only if the sentence is not present in the HashMap
            self.insert(self.sentences[i])
            

    def input(self, c: str) -> List[str]:
        # if the input is # then we check for the string in Hashmap and increase it's frequency is present
        # else make it 1, and return an empty string
        if c == '#':
            search_str = self.input_str
            if search_str not in self.freq:
                # insert the str into Trie and Hashmap only if they are not present
                self.freq[search_str] = 1
            else:
                self.freq[search_str] += 1
            self.insert(search_str)
            self.input_str = ''
            return []
        self.input_str += c
        prefix = self.input_str
        # fetch the list from Trie for the matching prefix
        return self.search(prefix)
         
# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)