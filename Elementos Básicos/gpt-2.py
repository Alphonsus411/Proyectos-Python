from gpt2_client import GPT2Client

gpt2 = GPT2Client('117M')  # This could also be `345M`, `774M`, or `1558M`. Rename `save_dir` to anything.
gpt2.load_model(force_download=False)  # Use cached versions if available.
