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

def output(embed_link, embed_code, url_type, url, output_file):
    print("Embed link:", embed_link)
    print("Embed code:", embed_code)
    with open(output_file, 'a') as o:
      o.write("For "+ url_type +": " +url+ "\n")
      o.write("Embed link: "+ embed_link + "\n")
      o.write("Embed code: "+ embed_code + "\n")
    o.close()
      

def url_matcher(url):
     instagram_domain_match = re.search("instagram", url)
     instagram_reel_match = re.search("reel",url)
     yt_domain_match = re.search("youtube", url)
     yt_shorts_match = re.search("shorts",url)

     if instagram_domain_match == None and instagram_reel_match == None:
        instagram_domain_match = False
        instagram_reel_match = False
     else:
        yt_domain_match = False
        yt_shorts_match = False   
     
     return {"instagram_domain_match":instagram_domain_match, "instagram_reel_match":instagram_reel_match, "yt_domain_match":yt_domain_match, "yt_shorts_match":yt_shorts_match}

def compute_embeds(instagram_domain_match, instagram_reel_match, yt_domain_match, yt_shorts_match, url, output_file):
    try:
      if instagram_domain_match and instagram_reel_match:
        url_type = "instagram reel"
        insta_id = getinstaid(url)
        embed_insta_link = instalink(insta_id)
        code_insta = embed(embed_insta_link)
        output(embed_insta_link, code_insta, url_type, url, output_file)

      elif yt_domain_match and yt_shorts_match:
        url_type = "yt shorts"
        yt_id = getytid(url)
        embed_yt_link = ytlink(yt_id)
        code_yt = embed(embed_yt_link)
        output(embed_yt_link, code_yt, url_type, url, output_file)

      else:
        print("Invalid, Please enter only instagram reel or youtube shorts links only")

    except:
      print("An error has occured")

    finally:
      print("Embedify terminated")     

def url_parser(input_source, output_file):
    if ('.txt'not in input_source):
      match = url_matcher(input_source)
      instagram_domain_match = match['instagram_domain_match']
      instagram_reel_match = match['instagram_reel_match']
      yt_domain_match = match['yt_domain_match']
      yt_shorts_match = match['yt_shorts_match']    
      compute_embeds(instagram_domain_match, instagram_reel_match, yt_domain_match, yt_shorts_match,input_source, output_file)

    else:
        f = open(input_source, 'r', encoding="utf-8")
        for line in f:
            url_file = line
            match = url_matcher(url_file)
            instagram_domain_match = match['instagram_domain_match']
            instagram_reel_match = match['instagram_reel_match']
            yt_domain_match = match['yt_domain_match']
            yt_shorts_match = match['yt_shorts_match']    
            compute_embeds(instagram_domain_match, instagram_reel_match, yt_domain_match, yt_shorts_match,line,output_file)
        f.close()
    

input = argparse.ArgumentParser(
    prog='Embedify',
    description='Converts instagram reels and youtube shorts into embed links and embed code storig it into an output.txt file',
    epilog='In collab with Jesus made with <3 by WeenAIthDev'
)

input.add_argument('--url', help="Add a youtube shorts or instagram reel link to generate embed link and embed code.")
input.add_argument('--file', help="Add a youtube shorts or instagram reel links in file to generate embed link and embed code.")
input.add_argument('--append', help="Adds embed code and link to a file without clearing", action='store_false')
input.add_argument('--outputfile', help="Add generated embed link and embed code to output file name specified of .txt format." )
arg_url = input.parse_args()
if arg_url.url and not arg_url.file:
  url = arg_url.url
  url_parser(url, arg_url.outputfile)
elif arg_url.url and arg_url.file:
   url = arg_url.url
   file = arg_url.file
   url_parser(url, arg_url.outputfile)  
   url_parser(file, arg_url.outputfile)
elif arg_url.file and not arg_url.url:  
 file = arg_url.file
 url_parser(file, arg_url.outputfile)
else:
   print("Invalid input format please add only urls or .txt files")             



