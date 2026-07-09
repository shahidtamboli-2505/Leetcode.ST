from collections import deque, Counter

class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        n = len(friends)

        visited = [False] * n
        visited[id] = True

        q = deque([id])
        curr_level = 0

        while q and curr_level < level:
            for _ in range(len(q)):
                person = q.popleft()
                for f in friends[person]:
                    if not visited[f]:
                        visited[f] = True
                        q.append(f)
            curr_level += 1

        freq = Counter()

        while q:
            person = q.popleft()
            for video in watchedVideos[person]:
                freq[video] += 1

        return sorted(freq.keys(), key=lambda x: (freq[x], x))