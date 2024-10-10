#made by Ira

from twitterPost import postOnTwitter

def main():
    imagesToPost = ['myNameIsIra.png']
    wordsToPost = "Hello World!"

    postOnTwitter(wordsToPost, imagesToPost)

if __name__ == "__main__":
    main()