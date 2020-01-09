import pandas as pd

youtube = pd.read_csv("USvideos.csv.csv")
print(youtube.head())

youtube.drop(["thumbnail_link","video_id","trending_date","publish_time","comments_disabled","ratings_disabled","video_error_or_removed"],
             axis=1,inplace=True)
print(youtube)

print(len(youtube.index))
print(len(youtube.columns))

likes = youtube["likes"].mean()
print(likes)

dislikes = youtube["dislikes"].mean()
print(dislikes)

views = youtube[youtube["views"] == youtube["views"].max()]["title"].iloc[0]
print(views)

min_views = youtube[youtube["views"] == youtube["views"].min()]["title"].iloc[0]
print(min_views)

avg_comment = youtube.groupby("category_id").mean()["comment_count"]
print(avg_comment)

cat = youtube["category_id"].value_counts()
print(cat)

youtube["title_length"] = youtube["title"].apply(len)
print(youtube)

#tags

def countTag(tag):
    tagLsit = tag.split("|")
    return len(tagLsit)

youtube["tagCount"] = youtube["tags"].apply(countTag)
print(youtube)

def likesdislikesratio(like,dislike):
    likesList = []
    for key, value in list(youtube["likes"].iteritems()):
        likesList.append(value)
    dislikesList = []
    for key, value in list(youtube["dislikes"].iteritems()):
        dislikesList.append(value)

    likedislike = list(zip(likesList,dislikesList))
    ratio = []
    for like,dislike in likedislike:
        if(like + dislike) == 0:
            ratio.append(0)
        else:
            ratio.append(like / (like + dislike))
    return ratio

youtube["likes_dislikes"] = likesdislikesratio(youtube["likes"],youtube["dislikes"])
youtube.sort_values("likes_dislikes",ascending = False, inplace = True)
print(youtube)

