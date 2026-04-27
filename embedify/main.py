import argparse
import re

def getytid(url):
    split_yt_id = url.replace("https://youtube.com/shorts/", "")
    return split_yt_id.split("?")[0]

def getinstaid(url):
    split_insta_id = url.replace("https://instagram.com/reel/", "")
    return split_insta_id.split("?")[0]

def instalink(id):
    insta_embed_link = "https://www.instagram.com/p/{}/embed".format(id)
    return insta_embed_link

def ytlink(id):
    yt_embed_link = "https://www.youtube.com/embed/{}".format(id)
    return yt_embed_link

def embed(link):
    embed_code = "<iframe src={}></iframe>".format(link)
    return embed_code

def output(embed_link, embed_code):
    print("Embed link:", embed_link)
    print("Embed code:", embed_code)


input = argparse.ArgumentParser(
    prog='Embedify',
    description='Converts instagram reels and youtube shorts into embed links and embed code',
    epilog='In collab with Jesus made with <3 by WeenAIthDev'
)

input.add_argument('--url', help="Add a youtube shorts or instagram reel link to generate embed link and embed code.")
arg_url = input.parse_args()
url = arg_url.url

instagram_domain_match = re.search("instagram", url)
instagram_reel_match = re.search("reel",url)
yt_domain_match = re.search("youtube", url)
yt_shorts_match = re.search("shorts",url)

try:
    if instagram_domain_match and instagram_reel_match:
        insta_id = getinstaid(url)
        embed_insta_link = instalink(insta_id)
        code_insta = embed(embed_insta_link)
        output(embed_insta_link, code_insta)

    elif yt_domain_match and yt_shorts_match:
        yt_id = getytid(url)
        embed_yt_link = ytlink(yt_id)
        code_yt = embed(embed_yt_link)
        output(embed_yt_link, code_yt)

    else:
        print("Invalid, Please enter only instagram reel or youtube shorts links only")

except:
    print("An error has occured")

finally:
    print("Embedify terminated")