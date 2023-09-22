import openai

key = open("api_key_holster.txt", "r").readline().strip('\n')
openai.api_key = key
response = openai.File.create(file=open("bio.jsonl", "rb"), purpose='fine-tune')

print(f"id: {response['id']}")

openai.FineTuningJob.create(training_file=response['id'], model="gpt-3.5-turbo")  # send the dataset for a fine-tune job

# openai.FineTuningJob.retrieve(response['id']) # retrieve the fine tune job - retrieve the state
# openai.FineTuningJob.list(limit=10) # List all the fine-tune jobs by ID
