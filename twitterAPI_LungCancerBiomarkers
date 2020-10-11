#using twitter API ID_LC Biomarkers in tweet

install.packages("twitteR")
library(twitteR)

api_key <- "XXXXXXXXXXXXX"
api_secret <- "XXXXXXXXXXXXX"
token <- "XXXXXXXXXXXXX"
token_secret <- "XXXXXXXXXXXXX"

setup_twitter_oauth(api_key, api_secret, token, token_secret)

tweetsLCBiomakers10_8 <- searchTwitter("lung and cancer and biomarkers", n=400, lang = "en")

tweetsLC.df <- twListToDF(tweetsLCBiomakers10_8)

write.csv(tweetsLC.df, "tweetsLCBiomarkers10_8.csv")

tweetsLC.df
