""" Leedcode 2325. Decode the Message """


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        letter = "abcdefghijklmnopqrstuvwxyz"
        temp_key = ""
        dec_message = ""
        for el in key:
            if el not in temp_key and el != " ":
                temp_key += el
        print(temp_key)
        alph_map = dict(zip(temp_key, letter))
        print(alph_map)
        for el in message:
            if el in alph_map:
                dec_message += alph_map[el]
            elif el == " ":
                dec_message += el

        return dec_message


# key = "the quick brown fox jumps over the lazy dog"
# message = "vkbs bs t suepuv"
key = "eljuxhpwnyrdgtqkviszcfmabo"
message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"

s = Solution()
print(s.decodeMessage(key, message))
