#https://leetcode.com/problems/defanging-an-ip-address/
#https://leetcode.com/submissions/detail/1234927335/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', "[.]")