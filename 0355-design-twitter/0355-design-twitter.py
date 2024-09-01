class Twitter:

    def __init__(self):
        self.time = 0
        self.followees = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweets[userId].append([self.time, tweetId])
        self.followees[userId].add(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for followee in self.followees[userId]:
            tweets = self.tweets[followee]
            if tweets:
                res += tweets
        heapq.heapify(res)
        recentTweets = []
        for _ in range(10):
            if res:
                recentTweets.append(heapq.heappop(res)[1])
        return recentTweets


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId] and followerId != followeeId:
            self.followees[followerId].remove(followeeId)
