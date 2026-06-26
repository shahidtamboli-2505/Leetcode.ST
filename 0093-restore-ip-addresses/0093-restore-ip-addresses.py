class Solution(object):
    def restoreIpAddresses(self, s):
        ans = []

        def dfs(index, parts):
            if len(parts) == 4:
                if index == len(s):
                    ans.append(".".join(parts))
                return

            for l in range(1, 4):
                if index + l > len(s):
                    break

                part = s[index:index + l]

                if len(part) > 1 and part[0] == '0':
                    continue

                if int(part) > 255:
                    continue

                parts.append(part)
                dfs(index + l, parts)
                parts.pop()

        dfs(0, [])
        return ans