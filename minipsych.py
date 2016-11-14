from watson_developer_cloud import PersonalityInsightsV3
from os.path import join, dirname
import json
import sys

creds = {
  "url": "https://gateway.watsonplatform.net/personality-insights/api",
  "password": "____________",
  "username": "_____________________"
}

def update_insights(client_name):
	# Pass the email you get in mail_recv into this function.
	# Make it update the json you have for that user's emotion.
		 jsonFile = open("client_name", "r")
		 data = json.load(jsonFile)
		 jsonFile.close()

		content = []
        for message in data:
            email_message = parser.Parser().parsestr(message)
            date_returned = email.utils.parsedate(email_content["Date"])
            if date_returned is None:
                return
            miliseconds_since = int(time.mktime(date_returned) * 1000)


            if email_content.is_multipart():
                email_data = email_content.get_payload(0)
            else:
                email_data = email_content.get_payload()

            id = email_content["Message-Id"]

            content.append({
                "content": content,
                "contenttype": "text/plain",
                "created": miliseconds_since,
                "id": id,
                "language": "en"
            })

        output = {
            "contentItems": content
        }
		jsonFile = open("client_progress", "w")
		jsonFile.write(json.dumps(output))
		jsonFile.close()
	## To do this, use file.open on the json file to open it, and then use file.read to make it a string.
	## With the string, use json.loads (I think) to convert it to json, append to the dictonary, then
	##convert it back into json and write it back into the file.
	# Then, call your analyzer.
	# U got this.


personality_insights = PersonalityInsightsV3(
    version='2016-10-20',
    username=creds['username'],
    password=creds['password'])

def smell_what_the_rock_is_cooking(path_to_emotions):
	with open(join(path_to_emotions)) as profile_json:
		profile = personality_insights.profile(
		    profile_json.read(), content_type='application/json',
		    raw_scores=True, consumption_preferences=True)

		print(json.dumps(profile, indent=2))

if __name__ == "__main__":
	smell_what_the_rock_is_cooking(sys.argv[1])

	
