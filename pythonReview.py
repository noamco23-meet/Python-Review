def create_youtube_video(title, description, hashtag):
	video = {"title":title, "description":description, "likes":0, "dislikes":0, "comments":{}, "hashtag": hashtag}
	return video

def like(video):
	if "likes" in video:
		video["likes"]+=1;
	return video

def dislike(video):
	if "dislikes" in video:
		video["dislikes"]+=1;
	return video

def add_comment(video, username, comment_text):
	video["comments"][username] = comment_text
	return video

def similarity_to_video(video1, video2):
	tagcount = 0
	sametag = 0
	for tag in video1["hashtag"]:
		tagcount+=1
		if tag in video2["hashtag"]:
			sametag+=1

	return (sametag/tagcount)*100



newvideo = create_youtube_video("first video", "hey, this is my first video!", ["new", "first", "hello"])
newvideo = like(newvideo) 
newvideo = add_comment(newvideo, "noam", "incredible")
print(newvideo)

secondvideo = create_youtube_video("second video", "hey, this is my second video", ["latest", "second", "hello"])

print("The two videos are " + str(int(similarity_to_video(newvideo, secondvideo))) +"% similar")	