class Twitter:

    def __init__(self):
        self.tweets = {}
        self.tweet_counter = 0
        self.followers = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = [(self.tweet_counter, tweetId)]
            self.followers[userId] = {userId: 1}
        else:
            self.tweets[userId].append((self.tweet_counter, tweetId))
        self.tweet_counter += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # print(self.followers[userId])
        followers = [f for f in self.followers[userId] if self.followers[userId][f] == 1]
        # print(userId, followers)
        tweets = []
        for person in followers:
            tweets.extend(self.tweets[person])
        
        # print(tweets)
        tweets.sort(key=lambda x:-x[0])
        return [t[1] for t in tweets[:10]]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = {followeeId: 1}
        else:
            self.followers[followerId][followeeId] = 1
        print("in follow", self.followers)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId][followeeId] = 0
        
