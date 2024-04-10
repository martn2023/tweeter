# Tweeter (Twitter clone)
A live demo will be hosted on Heroku

## Author's context:
Last week, I published my first homegrown CRUD: [Yindeed](https://github.com/martn2023/yindeed1/blob/master/README.md). The learnings and feedback from mentors has driven the following goals for this project:

## What I built:
>**Overview:**<br>
A slim social media site similar to Twitter, but with a few design nuances:
>* user A can create an "Original Post":
>  * users A or B can "Reply" to Original Post, but not to a Reply
>  * replies from B show up in A's "Feed"
>* user A can subscribe to user B:
>  * in A's Feed, B's Original Posts show up, but not B's replies
>* Feed content is not censored, filtered, prioritized by select authors nor following size. For now, content is only sortable in reverse chronology 

## New technical achievements:
>**PERSISTENT DATA - PostGres:**
Heroku doesn't support persistent data with SQLlite, which drove me towards PostGres. This marks my first PostGres installation ever.


## Potential improvements:
>**NESTED REPLIES:**<br>
Think of Reddit.com's reply structure<br>

>**DOWNVOTING:**
  
>**NESTED REPLIES:**<br>
Think of Reddit.com's reply structure<br>

>**RECOMMENDATION ENGINE:**<br>
Feed content would be filtered and prioritized based off a staff-determined scoring system. A further advancement would allow users to customize how this recommendation engine thinks i.e. would it focus on the speaker more than the message content? The topic more than the recency?