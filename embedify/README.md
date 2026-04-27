# Embedify
#### A command line tool that converts instagram reels and youtube shorts urls into embed url wrapped into iframe basically a embed code generator.
```
        ┌───────────────┐
        │     INPUT     │
        │   (URL link)  │
        └───────┬───────┘
                │
                ▼
     ┌─────────────────────┐
     │  DETECT PLATFORM    │
     │ youtube / instagram │
     └───────┬─────────────┘
             │
     ┌───────┴────────┬──────────────┐
     ▼                ▼              ▼
┌───────────┐   ┌────────────┐   ┌───────────┐
│ Instagram │   │  YouTube   │   │   Other   │
└────┬──────┘   └────┬───────┘   └────┬──────┘
     │               │                │
     ▼               ▼                ▼
┌─────────────┐  ┌─────────────┐  ┌────────────┐                
│ Extract ID  │  │ Extract ID  │  │  INVALID   │----------------| print error message | 
└────┬────────┘  └────┬────────┘  └────────────┘                
     │                │                                          
     ▼                ▼
┌─────────────────┐  ┌────────────────────────┐
│ Create IG Embed │  │ Create YT Embed        │
│ instagram.com   │  │ youtube.com/embed/id   │
│ /p/id/embed     │  └───────────┬────────────┘
└────┬────────────┘              │
     │                           │
     └──────────────┬────────────┘
                    ▼
         ┌──────────────────────┐
         │  WRAP IN IFRAME      │
         │ <iframe src="...">   │
         └──────────┬───────────┘
                    │
                    ▼
         ┌──────────────────────┐
         │   SAVE / OUTPUT      │
         │ Original + Embed     │
         └──────────────────────┘
```
